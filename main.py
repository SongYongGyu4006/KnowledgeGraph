from pykeen.pipeline import pipeline

result = pipeline(
    model='TransE',
    dataset='nations',
    ##epcohs의 default값은 5임.
)

print(result.metric_results.to_df())