# Python notes

## Mocking env variables in unit test
```python
k = mock.patch.dict(os.environ, {'IMAGE_BUCKET': 'xyz'})
k.start()
bucket = get_bucket('pre')
k.stop()
```