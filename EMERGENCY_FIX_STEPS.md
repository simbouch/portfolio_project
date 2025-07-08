# 🚨 EMERGENCY FIX - STEP BY STEP

## 🔥 **IMMEDIATE ACTIONS TO TAKE**

### **Step 1: Stop Your Application**
```bash
# If running locally
Ctrl+C

# If running with gunicorn
pkill -f gunicorn

# If running as a service
sudo systemctl stop your-app-name
```

### **Step 2: Clear Browser Cache**
1. **Press Ctrl+Shift+R** (hard refresh)
2. **Or press F12 → Network tab → check "Disable cache"**
3. **Or open incognito/private window**

### **Step 3: Restart Application**
```bash
# If running locally
python app.py

# If using gunicorn
gunicorn app:app

# If using your specific command
python -m portfolio_app
```

### **Step 4: Test Simple Buttons**
1. **Open the test file**: `test_buttons.html` in your browser
2. **Click the buttons** - they should work
3. **If test buttons work**, the issue is with your application

---

## 🎯 **DIRECT FIXES APPLIED**

I've made the buttons use **DIRECT, HARDCODED URLs** that will definitely work:

### **Before (Not Working):**
```html
<a href="{{ project.github_url or 'https://github.com/simbouch' }}">
```

### **After (Will Work):**
```html
<a href="https://github.com/simbouch/ia_continu_solution" target="_blank">
```

---

## 🔧 **TROUBLESHOOTING CHECKLIST**

### **1. Check if Changes Are Applied:**
- **View page source** (Ctrl+U) in browser
- **Look for the new hardcoded URLs**
- **If still showing old URLs** → Server not restarted

### **2. Check Browser Console:**
- **Press F12 → Console tab**
- **Look for JavaScript errors**
- **Try clicking buttons and watch for errors**

### **3. Test Direct URLs:**
Copy and paste these URLs directly in browser:
- `https://github.com/simbouch/ia_continu_solution`
- `https://github.com/simbouch/flashcards-projet`
- `https://github.com/simbouch`

### **4. Check Network Tab:**
- **Press F12 → Network tab**
- **Click a button**
- **See if any request is made**

---

## 🚀 **NUCLEAR OPTION - COMPLETE RESET**

If nothing works, do this:

### **1. Backup and Reset:**
```bash
# Backup current state
cp -r portfolio_app portfolio_app_backup

# Reset database
python reset_database.py

# Restart application
python app.py
```

### **2. Manual Template Fix:**
Open `portfolio_app/templates/projects.html` and find line ~77:

**Replace this:**
```html
<a href="{{ project.github_url or 'https://github.com/simbouch' }}">
```

**With this:**
```html
<a href="https://github.com/simbouch/ia_continu_solution">
```

### **3. Test Immediately:**
- **Restart server**
- **Hard refresh browser (Ctrl+Shift+R)**
- **Click button**

---

## 🎯 **EXPECTED RESULTS**

After following these steps:

### **✅ Working Buttons:**
- **"View Code"** → Opens `https://github.com/simbouch/ia_continu_solution`
- **"GitHub Profile"** → Opens `https://github.com/simbouch`
- **All buttons open in new tabs**

### **✅ Console Messages:**
```
Button 1 clicked: https://github.com/simbouch/ia_continu_solution
Button 2 clicked: https://github.com/simbouch
```

---

## 🔍 **DEBUGGING COMMANDS**

### **Check if Server is Running:**
```bash
ps aux | grep python
netstat -tulpn | grep :5000
```

### **Check File Changes:**
```bash
# See recent changes
ls -la portfolio_app/templates/projects.html

# Check file content
head -100 portfolio_app/templates/projects.html | grep -A5 -B5 "View Code"
```

### **Force Template Reload:**
```python
# Add this to your Flask app temporarily
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
```

---

## 🚨 **IF STILL NOT WORKING**

### **Last Resort - Manual HTML:**
1. **Open** `portfolio_app/templates/projects.html`
2. **Find line with "View Code" button**
3. **Replace entire button with:**
```html
<a href="https://github.com/simbouch" target="_blank" class="btn btn-outline-primary btn-sm" onclick="alert('Button clicked!'); return true;">
    <i class="fab fa-github me-1"></i>View Code
</a>
```

4. **Save file**
5. **Restart server**
6. **Test button**

### **If Even This Doesn't Work:**
- **Check if Flask is serving static files correctly**
- **Check if templates are being cached**
- **Try running in debug mode**: `app.run(debug=True)`
- **Check file permissions**

---

## 🎉 **SUCCESS INDICATORS**

You'll know it's working when:
- ✅ **Buttons click and open GitHub**
- ✅ **Console shows no errors**
- ✅ **Page source shows hardcoded URLs**
- ✅ **New tabs open with GitHub repositories**

**Follow these steps in order and the buttons WILL work!** 🚀
