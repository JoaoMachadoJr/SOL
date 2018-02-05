#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.requests import Session, Request
from lib.requests.adapters import HTTPAdapter
from lib.requests.packages.urllib3.util.retry import Retry

class Conection:
    """
    Essa classe será usada para controlar a comunicação com o site facebook.com
    """

    maxretries = 10
    timeout = (5,5)

    @staticmethod
    def get(url : str, params : dict = None) -> dict:
        """
        Esse método envia para o facebook a url passada por parâmetro, e devolve a resposta

        Args:
            url:    O endereço para onde será feita a requisição
            params: Os parâmetros da requisição
        :return: o JSON contendo a resposta da requisição
        """
        sessao = Session()
        sessao.mount('https://', HTTPAdapter(max_retries=Retry(total=Conection.maxretries)))
        rslt= sessao.get(url,timeout=Conection.timeout, params=params).json()
        if "error" in rslt:
            raise Exception('Error on request:'+str(rslt['error']))
        else:
            return rslt

    @staticmethod
    def post(url : str, files : dict = None, params : dict = None) -> dict:
        """
        Esse método envia para o facebook a url passada por parâmetro, e devolve a resposta

        Args:
            url:    O endereço para onde será feita a requisição
            params: Os parâmetros da requisição
        :return: o JSON contendo a resposta da requisição
        """
        sessao = Session()
        sessao.mount('https://', HTTPAdapter(max_retries=Retry(total=Conection.maxretries)))
        if files is None:
            rslt= sessao.post(url,timeout=Conection.timeout, params=params).json()
        else:
            rslt= sessao.post(url, timeout=Conection.timeout, params=params, files=files).json()
        if "error" in rslt:
            raise Exception('Error on request:'+str(rslt['error']))
        else:
            return rslt

