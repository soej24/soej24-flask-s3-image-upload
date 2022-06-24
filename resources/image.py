from datetime import datetime
from http import HTTPStatus
from os import access
from flask import request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql.connector.errors import Error
import mysql.connector

class FileUploadResource(Resource) :

    def post(self) :

        # 1. 클라이언트로부터 데이터를 받아온다.
        # request.files 에 파일을 받아온다.
        # 따라서 파일이 없는 상태로 API 가 호출되면,
        # 에러메세지를 클라이런트에 응답해주자.

        # photo란 클라이언틍서 보내는 key!!
        if 'photo' not in request.files:
            return {'error' : '파일을 업로드 하세요'}, 400

        # 클라이언트로부터 파일을 받아온다.
        file = request.files['photo']

        # 파일명을 우리가 변경해 준다. (파일명이 중복되서 올라가면 안되기 때문에~)
        # 파일명은 유니크하게 만들어야 한다.
        current_time = datetime.now()
        new_file_name = current_time.isoformat().replace(':', '_')

        # 유저가 올린 파일의 이름을 내가 만든 파일 명으로 변경
        file.filename = new_file_name

        # S3에 업로드 하면 된다.
        # AWS의 라이브러리를 사용해야 한다.
        # 이 파이썬 라이브러리를 boto3 라이브러리!
        # boto3 라이브러리 설치
        # pip install boto3



        return