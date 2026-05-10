---
name: content-optimization
description: Enhances content quality, readability, and SEO performance
tags: [content, seo, readability, engagement]
---

# Content Optimization Process

Follow these steps to optimize content for quality, readability, and SEO:

## 1. Load Optimization Guidelines

First, understand the optimization criteria:
- Load `reference.md` for complete optimization checklist
- Load `examples.md` to see before/after optimization examples

## 2. Analyze Current Content

Review the content across these dimensions:

### Structure Analysis
- Check heading hierarchy (H1 → H2 → H3)
- Verify paragraph lengths (3-5 sentences ideal)
- Assess use of lists and formatting
- Evaluate logical flow and organization

### Language Analysis
- Identify vocabulary complexity
- Check for passive voice usage
- Assess sentence clarity
- Verify tone consistency

### SEO Analysis
- Review keyword usage and density
- Check meta description potential
- Identify internal linking opportunities
- Assess header tag optimization

### Engagement Analysis
- Evaluate introduction hook strength
- Check for clear calls-to-action
- Assess use of examples and stories
- Verify conclusion effectiveness

## 3. Run Automated Analysis

Execute the content analyzer:
```bash
python scripts/analyze_content.py <content_file>
```

This will provide:
- Readability score (Flesch-Kincaid)
- Keyword density analysis
- Sentence length distribution
- Passive voice percentage

## 4. Apply Optimizations

Use the optimization template from `templates/optimization-report.md` to structure improvements:

### Priority 1: Critical Issues
- Fix broken structure
- Correct grammar/spelling
- Remove confusing sections

### Priority 2: Readability
- Simplify complex sentences
- Replace jargon with clear language
- Add transitions between sections
- Break up long paragraphs

### Priority 3: SEO
- Integrate target keywords naturally
- Optimize headings for search
- Add meta description
- Suggest internal links

### Priority 4: Engagement
- Strengthen introduction
- Add compelling examples
- Include clear CTAs
- Improve conclusion

## 5. Generate Optimization Report

Create a summary including:
- Before/after readability scores
- Key improvements made
- SEO enhancements applied
- Engagement optimizations
- Recommended next steps
