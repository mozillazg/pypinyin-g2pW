# -*- coding: utf-8 -*-
import os
import time

from pypinyin import lazy_pinyin, Style

from pypinyin_g2pw import G2PWPinyin

model_dir = os.getenv('MODEL_DIR', 'G2PWModel/G2PWModel-v2/')
model_source = os.getenv('MODEL_SOURCE', 'bert-base-chinese/')


def test_lazy_pinyin():
    han = ('它没有婆娑的姿态，没有屈曲盘旋的虬枝，也许你要说它不美丽，'
           '——如果美是专指“婆娑”或“横斜逸出”之类而言，那么，'
           '白杨树算不得树中的好女子；但是它却是伟岸，正直，朴质，严肃，'
           '也不缺乏温和，更不用提它的坚强不屈与挺拔，它是树中的伟丈夫！')
    g2pw = G2PWPinyin(model_dir=model_dir, model_source=model_source)

    now = time.time()
    p1 = lazy_pinyin(han, style=Style.TONE3)
    t1 = time.time() - now

    now = time.time()
    p2 = g2pw.lazy_pinyin(han, style=Style.TONE3)
    t2 = time.time() - now

    print('han: \n{}'.format(han))

    print('pypinyin {}s: \n{}'.format(t1, ' '.join(p1)))

    print('pypinyin_g2pw {}s: \n{}'.format(t2, ' '.join(p2)))


if __name__ == '__main__':
    test_lazy_pinyin()
