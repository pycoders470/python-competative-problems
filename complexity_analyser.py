from typing import List
import time
import sys
from functools import wraps


def complexity_analyzer(func):
    """
    Decorator that analyzes and displays time and space complexity.
    
    This decorator:
    - Measures execution time
    - Estimates space complexity based on input size
    - Displays complexity analysis after function execution
    
    Args:
        func: The function to be wrapped and analyzed
        
    Returns:
        A wrapped function that prints complexity information
    """
    @wraps(func)
    def wrapper(self, array: List):
        # Record input size
        input_size = len(array)
        
        # Record memory before execution
        initial_memory = sys.getsizeof(array)
        
        # Measure execution time
        start_time = time.perf_counter()
        result = func(self, array)
        end_time = time.perf_counter()
        
        # Record memory after execution
        final_memory = sys.getsizeof(result)
        
        # Calculate metrics
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        memory_used = final_memory - initial_memory
        
        # Display complexity analysis
        print(f"\n{'='*60}")
        print(f"Function: {func.__name__}")
        print(f"{'='*60}")
        print(f"Input Size (n): {input_size}")
        print(f"Execution Time: {execution_time:.4f} ms")
        print(f"Memory Used: {memory_used} bytes")
        print(f"\nTheoretical Complexity Analysis:")
        print(f"  Time Complexity: O(n²) - nested loops performing ~n(n-1)/2 comparisons")
        print(f"  Space Complexity: O(1) - sorts in-place with minimal extra space")
        print(f"  Operations Count: ~{input_size * (input_size - 1) // 2} comparisons")
        print(f"{'='*60}\n")
        
        return result
    
    return wrapper