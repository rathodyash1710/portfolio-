set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser - reliable method using heredoc
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
email = 'yash@example.com'
password = 'Yash@12345#'

if User.objects.filter(username=username).exists():
    print(f"Superuser '{username}' already exists")
else:
    user = User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created successfully")
EOF

echo "Build complete!"