# Python Notes

## Setting up Python
pyenv - https://github.com/pyenv/pyenv
```python
# Install pyenv using brew
$ brew install pyenv

# Install specific python version
$ pyenv install 3.9

# See installed versions
$ pyenv versions
* system (set by /Users/user/.pyenv/version)
  3.9.15

# Use wanted version
$ pyenv global 3.9

# Install desired packages
$ sudo pip install awscli awscli-local
```

---

## Using Python Virtual Environment
Link - https://docs.python.org/3/tutorial/venv.html

```python
# Create virtual environment
$ python3 -m venv venv-test

# Activate virtual environment
path $ source /venv-test/bin/activate
(venv-test) path $ # Environment is activated

# To exit vitrual environment
(venv-test) path $ deactivate 
```
---
## Python logging

- [Basic to Advanced Logging with Python](https://towardsdatascience.com/basic-to-advanced-logging-with-python-in-10-minutes-631501339650)

---
## Make python script executable
```
#!/usr/bin/env python
#!/usr/bin/env python3
```
---
## Hash file
```bash
openssl sha1 <file>
```

---

## Links
[Pigar](https://github.com/damnever/pigar)
[Pipreqs](https://github.com/bndr/pipreqs)

```bash
> pip install \
    --platform manylinux2014_x86_64 \
    --target=. \
    --implementation cp \
    --python 3.9 \
    --only-binary=:all: --upgrade \
    --force-reinstall
    pillow

> pip cache purge

> pip install ... --no-cache-dir

> pip install 'xkcdpass==1.2.5' --force-reinstall
```