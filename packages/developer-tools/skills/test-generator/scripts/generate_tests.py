#!/usr/bin/env python3
"""
Test generator script
Generates test boilerplate for different testing frameworks
"""

import sys
import re
from pathlib import Path

PYTEST_TEMPLATE = '''"""
Tests for {module_name}
"""

import pytest
from {module_path} import {function_name}


class Test{class_name}:
    """Test suite for {function_name}"""
    
    def test_{function_name}_happy_path(self):
        """Test {function_name} with valid inputs"""
        # Arrange
        # TODO: Set up test data
        
        # Act
        # TODO: Call the function
        
        # Assert
        # TODO: Verify expected outcome
        pass
    
    def test_{function_name}_edge_cases(self):
        """Test {function_name} with edge case inputs"""
        # TODO: Test boundary values
        pass
    
    def test_{function_name}_error_handling(self):
        """Test {function_name} error handling"""
        # TODO: Test invalid inputs
        pass
'''

JEST_TEMPLATE = '''/**
 * Tests for {module_name}
 */

import {{ {function_name} }} from './{module_path}';

describe('{function_name}', () => {{
  it('should handle valid inputs correctly', () => {{
    // Arrange
    // TODO: Set up test data
    
    // Act
    // TODO: Call the function
    
    // Assert
    // TODO: Verify expected outcome
  }});
  
  it('should handle edge cases', () => {{
    // TODO: Test boundary values
  }});
  
  it('should handle errors appropriately', () => {{
    // TODO: Test error conditions
  }});
}});
'''

def generate_test(source_file, framework='pytest'):
    """Generate test boilerplate for a source file"""
    
    source_path = Path(source_file)
    if not source_path.exists():
        print(f"Error: File {source_file} not found")
        return
    
    module_name = source_path.stem
    function_name = module_name  # Simplified - could parse actual functions
    class_name = ''.join(word.capitalize() for word in module_name.split('_'))
    
    if framework == 'pytest':
        template = PYTEST_TEMPLATE
        test_file = f"test_{module_name}.py"
    elif framework == 'jest':
        template = JEST_TEMPLATE
        test_file = f"{module_name}.test.js"
    else:
        print(f"Unsupported framework: {framework}")
        return
    
    test_content = template.format(
        module_name=module_name,
        module_path=module_name,
        function_name=function_name,
        class_name=class_name
    )
    
    print(f"\n{'='*60}")
    print(f"Generated Test File: {test_file}")
    print(f"{'='*60}\n")
    print(test_content)
    print(f"\n{'='*60}")
    print(f"Copy the above content to: tests/{test_file}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_tests.py <source_file> [framework]")
        print("Frameworks: pytest (default), jest")
        sys.exit(1)
    
    framework = sys.argv[2] if len(sys.argv) > 2 else 'pytest'
    generate_test(sys.argv[1], framework)
