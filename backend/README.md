1. Create a virtual environment
2. Activate the virtual environment
3. Install the requirements
```console
pip install -r requirements.txt
```
4. Make the migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Create a superuser
```bash
python manage.py createsuperuser
```