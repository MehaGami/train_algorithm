# Train Algorithm

A collection of educational algorithms in Python for practicing basic programming concepts.

## 📋 Requirements

- Python 3.6 or higher

## 🚀 Installation and Setup

### Step 1: Clone the repository (if needed)

```bash
git clone <repository-url>
cd train_algoritm
```

### Step 2: Create a virtual environment

```bash
python3 -m venv venv
```

### Step 3: Activate the virtual environment

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

After activation, you'll see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the program

```bash
python train_algorithm.py
```

### Deactivate the virtual environment

When you're done working:

```bash
deactivate
```

## 📝 Available Algorithms

1. **Even or Odd**

   - Input a number and determine if it's even or odd.
   - Example:
     - Input: `7`
     - Output: `Odd`

2. **Sum of Numbers from 1 to n**

   - Calculate the sum from 1 up to the given number `n`.
   - Example:
     - Input: `10`
     - Output: `55`

3. **Factorial**

   - Calculate the factorial of a given number.
   - Example:
     - Input: `5`
     - Output: `120`

4. **Reverse String**

   - Input a string and get its reverse.
   - Example:
     - Input: `hello`
     - Output: `olleh`

5. **Palindrome Check**

   - Check if the input string is a palindrome (ignores spaces and case).
   - Example:
     - Input: `Race car`
     - Output: `Palindrome`

6. **Average of Numbers in a List**

   - Calculate the arithmetic mean (average) of a list of numbers entered separated by commas or spaces.
   - Example:
     - Input: `1, 2, 3, 4, 5`
     - Output: `3.0`

7. **Find Maximum Number in a List**

   - Find the largest number in a list of numbers entered separated by commas or spaces.
   - Example:
     - Input: `1, 7, 3, 4, 5`
     - Output: `7`

8. **Count Occurrences of a Number in a List**

   - Count how many times a specific number appears in a list of numbers entered separated by commas or spaces.
   - Example:
     - Input numbers: `1, 2, 3, 2, 4, 2`
     - Input number to count: `2`
     - Output: `3`

9. **Get Even Numbers from a List**

   - Return all even numbers from a list entered separated by commas or spaces.
   - Example:
     - Input: `1, 2, 3, 4, 5, 6`
     - Output: `2, 4, 6`

10. **Get Unique Numbers from a List**

    - Return all unique numbers from a list entered separated by commas or spaces, preserving their order.
    - Example:
      - Input: `1, 2, 2, 3, 4, 3, 5`
      - Output: `1, 2, 3, 4, 5`

11. **NBU Currency Exchange Rates**

    - Fetch current exchange rates from the National Bank of Ukraine API for USD and EUR.
    - No input required - automatically displays current rates.
    - Example output:
      ```
      ┌─────────────────────────┐
      │ 💰 Currency: USD        │
      │ 💵 Exchange: 41.2215    │
      │ 📅 Date: 02.10.2025     │
      └─────────────────────────┘
      ```

12. **🎯 Two Sum (LeetCode #1)**

    - Classic LeetCode problem for algorithm practice.
    - Given an array of integers and a target sum, find the indices of two numbers that add up to the target.
    - Uses nested loops approach (Brute Force) with O(n²) time complexity.
    - Great for learning array manipulation and enumerate() function.
    - Example:
      - Input numbers: `2, 7, 11, 15`
      - Input target: `9`
      - Output: `0 1` (because nums[0] + nums[1] = 2 + 7 = 9)

## 💡 Usage

Run the script and choose an algorithm by name or number:

```bash
python train_algorithm.py
```

When prompted, enter one of the following:

- `one` or `1` for Even or Odd
- `two` or `2` for Sum of Numbers
- `three` or `3` for Factorial
- `four` or `4` for Reverse String
- `five` or `5` for Palindrome Check
- `six` or `6` for Average of Numbers in a List
- `seven` or `7` for Find Maximum Number in a List
- `eight` or `8` for Count Occurrences of a Number in a List
- `nine` or `9` for Get Even Numbers from a List
- `ten` or `10` for Get Unique Numbers from a List
- `eleven` or `11` for NBU Currency Exchange Rates
- `twelve` or `12` for Two Sum (LeetCode #1)

## 📖 Examples

### Example 1: Palindrome Check

```bash
$ python train_algorithm.py
Write algorithm number(one, two, three ... etc): five
Write string: Race car
Palindrome
```

### Example 2: NBU Currency Rates

```bash
$ python train_algorithm.py
Write algorithm number(one, two, three ... etc): 11
┌─────────────────────────┐
│ 💰 Currency: USD        │
│ 💵 Exchange: 41.2215    │
│ 📅 Date: 02.10.2025     │
└─────────────────────────┘

┌─────────────────────────┐
│ 💰 Currency: EUR        │
│ 💵 Exchange: 48.3734    │
│ 📅 Date: 02.10.2025     │
└─────────────────────────┘
```

## 🛠️ Project Structure

```
train_algoritm/
├── README.md              # Project documentation
├── train_algorithm.py     # Main program with all algorithms
├── requirements.txt       # Python dependencies
└── venv/                  # Virtual environment (created by you)
```

## 📚 Notes

- Most algorithms use only Python's standard library (`re` module for regex)
- Algorithm #11 requires the `requests` library for API calls to NBU
- External packages are listed in `requirements.txt`
- Virtual environment is recommended but optional
- All algorithms include basic error handling for invalid inputs

## 📄 License

This is an educational project for learning purposes.
