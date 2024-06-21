Setting up LLMs

Prerequisites:
- Install [Docker](https://docs.docker.com/engine/install/) (LTS version)
- Install [Postman](https://www.postman.com/downloads/) API Client (Optional)


How to build
`docker compose build --progress=plain`

How to run Images
`docker compose up`

Stop docker images
`docker-compose down`

API to call
POST `http://localhost:5000/ask`
Data `{ prompt:"why sky is blue" }`

example response
`[
    [
        {
            "model": "phi3",
            "resp": [
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:07.792629444Z",
                    "response": " Hello",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:08.003989693Z",
                    "response": "!",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:08.226448892Z",
                    "response": " How",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:08.439052006Z",
                    "response": " can",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:08.649110639Z",
                    "response": " I",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:08.857398067Z",
                    "response": " assist",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:09.06695029Z",
                    "response": " you",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:09.276579488Z",
                    "response": " today",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:09.485384311Z",
                    "response": "?",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:09.707610024Z",
                    "response": " Whether",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:09.917922412Z",
                    "response": " it",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:10.128676587Z",
                    "response": "'",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:10.33391244Z",
                    "response": "s",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:10.542854201Z",
                    "response": " answering",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:10.752843349Z",
                    "response": " questions",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:10.962289194Z",
                    "response": ",",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:11.170030302Z",
                    "response": " providing",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:11.387814469Z",
                    "response": " information",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:11.596944318Z",
                    "response": ",",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:11.80820749Z",
                    "response": " or",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:12.02241451Z",
                    "response": " gu",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:12.232189189Z",
                    "response": "iding",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:12.438648127Z",
                    "response": " you",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:12.6497557Z",
                    "response": " through",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:12.866534788Z",
                    "response": " a",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:13.074263033Z",
                    "response": " process",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:13.281187763Z",
                    "response": ",",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:13.487977526Z",
                    "response": " feel",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:13.699609968Z",
                    "response": " free",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:13.908016269Z",
                    "response": " to",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:14.117564204Z",
                    "response": " share",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:14.334200127Z",
                    "response": " what",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:14.548399449Z",
                    "response": " you",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:14.760213605Z",
                    "response": " need",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:14.973751014Z",
                    "response": " help",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:15.185546511Z",
                    "response": " with",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:15.397024179Z",
                    "response": ".",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:15.611587165Z",
                    "response": "\n",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:15.83327104Z",
                    "response": "\n",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:16.047194803Z",
                    "response": "(",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:16.256666754Z",
                    "response": "Note",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:16.461699328Z",
                    "response": ":",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:16.672119695Z",
                    "response": " This",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:16.881569918Z",
                    "response": " response",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:17.088083237Z",
                    "response": " is",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:17.300058973Z",
                    "response": " craft",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:17.505097563Z",
                    "response": "ed",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:17.720021905Z",
                    "response": " as",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:17.929637026Z",
                    "response": " an",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:18.137267071Z",
                    "response": " example",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:18.343031805Z",
                    "response": " of",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:18.549347668Z",
                    "response": " a",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:18.756152574Z",
                    "response": " simple",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:18.968684175Z",
                    "response": " gre",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:19.178443654Z",
                    "response": "eting",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:19.386403421Z",
                    "response": " interaction",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:19.602388056Z",
                    "response": " that",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:19.811532689Z",
                    "response": " might",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:20.019551798Z",
                    "response": " occur",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:20.226486716Z",
                    "response": " in",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:20.448327532Z",
                    "response": " various",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:20.664395571Z",
                    "response": " context",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:20.8773232Z",
                    "response": "s",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:21.086361699Z",
                    "response": " such",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:21.297609119Z",
                    "response": " as",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:21.510083928Z",
                    "response": " customer",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:21.723231783Z",
                    "response": " service",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:21.940158253Z",
                    "response": ",",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:22.152140786Z",
                    "response": " for",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:22.364594207Z",
                    "response": "ums",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:22.580201515Z",
                    "response": ",",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:22.798899844Z",
                    "response": " or",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:23.020452669Z",
                    "response": " general",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:23.235578067Z",
                    "response": " convers",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:23.459055077Z",
                    "response": "ations",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:23.677299435Z",
                    "response": ".)",
                    "done": false
                },
                {
                    "model": "phi3",
                    "created_at": "2024-06-21T10:31:23.892317387Z",
                    "response": "",
                    "done": true,
                    "done_reason": "stop",
                    "context": [
                        32010,
                        7251,
                        32007,
                        32001,
                        15043,
                        29991,
                        1128,
                        508,
                        306,
                        6985,
                        366,
                        9826,
                        29973,
                        26460,
                        372,
                        29915,
                        29879,
                        22862,
                        5155,
                        29892,
                        13138,
                        2472,
                        29892,
                        470,
                        1410,
                        4821,
                        366,
                        1549,
                        263,
                        1889,
                        29892,
                        4459,
                        3889,
                        304,
                        6232,
                        825,
                        366,
                        817,
                        1371,
                        411,
                        29889,
                        13,
                        13,
                        29898,
                        9842,
                        29901,
                        910,
                        2933,
                        338,
                        25554,
                        287,
                        408,
                        385,
                        1342,
                        310,
                        263,
                        2560,
                        1395,
                        15133,
                        14881,
                        393,
                        1795,
                        6403,
                        297,
                        5164,
                        3030,
                        29879,
                        1316,
                        408,
                        11962,
                        2669,
                        29892,
                        363,
                        6762,
                        29892,
                        470,
                        2498,
                        9678,
                        800,
                        1846,
                        32007
                    ],
                    "total_duration": 16685516040,
                    "load_duration": 1285700,
                    "prompt_eval_count": 3,
                    "prompt_eval_duration": 542324000,
                    "eval_count": 77,
                    "eval_duration": 16099648000
                }
            ]
        }
    ],
    []
]`