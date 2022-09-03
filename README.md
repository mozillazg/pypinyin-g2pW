# pypinyin-g2pW

基于 [g2pW](https://github.com/GitYCC/g2pW/) 提升 [pypinyin](https://github.com/mozillazg/python-pinyin) 的准确性。

特点：

* 可以通过训练模型的方式提升拼音准确性。
* 功能和使用习惯与 pypinyin 基本保持一致，支持多种拼音风格。


## 使用

### 安装依赖

1. 安装 [PyTorch](https://pytorch.org/get-started/locally/)。
2. 下载并解压 G2PWModel:

    ```
    wget https://storage.googleapis.com/esun-ai/g2pW/G2PWModel-v2-onnx.zip
    unzip G2PWModel-v2-onnx.zip
    ```
3. 安装 [git-lfs](https://git-lfs.github.com/)。
4. 下载 [bert-base-chinese](https://huggingface.co/bert-base-chinese):

   ```
   git lfs install
   git clone https://huggingface.co/bert-base-chinese
   ```
5. 安装本项目:

   ```
   pip install pypinyin-g2pw
   ```

### 使用示例

   ```python
   >>> from pypinyin import Style
   >>> from pypinyin_g2pw import G2PWPinyin

   # 需要将 model_dir 和 model_source 的值指向下载的模型数据目录
   >>> g2pw = G2PWPinyin(model_dir='G2PWModel/',
                         model_source='bert-base-chinese/',
                         v_to_u=False, neutral_tone_with_five=True)
   >>> han = '然而，他红了20年以后，他竟退出了大家的视线。'

   # def lazy_pinyin(self, hans, style=Style.NORMAL, errors='default', strict=True, **kwargs)
   # 通过 lazy_pinyin 方法获取拼音数据，各个参数的含义和作用跟 pypinyin 中是一样的，
   # v_to_u 和 neutral_tone_with_five 参数只能在初始化 G2PWPinyin 时指定。

   >>> g2pw.lazy_pinyin(han)
   ['ran', 'er', '，', 'ta', 'hong', 'le', '20', 'nian', 'yi', 'hou', '，', 'ta', 'jing', 'tui', 'chu', 'le', 'da', 'jia', 'de', 'shi', 'xian', '。']

   >>> g2pw.lazy_pinyin(han, style=Style.TONE)
   ['rán', 'ér', '，', 'tā', 'hóng', 'le', '20', 'nián', 'yǐ', 'hòu', '，', 'tā', 'jìng', 'tuì', 'chū', 'le', 'dà', 'jiā', 'de', 'shì', 'xiàn', '。']

   >>> g2pw.lazy_pinyin(han, style=Style.TONE3)
   ['ran2', 'er2', '，', 'ta1', 'hong2', 'le5', '20', 'nian2', 'yi3', 'hou4', '，', 'ta1', 'jing4', 'tui4', 'chu1', 'le5', 'da4', 'jia1', 'de5', 'shi4', 'xian4', '。']
   ```

## 离线使用

默认情况下，即便使用了离线的模型数据，程序使用的 transformers 模块仍旧会从 huggingface.co 下载部分模型元数据。
可以通过设置环境变量 `TRANSFORMERS_OFFLINE=1` 以及环境变量 `HF_DATASETS_OFFLINE=1` 禁用获取元数据的操作，实现完全离线使用的需求。
详见 [transformers 官方文档](https://huggingface.co/docs/transformers/v4.21.2/en/installation#offline-mode)。


## 模型训练

详见 [g2pW](https://github.com/GitYCC/g2pW/#train-model) 官方文档中的说明。
