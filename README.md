# prereg

This repository has the code for auto-adding course and stuff on <https://prereg1.iium.edu.my/>.

## Setup and Run

Download the required libraries.

```shell
$ cd prereg
$ pip install -r requirements.txt
```

Make a `.env` file containing your username and password.

```shell
USER = your username
PASS = your password
```

Then replace the `add_course()` line in `main.py` with the course you want to add. The first and second variable is `course_code` and `section` respectively.

```python
prereg.add_course('MATH 2330', '3')
```

Run

```shell
$ python main.py
```

If there is any error, try to download a different version of `msedgedriver.exe` at [Microsoft Edge Webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/). Make sure the version is the same as your Edge browser version.