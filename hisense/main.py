# -*- coding: utf-8 -*-
from hisense.Dispatch import Dispatch

if __name__ == '__main__':
    # socketServer = SocketServer()
    # socketServer.startProject()

    dispatch = Dispatch()
    dispatch.dispatch('requestAllDate')
