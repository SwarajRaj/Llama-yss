{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73acfad5-5c54-43be-8a50-69e44b3a65e7",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after 'if' statement on line 9 (1793384122.py, line 11)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 11\u001b[1;36m\u001b[0m\n\u001b[1;33m    st.code(\"Hello Hiring Manager, I am from Atliq\", language='markdown'\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after 'if' statement on line 9\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\" Cold Mail Generator\")\n",
    "\n",
    "url_input = st.text_input(\"Enter a URL:\", value=\"https://jobs.mercedes-benz.com/enUS/machine-learning-engineer-ai-products-140531-MER0003CK2\")\n",
    "\n",
    "submit_button = st.button(\"Submit\")\n",
    "\n",
    "if submit_button:\n",
    "\n",
    "st.code(\"Hello Hiring Manager, I am from Atliq\", language='markdown'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "95e2c0e3-a9ff-4e00-903f-81456e1a4a91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeableNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: streamlit in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (1.39.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (5.4.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (1.8.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (2.2.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (4.25.5)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (17.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (13.9.1)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (8.5.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<6,>=2.1.5 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (5.0.3)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: narwhals>=1.5.2 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from altair<6,>=4.0->streamlit) (1.9.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\seshu\\appdata\\roaming\\python\\python312\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da3deb34-7019-4a2e-97cc-ddf2474d5da6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
