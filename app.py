from flask import Flask, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# 간단한 API 엔드포인트
@app.route('/manifest.json', methods=['GET'])
def test_api():
    # 반환할 JSON 데이터

    manifest_data = {
  "@context": [
    "http://www.w3.org/ns/anno.jsonld",
    "http://iiif.io/api/presentation/3/context.json"
  ],
  "id": "https://biiif-template-example-3kntb3jpl-mnemoscene.vercel.app/video/index.json",
  "type": "Manifest",
  "items": [
    {
      "id": "https://biiif-template-example-3kntb3jpl-mnemoscene.vercel.app/video/index.json/canvas/0",
      "type": "Canvas",
      "items": [
        {
          "id": "https://biiif-template-example-3kntb3jpl-mnemoscene.vercel.app/video/index.json/canvas/0/annotationpage/0",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://biiif-template-example-3kntb3jpl-mnemoscene.vercel.app/video/index.json/canvas/0/annotation/0",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://biiif-template-example-3kntb3jpl-mnemoscene.vercel.app/video/_bigbuckbunny/bbb-butterfly.mp4",
                "type": "Video",
                "format": "video/mp4",
                "label": {
                  "@none": [
                    "_bigbuckbunny"
                  ]
                }
              },
              "target": "https://biiif-template-example-3kntb3jpl-mnemoscene.vercel.app/video/index.json/canvas/0"
            }
          ]
        }
      ],
      "label": {
        "@none": [
          "_bigbuckbunny"
        ]
      },
      "duration": 10
    }
  ],
  "label": {
    "@none": [
      "Big Buck Bunny"
    ]
  }
}

# http://localhost:8080/api/iiif/v2/kmImages/OjppdGVtOjpmMjAyNDA2MjBQMnlwLnBuZzo67J207ZiE7IS4IOy0iOq4sCDsnpHtkojsnbQg67O07Jes7KO864qUIO2YgeyLoOyEsS5wbmc=/full/max/0/default.jpg
    # JSON 데이터를 UTF-8로 반환
    response = Response(
        response=json.dumps(manifest_data, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    return response

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
