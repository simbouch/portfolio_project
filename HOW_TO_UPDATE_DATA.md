# 🔄 How to Update Portfolio Data

## 🚨 **IMPORTANT: Why Your Changes Aren't Showing**

The reason you're not seeing the updated projects and experience is because the database still contains the old sample data. The new data I created is in the code, but it only gets loaded when the database is empty.

## 🛠️ **3 Ways to Fix This:**

### **Method 1: Use the Reset Button (Easiest)**

1. **Run your portfolio application locally**
2. **Go to the About page** (`/about`)
3. **Scroll to the bottom** - you'll see a "Development Tools" section
4. **Click "Reset Portfolio Data"** button
5. **Confirm the reset**
6. **Check your projects and experience pages** - they should now show the updated data!

### **Method 2: Run the Reset Script**

1. **Open terminal in your project directory**
2. **Run the reset script:**
   ```bash
   python reset_database.py
   ```
3. **This will:**
   - Drop all existing data
   - Create fresh tables
   - Load the new sample data with correct GitHub links and experience

### **Method 3: Delete the Database File (Nuclear Option)**

1. **Stop your application**
2. **Find and delete the database file** (usually `instance/portfolio.db` or similar)
3. **Restart your application**
4. **The app will create a new database with the updated data**

## ✅ **What Will Be Updated:**

### **Projects:**
- ✅ All GitHub links will be correct
- ✅ Project descriptions will match actual repositories
- ✅ New projects added (OCR collection, web scraping, classification)
- ✅ Accurate technology stacks

### **Experience:**
- ✅ Current position: AI Developer/Engineer at CHRU de Nancy
- ✅ AI Developer Training at Microsoft AI School by Simplon
- ✅ All job titles, companies, and dates from your CV
- ✅ Comprehensive forensic science background

### **Skills:**
- ✅ Added missing programming languages (R, Java, PHP)
- ✅ Data visualization tools (Power BI, Tableau, Matplotlib, Seaborn)
- ✅ Big data & ETL tools (PySpark, Talend, Alteryx)
- ✅ Cloud services (Azure ML, Microsoft Dataverse)
- ✅ Data collection tools (Scrapy, BeautifulSoup, API Development)

## 🎯 **After Reset:**

1. **Check Projects page** - all GitHub links should work correctly
2. **Check Experience page** - should show your current AI Developer role
3. **Check Skills page** - should include all technologies from your CV
4. **Verify GitHub links** - click on project links to ensure they go to the right repositories

## 🚀 **For Deployment:**

After you've verified everything works locally:

1. **Commit all changes:**
   ```bash
   git add .
   git commit -m "🔧 Complete portfolio overhaul: Fix all GitHub links, update experience & skills based on CV"
   git push origin main
   ```

2. **Deploy to Render** - the new initialization logic will automatically load the updated data

## 🆘 **If You Still Have Issues:**

1. **Check the browser console** for any JavaScript errors
2. **Check the application logs** for any database errors
3. **Try the reset button multiple times** if needed
4. **Clear your browser cache** and refresh

The updated data is definitely in the code now - it just needs to be loaded into the database! 🎉
