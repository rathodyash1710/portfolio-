#!/usr/bin/env bash
# Exit on error
set -o errexit

# Step 1: Install Python packages
pip install -r requirements.txt

# Step 2: Collect static files (CSS, JS, images)
python manage.py collectstatic --no-input

# Step 3: Apply database migrations
python manage.py migrate
```

**What each step does:**

| Step | Purpose | Why? |
|------|---------|------|
| `pip install` | Install all Python libraries | Django, DRF, etc. needed to run |
| `collectstatic` | Gather all static files | CSS, JS, admin panel files |
| `migrate` | Setup database | Create tables for your models |

---

### For Frontend - It's Automatic!

When you run `npm run build`, Vite automatically:

**Before Build (Development):**
```
src/
├── App.jsx (50 KB)
├── index.css (10 KB)
├── components/ (many files)
└── assets/ (images, icons)
Total: ~500 files, 5 MB
```

**After Build (Production):**
```
dist/
├── index.html
├── assets/
│   ├── index-abc123.js (200 KB, minified)
│   └── index-def456.css (50 KB, minified)
Total: ~10 files, 500 KB
```

**Benefits:**
- ✅ **Faster loading** (minified, compressed)
- ✅ **Fewer files** (bundled together)
- ✅ **Optimized images** (compressed)
- ✅ **Browser compatible** (transpiled code)

---

## 🎨 Visual Example: Build Process

### Backend Build Flow:
```
GitHub Code
    ↓
[Render Server]
    ↓
Run build.sh
    ↓
├── Install Django ✅
├── Install libraries ✅
├── Collect CSS/JS ✅
└── Setup database ✅
    ↓
Start gunicorn
    ↓
🌐 Live Backend!
```

### Frontend Build Flow:
```
GitHub Code
    ↓
[Render Server]
    ↓
npm install
    ↓
npm run build
    ↓
├── Minify JavaScript ✅
├── Optimize CSS ✅
├── Compress images ✅
└── Bundle everything ✅
    ↓
Serve from 'dist' folder
    ↓
🌐 Live Website!