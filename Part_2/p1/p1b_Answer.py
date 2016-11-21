# -*- coding: utf-8 -*-

def sortQueue(data):
    return sorted(data, key=lambda x: float(x[0])/x[1], reverse=True)
# END sortQueue