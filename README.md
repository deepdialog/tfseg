# Chinese Word Segmentation with TensorFlow

solution: Albert + CRF

接口类似jieba

安装：`pip install tfseg`

分词：

```python
>>> import tfseg
>>> tfseg.lcut('我爱北京天安门')
['我', '爱', '北京', '天安门']
```

词性：

```python
>>> from tfseg import posseg
>>> posseg.lcut('我爱北京天安门')
[('我', 'r'), ('爱', 'v'), ('北京', 'ns'), ('天安门', 'ns')]
```