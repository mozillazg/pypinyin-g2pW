# -*- coding: utf-8 -*-

from pypinyin.constants import RE_HANS
from pypinyin.core import Pinyin, Style
from pypinyin.seg.simpleseg import simple_seg
from pypinyin.converter import UltimateConverter
from pypinyin.contrib.tone_convert import to_tone
from g2pw.api import G2PWConverter


class G2PWPinyin(Pinyin):
    def __init__(self, model_dir='G2PWModel/', model_source=None,
                 num_workers=None, batch_size=None,
                 turnoff_tqdm=True, enable_non_tradional_chinese=True,
                 v_to_u=False, neutral_tone_with_five=False, tone_sandhi=False, **kwargs):
        self._g2pw = G2PWConverter(
            model_dir=model_dir,
            style='pinyin',
            model_source=model_source,
            num_workers=num_workers,
            batch_size=batch_size,
            turnoff_tqdm=turnoff_tqdm,
            enable_non_tradional_chinese=enable_non_tradional_chinese,
        )
        self._converter = Converter(
            self._g2pw, v_to_u=v_to_u,
            neutral_tone_with_five=neutral_tone_with_five,
            tone_sandhi=tone_sandhi,
        )

    def get_seg(self, **kwargs):
        return simple_seg


class Converter(UltimateConverter):
    def __init__(self, g2pw_instance, v_to_u=False,
                 neutral_tone_with_five=False,
                 tone_sandhi=False, **kwargs):
        super(Converter, self).__init__(
            v_to_u=v_to_u,
            neutral_tone_with_five=neutral_tone_with_five,
            tone_sandhi=tone_sandhi, **kwargs)

        self._g2pw = g2pw_instance

    def convert(self, words, style, heteronym, errors, strict, **kwargs):
        pys = []
        if RE_HANS.match(words):
            pys = self._to_pinyin(words, style=style, heteronym=heteronym,
                                  errors=errors, strict=strict)
            post_data = self.post_pinyin(words, heteronym, pys)
            if post_data is not None:
                pys = post_data

            pys = self.convert_styles(
                pys, words, style, heteronym, errors, strict)

        else:
            py = self.handle_nopinyin(words, style=style, errors=errors,
                                      heteronym=heteronym, strict=strict)
            if py:
                pys.extend(py)

        return _remove_dup_and_empty(pys)

    def _to_pinyin(self, han, style, heteronym, errors, strict, **kwargs):
        g2pw_pinyin = self._g2pw(han)

        if not g2pw_pinyin:  # g2pw 不支持的汉字改为使用 pypinyin 原有逻辑
            return super(Converter, self).convert(
                         han, Style.TONE, heteronym, errors, strict, **kwargs)

        pinyins = []

        for i, item in enumerate(g2pw_pinyin[0]):
            if item is None:  # g2pw 不支持的汉字改为使用 pypinyin 原有逻辑
                py = super(Converter, self).convert(
                           han[i], Style.TONE, heteronym, errors, strict, **kwargs)
                pinyins.extend(py)
            else:
                pinyins.append([to_tone(item)])

        return pinyins


def _remove_dup_items(lst, remove_empty=False):
    new_lst = []
    for item in lst:
        if remove_empty and not item:
            continue
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


def _remove_dup_and_empty(lst_list):
    new_lst_list = []
    for lst in lst_list:
        lst = _remove_dup_items(lst, remove_empty=True)
        if lst:
            new_lst_list.append(lst)
        else:
            new_lst_list.append([''])

    return new_lst_list
