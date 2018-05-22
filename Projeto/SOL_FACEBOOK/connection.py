#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.requests import Session
from lib.requests.adapters import HTTPAdapter
from lib.requests.packages.urllib3.util.retry import Retry


class Connection:
    """
    Essa classe será usada para controlar a comunicação com o site facebook.com
    """

    max_retries = 10
    timeout = (5, 5)

    @staticmethod
    def get(url: str, params: dict = None) -> dict:
        """
        Esse método envia para o facebook a url passada por parâmetro, e devolve a resposta

        Args:
            url:    O endereço para onde será feita a requisição
            params: Os parâmetros da requisição
        :return: o JSON contendo a resposta da requisição
        """
        sessao = Session()
        sessao.mount('https://', HTTPAdapter(max_retries=Retry(total=Connection.max_retries)))
        result = sessao.get(url, timeout=Connection.timeout, params=params).json()
        if "error" in result:
            raise Exception('Error on request:' + str(result['error']))
        else:
            return result

    @staticmethod
    def post(url: str, files: dict = None, params: dict = None) -> dict:
        """
        Esse método envia para o facebook a url passada por parâmetro, e devolve a resposta

        Args:
            url:    O endereço para onde será feita a requisição
            params: Os parâmetros da requisição
        :return: o JSON contendo a resposta da requisição
        """
        sessao = Session()
        sessao.mount('https://', HTTPAdapter(max_retries=Retry(total=Connection.max_retries)))
        if files is None:
            result = sessao.post(url, timeout=Connection.timeout, params=params).json()
        else:
            result = sessao.post(url, timeout=Connection.timeout, params=params, files=files).json()
        if "error" in result:
            raise Exception('Error on request:' + str(result['error']))
        else:
            return result
