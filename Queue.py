{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNzo7Xluf7eaZJ90wy9M4qN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/deekshitha799/DDS/blob/main/Queue.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MWICW6GhjvW5",
        "outputId": "bf02cb86-3add-48f1-ed34-1e72d2e5f549"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting lab5_queue.cpp\n"
          ]
        }
      ],
      "source": [
        "%%writefile lab5_queue.cpp\n",
        "#include<iostream>\n",
        "#define SIZE 5\n",
        "using namespace std;\n",
        "\n",
        "class Queue {\n",
        "  int arr[SIZE] , front, rear;\n",
        "public:\n",
        "  Queue() {\n",
        "    front = rear = -1;\n",
        "  }\n",
        "  void enqueue(int val) {\n",
        "    if((rear + 1) % SIZE == front) {\n",
        "      cout << \"Queue Overflow\\n\";\n",
        "      return;\n",
        "    }\n",
        "    if(front == -1) front = 0;\n",
        "    rear = (rear + 1) % SIZE;\n",
        "    arr[rear] = val;\n",
        "  }\n",
        "\n",
        "  void dequeue() {\n",
        "    if(front == -1) {\n",
        "      cout << \"Queue underflow\\n\";\n",
        "      return;\n",
        "    }\n",
        "    cout << \"dequeued:\" << arr[front] << endl;\n",
        "    if(front == rear)\n",
        "      front = rear = -1;\n",
        "    else\n",
        "      front = (front + 1) % SIZE;\n",
        "  }\n",
        "\n",
        "  void traverse() {\n",
        "    if (front == -1) {\n",
        "      cout << \"Queue is empty\\n\";\n",
        "      return;\n",
        "    }\n",
        "    cout << \"Queue:\";\n",
        "    int i = front;\n",
        "    while (true) {\n",
        "      cout << arr[i] << \" \";\n",
        "      if(i == rear) break;\n",
        "      i = (i + 1) % SIZE;\n",
        "    }\n",
        "    cout << endl;\n",
        "  }\n",
        "\n",
        "  void search(int key) {\n",
        "    if(front == -1) {\n",
        "      cout << \"Queue is empty\\n\";\n",
        "      return;\n",
        "    }\n",
        "    int i = front;\n",
        "    while (true) {\n",
        "      if(arr[i] == key) {\n",
        "        cout << \"Element \" << key << \"found at index\" << i << endl;\n",
        "        return;\n",
        "      }\n",
        "      if(i == rear) break;\n",
        "      i = (i + 1) % SIZE;\n",
        "    }\n",
        "    cout << \"element not found\\n\";\n",
        "  }\n",
        "};\n",
        "\n",
        "int main() {\n",
        "  Queue q;\n",
        "  q.enqueue(10);\n",
        "  q.enqueue(20);\n",
        "  q.enqueue(30);\n",
        "  q.traverse();\n",
        "  q.dequeue();\n",
        "  q.traverse();\n",
        "  q.search(20);\n",
        "  q.search(99);\n",
        "  return 0;\n",
        "}\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!g++ lab5_queue.cpp -o lab5"
      ],
      "metadata": {
        "id": "cbG0xbKSqZaQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!./lab5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "naHRpXL-q6_o",
        "outputId": "0e8d60c5-2505-4335-914d-c3dde875402e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Queue:10 20 30 \n",
            "dequeued:10\n",
            "Queue:20 30 \n",
            "Element 20found at index1\n",
            "element not found\n"
          ]
        }
      ]
    }
  ]
}