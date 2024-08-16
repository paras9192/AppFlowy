{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyOdEL6rmqLrE6zKRuSA6MBy",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/paras9192/AppFlowy/blob/main/Langchain.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F3c87GprTHZG",
        "outputId": "7de8f3f2-6c70-44d1-e5bb-a3cf7705cd2b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain\n",
            "  Downloading langchain-0.2.14-py3-none-any.whl.metadata (7.1 kB)\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.37.1-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Collecting pypdf2\n",
            "  Downloading pypdf2-3.0.1-py3-none-any.whl.metadata (6.8 kB)\n",
            "Collecting python-dotenv\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Collecting faiss-cpu\n",
            "  Downloading faiss_cpu-1.8.0.post1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.7 kB)\n",
            "Requirement already satisfied: huggingface-hub in /usr/local/lib/python3.10/dist-packages (0.23.5)\n",
            "Collecting InstructorEmbedding==1.0.1\n",
            "  Downloading InstructorEmbedding-1.0.1-py2.py3-none-any.whl.metadata (20 kB)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (6.0.2)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.0.32)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain) (3.10.2)\n",
            "Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from langchain) (4.0.3)\n",
            "Collecting langchain-core<0.3.0,>=0.2.32 (from langchain)\n",
            "  Downloading langchain_core-0.2.32-py3-none-any.whl.metadata (6.2 kB)\n",
            "Collecting langchain-text-splitters<0.3.0,>=0.2.0 (from langchain)\n",
            "  Downloading langchain_text_splitters-0.2.2-py3-none-any.whl.metadata (2.1 kB)\n",
            "Collecting langsmith<0.2.0,>=0.1.17 (from langchain)\n",
            "  Downloading langsmith-0.1.99-py3-none-any.whl.metadata (13 kB)\n",
            "Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (1.26.4)\n",
            "Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.8.2)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain) (2.32.3)\n",
            "Collecting tenacity!=8.4.0,<9.0.0,>=8.1.0 (from langchain)\n",
            "  Downloading tenacity-8.5.0-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.4.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<5,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl.metadata (38 kB)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub) (3.15.4)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub) (2024.6.1)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub) (4.66.5)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.3.5)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (24.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.0.5)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.9.4)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
            "Collecting jsonpatch<2.0,>=1.33 (from langchain-core<0.3.0,>=0.2.32->langchain)\n",
            "  Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)\n",
            "Collecting orjson<4.0.0,>=3.9.14 (from langsmith<0.2.0,>=0.1.17->langchain)\n",
            "  Downloading orjson-3.10.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (50 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.4/50.4 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.20.1 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain) (2.20.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain) (2024.7.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.0.3)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Collecting jsonpointer>=1.9 (from jsonpatch<2.0,>=1.33->langchain-core<0.3.0,>=0.2.32->langchain)\n",
            "  Downloading jsonpointer-3.0.0-py2.py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Downloading InstructorEmbedding-1.0.1-py2.py3-none-any.whl (19 kB)\n",
            "Downloading langchain-0.2.14-py3-none-any.whl (997 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m997.8/997.8 kB\u001b[0m \u001b[31m18.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading streamlit-1.37.1-py2.py3-none-any.whl (8.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.7/8.7 MB\u001b[0m \u001b[31m90.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pypdf2-3.0.1-py3-none-any.whl (232 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m232.6/232.6 kB\u001b[0m \u001b[31m24.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading faiss_cpu-1.8.0.post1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (27.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m27.0/27.0 MB\u001b[0m \u001b[31m59.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m20.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_core-0.2.32-py3-none-any.whl (389 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m389.8/389.8 kB\u001b[0m \u001b[31m35.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_text_splitters-0.2.2-py3-none-any.whl (25 kB)\n",
            "Downloading langsmith-0.1.99-py3-none-any.whl (140 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m140.4/140.4 kB\u001b[0m \u001b[31m10.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m93.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tenacity-8.5.0-py3-none-any.whl (28 kB)\n",
            "Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.9/82.9 kB\u001b[0m \u001b[31m8.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)\n",
            "Downloading orjson-3.10.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m141.9/141.9 kB\u001b[0m \u001b[31m14.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)\n",
            "Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: InstructorEmbedding, watchdog, tenacity, smmap, python-dotenv, pypdf2, orjson, jsonpointer, faiss-cpu, pydeck, jsonpatch, gitdb, langsmith, gitpython, langchain-core, streamlit, langchain-text-splitters, langchain\n",
            "  Attempting uninstall: tenacity\n",
            "    Found existing installation: tenacity 9.0.0\n",
            "    Uninstalling tenacity-9.0.0:\n",
            "      Successfully uninstalled tenacity-9.0.0\n",
            "Successfully installed InstructorEmbedding-1.0.1 faiss-cpu-1.8.0.post1 gitdb-4.0.11 gitpython-3.1.43 jsonpatch-1.33 jsonpointer-3.0.0 langchain-0.2.14 langchain-core-0.2.32 langchain-text-splitters-0.2.2 langsmith-0.1.99 orjson-3.10.7 pydeck-0.9.1 pypdf2-3.0.1 python-dotenv-1.0.1 smmap-5.0.1 streamlit-1.37.1 tenacity-8.5.0 watchdog-4.0.2\n"
          ]
        }
      ],
      "source": [
        "!pip install langchain streamlit pypdf2 python-dotenv faiss-cpu huggingface-hub InstructorEmbedding==1.0.1"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install sentence-transformers"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ysxXqKYTjZFH",
        "outputId": "00c14817-ff46-4d31-a798-d0fa9ce1edce"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: sentence-transformers in /usr/local/lib/python3.10/dist-packages (3.0.1)\n",
            "Requirement already satisfied: transformers<5.0.0,>=4.34.0 in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (4.42.4)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (4.66.5)\n",
            "Requirement already satisfied: torch>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (2.3.1+cu121)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (1.26.4)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (1.3.2)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (1.13.1)\n",
            "Requirement already satisfied: huggingface-hub>=0.15.1 in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (0.23.5)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.10/dist-packages (from sentence-transformers) (9.4.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.15.1->sentence-transformers) (3.15.4)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.15.1->sentence-transformers) (2024.6.1)\n",
            "Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.15.1->sentence-transformers) (24.1)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.15.1->sentence-transformers) (6.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.15.1->sentence-transformers) (2.32.3)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.15.1->sentence-transformers) (4.12.2)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (1.13.1)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (3.1.4)\n",
            "Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cuda-runtime-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cuda-cupti-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cudnn-cu12==8.9.2.26 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (8.9.2.26)\n",
            "Requirement already satisfied: nvidia-cublas-cu12==12.1.3.1 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (12.1.3.1)\n",
            "Requirement already satisfied: nvidia-cufft-cu12==11.0.2.54 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (11.0.2.54)\n",
            "Requirement already satisfied: nvidia-curand-cu12==10.3.2.106 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (10.3.2.106)\n",
            "Requirement already satisfied: nvidia-cusolver-cu12==11.4.5.107 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (11.4.5.107)\n",
            "Requirement already satisfied: nvidia-cusparse-cu12==12.1.0.106 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (12.1.0.106)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.20.5 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (2.20.5)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (12.1.105)\n",
            "Requirement already satisfied: triton==2.3.1 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers) (2.3.1)\n",
            "Requirement already satisfied: nvidia-nvjitlink-cu12 in /usr/local/lib/python3.10/dist-packages (from nvidia-cusolver-cu12==11.4.5.107->torch>=1.11.0->sentence-transformers) (12.6.20)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers<5.0.0,>=4.34.0->sentence-transformers) (2024.5.15)\n",
            "Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from transformers<5.0.0,>=4.34.0->sentence-transformers) (0.4.4)\n",
            "Requirement already satisfied: tokenizers<0.20,>=0.19 in /usr/local/lib/python3.10/dist-packages (from transformers<5.0.0,>=4.34.0->sentence-transformers) (0.19.1)\n",
            "Requirement already satisfied: joblib>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from scikit-learn->sentence-transformers) (1.4.2)\n",
            "Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn->sentence-transformers) (3.5.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch>=1.11.0->sentence-transformers) (2.1.5)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.15.1->sentence-transformers) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.15.1->sentence-transformers) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.15.1->sentence-transformers) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.15.1->sentence-transformers) (2024.7.4)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch>=1.11.0->sentence-transformers) (1.3.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install -U langchain-huggingface"
      ],
      "metadata": {
        "id": "c53kzdT2icaY",
        "outputId": "64684c99-a28b-4109-fa06-8494399d9dc2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain-huggingface in /usr/local/lib/python3.10/dist-packages (0.0.3)\n",
            "Requirement already satisfied: huggingface-hub>=0.23.0 in /usr/local/lib/python3.10/dist-packages (from langchain-huggingface) (0.23.5)\n",
            "Requirement already satisfied: langchain-core<0.3,>=0.1.52 in /usr/local/lib/python3.10/dist-packages (from langchain-huggingface) (0.2.32)\n",
            "Requirement already satisfied: sentence-transformers>=2.6.0 in /usr/local/lib/python3.10/dist-packages (from langchain-huggingface) (3.0.1)\n",
            "Requirement already satisfied: tokenizers>=0.19.1 in /usr/local/lib/python3.10/dist-packages (from langchain-huggingface) (0.19.1)\n",
            "Requirement already satisfied: transformers>=4.39.0 in /usr/local/lib/python3.10/dist-packages (from langchain-huggingface) (4.42.4)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (3.15.4)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (2024.6.1)\n",
            "Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (24.1)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (6.0.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (2.32.3)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (4.66.5)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.23.0->langchain-huggingface) (4.12.2)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3,>=0.1.52->langchain-huggingface) (1.33)\n",
            "Requirement already satisfied: langsmith<0.2.0,>=0.1.75 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3,>=0.1.52->langchain-huggingface) (0.1.99)\n",
            "Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3,>=0.1.52->langchain-huggingface) (2.8.2)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3,>=0.1.52->langchain-huggingface) (8.5.0)\n",
            "Requirement already satisfied: torch>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=2.6.0->langchain-huggingface) (2.3.1+cu121)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=2.6.0->langchain-huggingface) (1.26.4)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=2.6.0->langchain-huggingface) (1.3.2)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=2.6.0->langchain-huggingface) (1.13.1)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=2.6.0->langchain-huggingface) (9.4.0)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers>=4.39.0->langchain-huggingface) (2024.5.15)\n",
            "Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from transformers>=4.39.0->langchain-huggingface) (0.4.4)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.3,>=0.1.52->langchain-huggingface) (3.0.0)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.75->langchain-core<0.3,>=0.1.52->langchain-huggingface) (3.10.7)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain-core<0.3,>=0.1.52->langchain-huggingface) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.20.1 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain-core<0.3,>=0.1.52->langchain-huggingface) (2.20.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.23.0->langchain-huggingface) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.23.0->langchain-huggingface) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.23.0->langchain-huggingface) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.23.0->langchain-huggingface) (2024.7.4)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (1.13.1)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (3.1.4)\n",
            "Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cuda-runtime-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cuda-cupti-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.1.105)\n",
            "Requirement already satisfied: nvidia-cudnn-cu12==8.9.2.26 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (8.9.2.26)\n",
            "Requirement already satisfied: nvidia-cublas-cu12==12.1.3.1 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.1.3.1)\n",
            "Requirement already satisfied: nvidia-cufft-cu12==11.0.2.54 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (11.0.2.54)\n",
            "Requirement already satisfied: nvidia-curand-cu12==10.3.2.106 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (10.3.2.106)\n",
            "Requirement already satisfied: nvidia-cusolver-cu12==11.4.5.107 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (11.4.5.107)\n",
            "Requirement already satisfied: nvidia-cusparse-cu12==12.1.0.106 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.1.0.106)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.20.5 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (2.20.5)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.1.105 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.1.105)\n",
            "Requirement already satisfied: triton==2.3.1 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (2.3.1)\n",
            "Requirement already satisfied: nvidia-nvjitlink-cu12 in /usr/local/lib/python3.10/dist-packages (from nvidia-cusolver-cu12==11.4.5.107->torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (12.6.20)\n",
            "Requirement already satisfied: joblib>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from scikit-learn->sentence-transformers>=2.6.0->langchain-huggingface) (1.4.2)\n",
            "Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn->sentence-transformers>=2.6.0->langchain-huggingface) (3.5.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (2.1.5)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch>=1.11.0->sentence-transformers>=2.6.0->langchain-huggingface) (1.3.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install langchain_community"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kTM4OVqEc3Tf",
        "outputId": "bfb78a9d-4a13-47e5-c47c-3f5b8d1e6a47"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain_community\n",
            "  Downloading langchain_community-0.2.12-py3-none-any.whl.metadata (2.7 kB)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (6.0.2)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (2.0.32)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (3.10.2)\n",
            "Collecting dataclasses-json<0.7,>=0.5.7 (from langchain_community)\n",
            "  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)\n",
            "Requirement already satisfied: langchain<0.3.0,>=0.2.13 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (0.2.14)\n",
            "Requirement already satisfied: langchain-core<0.3.0,>=0.2.30 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (0.2.32)\n",
            "Requirement already satisfied: langsmith<0.2.0,>=0.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (0.1.99)\n",
            "Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (1.26.4)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (2.32.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (8.5.0)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (2.3.5)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (24.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (6.0.5)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.9.4)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (4.0.3)\n",
            "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading marshmallow-3.21.3-py3-none-any.whl.metadata (7.1 kB)\n",
            "Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: langchain-text-splitters<0.3.0,>=0.2.0 in /usr/local/lib/python3.10/dist-packages (from langchain<0.3.0,>=0.2.13->langchain_community) (0.2.2)\n",
            "Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain<0.3.0,>=0.2.13->langchain_community) (2.8.2)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3.0,>=0.2.30->langchain_community) (1.33)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3.0,>=0.2.30->langchain_community) (24.1)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.3.0,>=0.2.30->langchain_community) (4.12.2)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.0->langchain_community) (3.10.7)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (2024.7.4)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain_community) (3.0.3)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.3.0,>=0.2.30->langchain_community) (3.0.0)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain<0.3.0,>=0.2.13->langchain_community) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.20.1 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain<0.3.0,>=0.2.13->langchain_community) (2.20.1)\n",
            "Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)\n",
            "Downloading langchain_community-0.2.12-py3-none-any.whl (2.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.3/2.3 MB\u001b[0m \u001b[31m22.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)\n",
            "Downloading marshmallow-3.21.3-py3-none-any.whl (49 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.2/49.2 kB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
            "Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)\n",
            "Installing collected packages: mypy-extensions, marshmallow, typing-inspect, dataclasses-json, langchain_community\n",
            "Successfully installed dataclasses-json-0.6.7 langchain_community-0.2.12 marshmallow-3.21.3 mypy-extensions-1.0.0 typing-inspect-0.9.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "from dotenv import load_dotenv\n",
        "from PyPDF2 import PdfReader\n",
        "from langchain.text_splitter import CharacterTextSplitter\n",
        "from langchain_community.embeddings import HuggingFaceInstructEmbeddings\n",
        "from langchain.vectorstores import FAISS\n",
        "from langchain.chat_models import ChatOpenAI\n",
        "from langchain.memory import ConversationBufferMemory\n",
        "from langchain.chains import (create_history_aware_retriever, create_retrieval_chain)\n",
        "from langchain_huggingface import HuggingFaceEndpoint\n",
        "from sentence_transformers import SentenceTransformer\n",
        "import numpy as np\n",
        "from faiss import IndexFlatL2\n",
        "from langchain.prompts import PromptTemplate"
      ],
      "metadata": {
        "id": "e7wvEfMBVcrL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def get_pdf_text(pdf_path):\n",
        "    pdf_reader = PdfReader(pdf_path)\n",
        "    text = \"\"\n",
        "    for page in pdf_reader.pages:\n",
        "        text += page.extract_text() or \"\"\n",
        "    return text\n"
      ],
      "metadata": {
        "id": "vXJ7rR2mVg4e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_text_chunks(text):\n",
        "    text_splitter = CharacterTextSplitter(\n",
        "        separator=\"\\n\",\n",
        "        chunk_size=1000,\n",
        "        chunk_overlap=200,\n",
        "        length_function=len\n",
        "    )\n",
        "    chunks = text_splitter.split_text(text)\n",
        "    print(chunks)\n",
        "    return chunks\n"
      ],
      "metadata": {
        "id": "zXRGJZ-8VqDQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def get_vectorstore(text_chunks):\n",
        "    # embeddings = OpenAIEmbeddings()\n",
        "    embeddings = HuggingFaceInstructEmbeddings(model_name=\"hkunlp/instructor-xl\")\n",
        "    print(embeddings)\n",
        "    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)\n",
        "    print(vectorstore)\n",
        "    return vectorstore"
      ],
      "metadata": {
        "id": "jT2lIVhKVsDG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def save_vectorstore(vectorstore, filename):\n",
        "    with open(filename, 'wb') as f:\n",
        "        pickle.dump(vectorstore, f)"
      ],
      "metadata": {
        "id": "X5xwQU-zeE9Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_conversation_chain(vectorstore):\n",
        "    # Create a standard retriever from the vectorstore\n",
        "    retriever = vectorstore.as_retriever()\n",
        "\n",
        "    # Define a prompt template that the retriever will use\n",
        "    prompt_template = \"\"\"\n",
        "    The following is a conversation between a user and an AI assistant. The assistant provides accurate, factual information and answers to the user's questions based on the context provided by the user.\n",
        "\n",
        "    User: {input}\n",
        "    Assistant:\n",
        "    \"\"\"\n",
        "\n",
        "    prompt = PromptTemplate(input_variables=[\"input\"], template=prompt_template)\n",
        "\n",
        "    # Set up the language model\n",
        "    # llm = HuggingFaceEndpoint(repo_id=\"google/flan-t5-xxl\",\n",
        "    #                      model_kwargs={\"temperature\": 0.5, \"max_length\": 512},\n",
        "    #                      huggingfacehub_api_token='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')\n",
        "    llm = HuggingFaceEndpoint(\n",
        "    repo_id=\"google/flan-t5-xxl\", max_length=128, temperature=0.5, token=\"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\"\n",
        ")\n",
        "\n",
        "    # Create a history-aware retriever\n",
        "    history_aware_retriever = create_history_aware_retriever(\n",
        "        llm=HuggingFaceEndpoint,\n",
        "        retriever=retriever,\n",
        "        prompt=prompt\n",
        "    )\n",
        "\n",
        "    # Set up memory\n",
        "    memory = ConversationBufferMemory(\n",
        "        memory_key='chat_history', return_messages=True\n",
        "    )\n",
        "\n",
        "    # Create the retrieval chain\n",
        "    conversation_chain = create_retrieval_chain(\n",
        "        retriever=retriever,\n",
        "        combine_docs_chain=history_aware_retriever\n",
        "    )\n",
        "    return conversation_chain\n"
      ],
      "metadata": {
        "id": "0DWK69OSVtUo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def handle_userinput(conversation_chain, user_question):\n",
        "    response = conversation_chain.invoke({'input': user_question})\n",
        "    return response\n"
      ],
      "metadata": {
        "id": "lFfn7fsEV1Zj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    # Load the PDF and extract the text\n",
        "    raw_text = get_pdf_text('testing.pdf')\n",
        "\n",
        "    # Split the text into chunks\n",
        "    text_chunks = get_text_chunks(raw_text)\n",
        "\n",
        "    # Create the vector store from the text chunks\n",
        "    vectorstore = get_vectorstore(text_chunks)\n",
        "    print(\"Vector store created.\")\n",
        "\n",
        "    # Create the conversation chain with the vector store\n",
        "    conversation_chain = get_conversation_chain(vectorstore)\n",
        "    print(\"Conversation chain created.\")\n",
        "\n",
        "    # Simulate a user input and get the response\n",
        "    user_question = \"Who is Paras?\"\n",
        "    response = handle_userinput(conversation_chain, user_question)\n",
        "\n",
        "    # Print the response\n",
        "    print(\"Response:\", response)\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B02HJ4NzV36A",
        "outputId": "cd4c5a4d-dcf9-4a9f-fed9-612db788ba20"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Hello\\nmy\\nname\\nis\\nparas\\nlohia\\ni\\nam\\na\\nsoftware\\ndeveloper']\n",
            "load INSTRUCTOR_Transformer\n",
            "max_seq_length  512\n",
            "client=INSTRUCTOR(\n",
            "  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: T5EncoderModel \n",
            "  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False})\n",
            "  (2): Dense({'in_features': 1024, 'out_features': 768, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity'})\n",
            "  (3): Normalize()\n",
            ") model_name='hkunlp/instructor-xl' cache_folder=None model_kwargs={} encode_kwargs={} embed_instruction='Represent the document for retrieval: ' query_instruction='Represent the question for retrieving supporting documents: ' show_progress=False\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:langchain_huggingface.llms.huggingface_endpoint:WARNING! max_length is not default parameter.\n",
            "                    max_length was transferred to model_kwargs.\n",
            "                    Please make sure that max_length is what you intended.\n",
            "WARNING:langchain_huggingface.llms.huggingface_endpoint:WARNING! token is not default parameter.\n",
            "                    token was transferred to model_kwargs.\n",
            "                    Please make sure that token is what you intended.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<langchain_community.vectorstores.faiss.FAISS object at 0x7fdfd95503d0>\n",
            "Vector store created.\n",
            "Conversation chain created.\n",
            "Response: {'input': 'Who is Paras?', 'context': [Document(page_content='Hello\\nmy\\nname\\nis\\nparas\\nlohia\\ni\\nam\\na\\nsoftware\\ndeveloper')], 'answer': [Document(page_content='Hello\\nmy\\nname\\nis\\nparas\\nlohia\\ni\\nam\\na\\nsoftware\\ndeveloper')]}\n"
          ]
        }
      ]
    }
  ]
}