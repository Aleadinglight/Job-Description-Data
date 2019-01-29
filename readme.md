# Data Scrapping With Python

Using Python script to scrap job's description data from Indeed.com

# Installation

1. Make sure Python 3 installed.

2. Install the necessary Python library:

```bash
pip install beautifulsoup4
pip install lxml
pip install pandas
```

Install the following library if there should be any errors

```bash
pip install xlsxwriter
pip install requests
```

# Using the script

1. Clone the project

```bash
git clone https://github.com/Aleadinglight/Job-Description-Data.git
```

2. Go to the `python` directory

```bash
cd python
```

3. Run the script in `main.py` with the link that you have

```bash
python main.py "www.blabla.com"
```

An example on how to get the link

<img src="../master/copylink.png"  width="300"/>

4. The result will be in `output.xlsx`
