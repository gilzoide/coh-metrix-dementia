# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from coh import base
from coh.resource_pool import rp as default_rp


class PersonalPronounsIncidence(base.Metric):
    """
    """
    name = 'Personal pronouns incidence'
    column_name = 'personal_pronouns'

    personal_pronouns = ['eu', 'tu', 'ele', 'ela', 'nós', 'vós', 'eles',
                         'elas', 'você', 'vocês']

    def __init__(self):
        super(PersonalPronounsIncidence, self).__init__()

    def value_for_text(self, t, rp=default_rp):
        words = [word.lower() for word in rp.all_words(t)]
        n_personal_pronouns = sum([word in self.personal_pronouns
                                   for word in words])
        return n_personal_pronouns / len(words)


class PronounsPerNounPhrase(base.Metric):
    """
    """
    name = 'Mean pronouns per noun phrase'
    column_name = 'pronouns_per_np'

    def value_for_text(self, t, rp=default_rp):
        raise NotImplementedError('Waiting for syntactic parser')


class TypeTokenRatio(base.Metric):
    """
    """
    name = 'Type to token ratio'
    column_name = 'ttr'

    def __init__(self):
        super(TypeTokenRatio, self).__init__()

    def value_for_text(self, t, rp=default_rp):
        words = [word.lower() for word in rp.all_words(t)]
        return len(set(words)) / len(words)


class Tokens(base.Category):
    name = 'Pronouns, Types and Tokens'
    table_name = 'tokens'

    def __init__(self):
        super(Tokens, self).__init__()
        self._set_metrics_from_module(__name__)
        self.metrics.sort(key=lambda m: m.name)
        # TODO: remove when PronounsPerNounPhrase is ready.
        del self.metrics[0]

    def values_for_text(self, t, rp=default_rp):
        return super(Tokens, self).values_for_text(t, rp)