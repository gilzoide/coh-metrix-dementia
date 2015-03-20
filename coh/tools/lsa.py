# -*- coding: utf-8 -*-
# Coh-Metrix-Dementia - Automatic text analysis and classification for dementia.
# Copyright (C) 2014  Andre Luiz Verucci da Cunha
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, print_function, division
from gensim.corpora import Dictionary
from gensim.models import LsiModel
from gensim.matutils import cossim


class LsaSpace(object):
    """Represents an LSA space, that can be used to compute similarities
    between text fragments (texts, paragraphs, sentences, and so on).
    """

    def __init__(self, dict_path, model_path):
        """Load an LSA space from a file.

        :dict_path: path to the dictionary file.
        :model_path: path to the model file.
        """
        self._dictionary = Dictionary.load_from_text(dict_path)
        self._lsi_model = LsiModel.load(model_path)

    def compute_similarity(self, doc1, doc2):
        """Compute the cosine similarity between two documents.

        :doc1: a list of strings, representing the first document.
        :doc2: a list of strings, representing the second document.
        :returns: a number between -1 and 1, representing the similarity
        between the two documents.
        """
        doc1_lsi = self._lsi_model[self._dictionary.doc2bow(doc1)]
        doc2_lsi = self._lsi_model[self._dictionary.doc2bow(doc2)]

        return cossim(doc1_lsi, doc2_lsi)


if __name__ == '__main__':
    from coh.conf import config

    space = LsaSpace(
        '/home/andre/Develop/corpora/lsamodel_wordids_350k.txt.bz2',
        '/home/andre/Develop/corpora/lsamodel_lsi.model')

    space = LsaSpace(config['LSA_DICT_PATH'], config['LSA_MODEL_PATH'])

    print(space.compute_similarity('o livro está sobre a mesa'.split(' '),
                                   'o livro está sobre a cadeira'.split(' ')))

    print(space.compute_similarity('o livro está sobre a mesa'.split(' '),
                                   'o livro está sobre a árvore'.split(' ')))

    print(space.compute_similarity('o livro está sobre a mesa'.split(' '),
                                   'maria foi ao mercado'.split(' ')))