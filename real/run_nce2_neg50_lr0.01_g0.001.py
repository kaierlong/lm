#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yunchuan Chen'

from utils import get_unigram_probtable
from models import NCELangModelV2
from keras.optimizers import AdamAnneal

NB_RUN_WORDS = 100000000
NB_VOCAB = 10000
NB_RUN_VAL = 100000
NB_EVALUATE = 5000000
SAVE_PATH = '../data/models/lang/nce2-neg50-e128-c128-lr0.01-gamma0.001.pkl'

DATA_PATH = '../data/corpus/wiki-sg-norm-lc-drop-bin.bz2'
BATCH_SIZE = 256
VAL_INTER = 1200

unigram_table = get_unigram_probtable(nb_words=NB_VOCAB)

opt = AdamAnneal(lr=0.01, lr_min=0.0045, gamma=0.001)
model = NCELangModelV2(vocab_size=NB_VOCAB, nb_negative=50, embed_dims=128, context_dims=128,
                       negprob_table=unigram_table, optimizer=opt)
model.compile()
model.train(data_file=DATA_PATH,
            save_path=SAVE_PATH,
            batch_size=BATCH_SIZE, train_nb_words=NB_RUN_WORDS,
            val_nb_words=NB_EVALUATE, train_val_nb=NB_RUN_VAL, validation_interval=VAL_INTER)