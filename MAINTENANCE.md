# Website Maintenance Guide

This guide explains how to maintain and update your personal academic website.

**Good news:** The website is designed to be **fully automated**! You only need to update data files - the website will automatically generate all navigation and indexing.

## 📚 Table of Contents

- [Adding New Publications](#adding-new-publications) ⭐ **FULLY AUTOMATED**
- [Adding New Blog Posts](#adding-new-blog-posts) ⭐ **FULLY AUTOMATED**
- [Adding Pipeline Images](#adding-pipeline-images)
- [File Structure](#file-structure)

---

## 📄 Adding New Publications ⭐ **FULLY AUTOMATED**

**You only need to update ONE file!** Everything else is automatic.

### Step 1: Add Pipeline Image

Place your publication's pipeline image in the `assets/img/publications/` directory:

```bash
# Example: For a paper called "MyPaper"
cp my-pipeline.png /data3/peirongcan/prongcan.github.io/assets/img/publications/mypaper.png
```

**Image Recommendations:**
- Format: PNG or JPG
- Size: 280px × 240px recommended
- Keep the aspect ratio readable

### Step 2: Update Publications Data File ✅ **ONLY THIS STEP IS NEEDED!**

Open `_data/publications.yml` and add your paper at the end:

```yaml
# Publications Data
# Add your papers here. The website will automatically render them.

- id: mypaper
  title: "My Paper Title: A Novel Approach"
  authors: "Rongcan Pei, Coauthor1, Coauthor2"
  status: "Under Review"
  arxiv: "https://arxiv.org/abs/XXXX.XXXXX"
  github: "https://github.com/yourusername/repo"
  image: "/assets/img/publications/mypaper.png"
  abstract: "A brief summary of your paper's key contributions and results. Keep it under 80 words."
```

**That's it!** The website will **automatically**:
- ✅ Display your paper on the homepage
- ✅ Add it to the sidebar navigation submenu
- ✅ Enable smooth scrolling to your paper
- ✅ Handle direct links like `/#mypaper`

**Field Descriptions:**
- `id`: Unique identifier (lowercase, no spaces) - used for URL anchor
- `title`: Full paper title
- `authors`: Author list (use HTML to highlight your name: `<span style='text-decoration: underline;'>R. Pei</span>*`)
- `status`: "Under Review", "Published", "Preprint", etc.
- `arxiv`: Optional arXiv link (will show arXiv icon if provided)
- `github`: Optional GitHub link (will show GitHub icon if provided)
- `github_label`: Optional custom label for GitHub link (defaults to "Code")
- `image`: Path to pipeline image
- `abstract`: Short summary (60-80 words recommended)

---

## 📝 Adding New Blog Posts ⭐ **FULLY AUTOMATED**

### Step 1: Create Blog Post File

Create a new Markdown file in the `_posts/` directory with the format: `YYYY-MM-DD-title.md`

```bash
# Example: Creating a blog post for February 12, 2026
touch /data3/peirongcan/prongcan.github.io/_posts/2026-02-12-my-new-post.md
```

### Step 2: Add Front Matter and Content

Edit the file with your blog content:

```markdown
---
title: Your Blog Post Title
date: 2026-02-12 14:30:00 +0800
description: A brief description of your post
categories: [Research, Life]  # Optional categories
pin: true  # Set to true if you want to pin this post
---

Your blog content goes here in Markdown format.

## Subheading

More content...
```

**Required Fields:**
- `title`: Post title
- `date`: Publication date (use your timezone)
- `description`: Short description shown in the blog list

**Optional Fields:**
- `categories`: Array of categories
- `pin`: Set to `true` to pin important posts
- `tags`: Array of tags for organization

**That's it!** The website will **automatically**:
- ✅ Display your post on the homepage
- ✅ Add it to the sidebar navigation submenu
- ✅ Enable smooth scrolling to your post
- ✅ Number them correctly (blog-1, blog-2, etc.)

### Changing Number of Blog Posts Displayed

To change how many blog posts appear on the homepage, edit `index.html`:

```liquid
{% assign posts = site.posts | limit: 3 %}
```

Change `3` to your desired number.

---

## 🖼️ Adding Pipeline Images

When adding pipeline images for publications:

### Directory Structure

```
assets/img/publications/
├── VERA.png
├── instructor.png
└── yourpaper.png  # Add new images here
```

### Best Practices

1. **File Naming:**
   - Use lowercase, no spaces
   - Use descriptive names (e.g., `mypaper.png`)

2. **Image Optimization:**
   - Compress images for web (keep under 200KB if possible)
   - Use PNG for diagrams with text
   - Use JPG for photos

3. **Sizing:**
   - Display size: 280px × 240px
   - Original size can be larger (will be scaled with `object-fit: contain`)

---

## 📁 File Structure

```
prongcan.github.io/
├── index.html              # Main homepage (auto-generates from data)
├── _config.yml             # Site configuration
├── _data/                 # ⭐ DATA FILES - Update these!
│   └── publications.yml   # Add your papers here (auto-displayed)
├── _posts/                # Blog posts (Markdown files)
│   └── YYYY-MM-DD-title.md
├── _tabs/                 # Sidebar navigation tabs
│   ├── about.md
│   ├── research.md        # Redirects to /#research
│   └── blog.md           # Redirects to /#blog
├── assets/
│   └── img/
│       ├── avatar.jpg      # Your profile picture
│       └── publications/  # Publication pipeline images
│           ├── VERA.png
│           ├── instructor.png
│           └── ...
└── MAINTENANCE.md         # This file
```

---

## 🔧 Quick Reference

### Publication Entry Template (YAML)

```yaml
- id: unique-id
  title: "Full Paper Title"
  authors: "Author1, Author2, Author3"
  status: "Under Review"
  arxiv: "https://arxiv.org/abs/XXXX.XXXXX"
  github: "https://github.com/username/repo"
  github_label: "Code & Prompts"
  image: "/assets/img/publications/filename.png"
  abstract: "Summary in 60-80 words."
```

### Blog Post Template (Markdown)

```markdown
---
title: Post Title
date: YYYY-MM-DD HH:MM:SS +0800
description: Description
categories: [Category1, Category2]
---

Content in Markdown...
```

---

## ⚡ What Happens Automatically?

You don't need to worry about:

❌ **NOT NEEDED:**
- Manual HTML updates
- JavaScript array modifications
- Navigation menu updates
- ID assignment
- Click handler updates
- CSS styling

✅ **AUTOMATIC:**
- Papers appear on homepage (from `_data/publications.yml`)
- Sidebar navigation updates (reads from page)
- Smooth scrolling (works for any ID)
- Blog listing (from `_posts/` directory)
- Responsive design
- URL routing and anchors

---

## ✅ Testing Changes

1. **Local Preview:**
   ```bash
   bundle exec jekyll serve
   ```
   Visit `http://localhost:4000` to preview changes.

2. **Deployment:**
   - Commit and push to GitHub
   - GitHub Actions will automatically build and deploy
   - Changes appear at `https://prongcan.github.io` within minutes

---

## 📞 Need Help?

If you encounter issues:

1. Check Jekyll documentation: https://jekyllrb.com/docs/
2. Check Chirpy theme docs: https://github.com/cotes2020/jekyll-theme-chirpy
3. Review this document's examples

---

**Last Updated:** 2026-02-12
