import seqio
import t5
import tensorflow as tf
import functools
from typing import Dict
import metrics

TaskRegistry = seqio.TaskRegistry
DEFAULT_OUTPUT_FEATURES = {
    "inputs": seqio.Feature(
        vocabulary=t5.data.get_default_vocabulary(), add_eos=True,
        required=False),
    "targets": seqio.Feature(
        vocabulary=t5.data.get_default_vocabulary(), add_eos=True)
}

def registerTask(task: str, splits: Dict, metric_name: str):
  def parseDataset(split: str, shuffle_files: bool = False, seed: int = 0):
    ds = tf.data.TextLineDataset([splits[split]])
    ds = ds.map(
    functools.partial(tf.io.decode_csv, record_defaults=["", ""],
                      field_delim="\t", use_quote_delim=False),
    num_parallel_calls=tf.data.experimental.AUTOTUNE)
    ds = ds.map(lambda *ex: dict(zip(["input", "target"], ex)))
    return ds
  def preprocessor(ds):
    def to_inputs_and_targets(ex):
      """Map {"inputs": ..., "targets": ...}->{"inputs": {task}..., "targets": ...}."""
      return {
          "inputs":ex["input"],
          "targets": ex["target"]
      }
    return ds.map(to_inputs_and_targets, 
                  num_parallel_calls=tf.data.experimental.AUTOTUNE)
  
  TaskRegistry.remove(task)
  TaskRegistry.add(
      task,
      source=seqio.FunctionDataSource(
          dataset_fn=parseDataset,
          splits=list(splits.keys())
      ),
      preprocessors=[preprocessor, 
          seqio.preprocessors.tokenize,
          seqio.CacheDatasetPlaceholder(),
          seqio.preprocessors.append_eos_after_trim,
      ],
      output_features=DEFAULT_OUTPUT_FEATURES,
      metric_fns=[metrics.map_name_to_metric_function(metric_name)]
  )
