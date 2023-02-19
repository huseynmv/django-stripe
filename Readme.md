##### Prerequisites

- Python 3 installed on your system
- Stripe Public key and secret key

##### Step 1: Install the Required Libraries

To install the required libraries, run the following command in your terminal:

```python
pip install -r requirements.txt
```

##### Step 2: Create a .env File to Store the API Key and Secret Key

Create a .env file in the same directory as your Python program and add the following lines:

```python
STRIPE_PUBLIC_KEY=your_public_key
STRIPE_SECRET_KEY=your_secret_key
DEBUG=True
```

Replace your_public_key and your_secret_key with your actual API key and secret key, respectively.

##### Step 3: Run the Python Program

Save the Python file and run it using the following command in your terminal:

```python
python manage.py runserver
```
