#!/usr/bin/env python3
"""
Content analyzer script
Analyzes content for readability, SEO, and engagement metrics
"""

import sys
import re
from pathlib import Path

def count_syllables(word):
    """Estimate syllable count for a word"""
    word = word.lower()
    vowels = 'aeiouy'
    syllable_count = 0
    previous_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel
    
    if word.endswith('e'):
        syllable_count -= 1
    if syllable_count == 0:
        syllable_count = 1
        
    return syllable_count

def calculate_flesch_reading_ease(text):
    """Calculate Flesch Reading Ease score"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    words = re.findall(r'\b\w+\b', text)
    syllables = sum(count_syllables(word) for word in words)
    
    if not sentences or not words:
        return 0
    
    avg_sentence_length = len(words) / len(sentences)
    avg_syllables_per_word = syllables / len(words)
    
    score = 206.835 - 1.015 * avg_sentence_length - 84.6 * avg_syllables_per_word
    return round(score, 1)

def calculate_flesch_kincaid_grade(text):
    """Calculate Flesch-Kincaid Grade Level"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    words = re.findall(r'\b\w+\b', text)
    syllables = sum(count_syllables(word) for word in words)
    
    if not sentences or not words:
        return 0
    
    avg_sentence_length = len(words) / len(sentences)
    avg_syllables_per_word = syllables / len(words)
    
    grade = 0.39 * avg_sentence_length + 11.8 * avg_syllables_per_word - 15.59
    return round(grade, 1)

def analyze_passive_voice(text):
    """Detect passive voice usage"""
    # Simple passive voice detection (to be + past participle)
    passive_patterns = [
        r'\b(is|are|was|were|be|been|being)\s+\w+ed\b',
        r'\b(is|are|was|were|be|been|being)\s+\w+en\b'
    ]
    
    passive_count = 0
    for pattern in passive_patterns:
        passive_count += len(re.findall(pattern, text, re.IGNORECASE))
    
    sentences = len(re.split(r'[.!?]+', text))
    passive_percentage = (passive_count / sentences * 100) if sentences > 0 else 0
    
    return passive_count, round(passive_percentage, 1)

def analyze_keywords(text, target_keyword=None):
    """Analyze keyword usage"""
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    
    if not target_keyword:
        # Find most common words (excluding common words)
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        word_freq = {}
        for word in words:
            if word not in common_words and len(word) > 3:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        top_keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        return top_keywords
    else:
        keyword_count = text.lower().count(target_keyword.lower())
        keyword_density = (keyword_count / total_words * 100) if total_words > 0 else 0
        return keyword_count, round(keyword_density, 2)

def analyze_content(file_path):
    """Analyze content file"""
    
    try:
        content = Path(file_path).read_text()
        
        # Calculate metrics
        flesch_ease = calculate_flesch_reading_ease(content)
        flesch_grade = calculate_flesch_kincaid_grade(content)
        passive_count, passive_pct = analyze_passive_voice(content)
        
        # Count basic stats
        sentences = len(re.split(r'[.!?]+', content))
        words = len(re.findall(r'\b\w+\b', content))
        paragraphs = len([p for p in content.split('\n\n') if p.strip()])
        
        avg_sentence_length = round(words / sentences, 1) if sentences > 0 else 0
        avg_paragraph_length = round(sentences / paragraphs, 1) if paragraphs > 0 else 0
        
        # Get top keywords
        top_keywords = analyze_keywords(content)
        
        # Print report
        print(f"\n{'='*60}")
        print(f"Content Analysis Report: {Path(file_path).name}")
        print(f"{'='*60}\n")
        
        print("📊 READABILITY METRICS")
        print(f"  Flesch Reading Ease: {flesch_ease}")
        if flesch_ease >= 60:
            print(f"    ✅ Good (Standard readability)")
        elif flesch_ease >= 30:
            print(f"    ⚠️  Difficult (Consider simplifying)")
        else:
            print(f"    ❌ Very Difficult (Needs simplification)")
        
        print(f"\n  Flesch-Kincaid Grade: {flesch_grade}")
        if 8 <= flesch_grade <= 10:
            print(f"    ✅ Target range (High school level)")
        elif flesch_grade < 8:
            print(f"    ℹ️  Below target (Very accessible)")
        else:
            print(f"    ⚠️  Above target (May be too complex)")
        
        print(f"\n📝 CONTENT STATISTICS")
        print(f"  Total Words: {words}")
        print(f"  Total Sentences: {sentences}")
        print(f"  Total Paragraphs: {paragraphs}")
        print(f"  Avg Sentence Length: {avg_sentence_length} words")
        print(f"  Avg Paragraph Length: {avg_paragraph_length} sentences")
        
        print(f"\n🎯 LANGUAGE ANALYSIS")
        print(f"  Passive Voice: {passive_count} instances ({passive_pct}%)")
        if passive_pct < 20:
            print(f"    ✅ Good (Active voice dominant)")
        else:
            print(f"    ⚠️  High (Consider more active voice)")
        
        print(f"\n🔍 TOP KEYWORDS")
        for keyword, count in top_keywords:
            density = round(count / words * 100, 2)
            print(f"  {keyword}: {count} times ({density}%)")
        
        print(f"\n{'='*60}")
        print("RECOMMENDATIONS")
        print(f"{'='*60}\n")
        
        recommendations = []
        
        if flesch_ease < 60:
            recommendations.append("• Simplify sentences for better readability")
        if flesch_grade > 10:
            recommendations.append("• Reduce complexity to high school level")
        if passive_pct > 20:
            recommendations.append("• Convert passive voice to active voice")
        if avg_sentence_length > 20:
            recommendations.append("• Break up long sentences (target: 15-20 words)")
        if avg_paragraph_length > 5:
            recommendations.append("• Shorten paragraphs (target: 3-5 sentences)")
        
        if recommendations:
            for rec in recommendations:
                print(rec)
        else:
            print("✅ Content meets all readability targets!")
        
        print(f"\n{'='*60}\n")
        
    except Exception as e:
        print(f"Error analyzing file: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_content.py <content_file>")
        sys.exit(1)
    
    exit_code = analyze_content(sys.argv[1])
    sys.exit(exit_code)
