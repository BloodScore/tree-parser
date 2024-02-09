import json
import xml
import xmltodict

from fastapi import APIRouter, HTTPException, Request, status

from src.parser import parser


api_router = APIRouter(
    prefix='/api',
    tags=['api']
)


@api_router.post('/parse-tree')
async def parse_tree(request: Request):
    content_type = request.headers.get('content-type')

    try:
        if content_type == 'application/json':
            try:
                body = await request.json()

                tree = parser.parse(body)

                return tree
            except json.decoder.JSONDecodeError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Missing or invalid json'
                )
        elif content_type == 'application/xml':
            try:
                body = await request.body()
                body = body.decode('utf-8')

                body = xmltodict.parse(body)

                tree = parser.parse(body)

                return tree
            except xml.parsers.expat.ExpatError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Missing or invalid xml'
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail=f'Unsupported media type {content_type}'
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Internal error. {e}'
        )
