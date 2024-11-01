### Part I: Data Structures

1. **Chapter 1 - Python Data Model**: **Card Deck Simulation**

   - Build a `Deck` class for playing cards, with special methods for indexing, slicing, and iterating.
   - Use dunder methods like `__len__`, `__getitem__`, and `__str__` to provide natural behavior for the deck and card objects.
   - Extend by adding operations like shuffling, drawing cards, and comparing card ranks.

2. **Chapter 2 - Sequences and Arrays**: **Task List Manager**

   - Implement a `TaskList` class that behaves like a sequence. Allow indexing, slicing, and sorting tasks based on priority or deadline.
   - Practice list comprehensions and generator expressions to filter and display tasks.
   - Introduce sequence unpacking and pattern matching for task attributes.

3. **Chapter 3 - Dictionaries and Sets**: **Contact Book**

   - Create a `ContactBook` to store contact information, using dictionaries to store data and sets for tags like “friends” or “work.”
   - Use dictionary and set comprehensions to manage contacts and tags efficiently.
   - Explore merging dictionaries and handling missing data with `defaultdict`.

4. **Chapter 4 - Unicode Text vs. Bytes**: **Text Encoding Tool**

   - Build a tool to encode, decode, and analyze text. Use different encodings and handle text files with multilingual support.
   - Implement Unicode normalization to clean text and use byte operations for encoded data.
   - Provide options for common encoding issues like handling BOM (Byte Order Mark).

5. **Chapter 5 - Data Class Builders**: **Library Catalog**

   - Implement a catalog system for a library using `@dataclass` to define `Book`, `Author`, and `Genre`.
   - Use `namedtuple` for simple data types, like `Location` for shelf coordinates.
   - Practice data validation and type hints for each data class, making sure catalog entries are consistent and accurate.

6. **Chapter 6 - Object References, Mutability, and Recycling**: **Memory Tracker**
   - Develop a small system to track object references and memory use for a collection of `Document` objects.
   - Implement a system to safely handle mutable data, and learn about shallow and deep copies.
   - Experiment with garbage collection by creating and deleting references.

### Part II: Functions as Objects

7. **Chapter 7 - Functions as First-Class Objects**: **Simple Calculator**

   - Create a calculator that supports basic operations using functions as first-class objects.
   - Store operations in a dictionary (`{'add': add, 'subtract': subtract, ...}`) and allow users to extend the calculator by adding new operations.
   - Implement higher-order functions to apply a series of operations to inputs and closures to track usage statistics.

8. **Chapter 8 - Type Hints in Functions**: **Budget Planner**

   - Design a `BudgetPlanner` tool with functions that take and return typed data for expense entries, budget limits, and balances.
   - Use type hints to ensure data consistency, and apply `mypy` or a similar tool to validate function signatures.
   - Practice writing functions that handle both optional and union types to support a flexible budget structure.

9. **Chapter 9 - Decorators and Closures**: **API Request Logger**

   - Build a decorator-based logging system for an API handler that tracks and logs each request's details (e.g., timing, status, errors).
   - Use closures to maintain state across requests, such as counting each type of request (GET, POST).
   - Add memoization to cache frequently accessed API responses using `lru_cache`.

10. **Chapter 10 - Design Patterns with Functions**: **Strategy-Based Discount System**

- Implement a discount system using the Strategy pattern, where different discount functions can be applied to orders based on rules (e.g., holiday, bulk).
- Use higher-order functions to apply the discount strategies.
- Practice selecting appropriate patterns for specific cases to improve flexibility and scalability.

### Part III: Classes and Protocols

11. **Chapter 11 - Classes and Protocols**: **Virtual File System**

- Build a virtual file system with `File` and `Directory` classes, with each file system component supporting basic operations (read, write, delete).
- Implement protocols to define expected behaviors and explore duck typing for file-like objects.
- Add custom methods to support moving, copying, and deleting files within directories.

12. **Chapter 12 - Special Methods for Sequences**: **Vector Operations**

- Design a `Vector` class that behaves like a sequence, with custom methods for addition, subtraction, and dot products.
- Overload operators (`+`, `-`, `*`) and use dunder methods like `__getitem__` and `__len__`.
- Implement attribute access using dynamic attribute names, such as `.x` and `.y`.

13. **Chapter 13 - Interfaces, Protocols, and ABCs**: **Shape Interface**

- Create a hierarchy of shapes (`Circle`, `Rectangle`, `Square`) using abstract base classes (ABCs) and protocols.
- Define a `Drawable` protocol to ensure all shapes support a `draw()` method.
- Practice using protocols for enforcing a common interface and designing flexible, scalable class hierarchies.

14. **Chapter 14 - Inheritance**: **Social Media Post System**

- Build a post system for a social media application with different post types (e.g., `TextPost`, `ImagePost`, `VideoPost`) inheriting from a `BasePost` class.
- Use mixin classes to add reusable functionalities like tagging, liking, and commenting.
- Practice composition over inheritance by combining multiple behaviors in a single post.

15. **Chapter 15 - Advanced Type Hints**: **Data Pipeline**

- Create a data pipeline system for loading, processing, and transforming data. Use advanced type hints, such as generics, for a flexible pipeline that handles various data types.
- Implement parameterized classes and protocols to enforce correct data handling at each pipeline stage.
- Use unions and optionals to handle optional stages, like logging or data transformation.

### Part IV: Control Flow

16. **Chapter 16 - Operator Overloading**: **Bank Account System**

- Build a bank account system that supports operations like deposit, withdraw, and transfer using operator overloading.
- Implement `+` and `-` for deposits and withdrawals and `+=` and `-=` for bulk adjustments.
- Add custom comparison methods to compare account balances.

17. **Chapter 17 - Iterators and Generators**: **Document Reader**

- Create a document reader that uses iterators to read lines or paragraphs.
- Implement a generator to produce a lazy-loaded stream of lines, paragraphs, or sentences.
- Experiment with nested generators to handle more complex document structures, like chapters or sections.

18. **Chapter 18 - with, match, and else Blocks**: **File Processor**

- Build a file processor that reads, processes, and saves files, using context managers to handle resources cleanly.
- Use pattern matching for different file formats, applying specific processing rules to each.
- Implement `else` blocks for handling cases where processing completes successfully.

19. **Chapter 19 - Concurrency Models**: **Web Scraper**

- Implement a web scraper that uses threads, processes, or async coroutines to download and parse multiple web pages concurrently.
- Experiment with each concurrency model to understand their strengths, such as using `asyncio` for I/O-bound tasks.
- Track and compare performance metrics for each approach.

20. **Chapter 20 - Concurrent Executors**: **Image Processor**

- Build an image processing system that uses concurrent executors for batch processing (e.g., resizing, filtering).
- Use futures and `ThreadPoolExecutor` or `ProcessPoolExecutor` to process images in parallel.
- Implement error handling to manage failed tasks gracefully.

21. **Chapter 21 - Asynchronous Programming**: **Async Chat Application**

- Create a real-time chat application with `asyncio` to handle message passing between users.
- Use asynchronous iterators for real-time message retrieval and processing.
- Implement throttling for chat rate limits and experiment with asynchronous data storage.

### Part V: Metaprogramming

22. **Chapter 22 - Dynamic Attributes and Properties**: **Configuration Manager**

- Build a configuration manager that loads settings dynamically from JSON or environment variables, using dynamic attributes.
- Implement properties to retrieve or set configuration values with validation.
- Allow access to configuration settings like `config.database.url` or `config.api.key`.

23. **Chapter 23 - Attribute Descriptors**: **Validated Settings System**

- Create a `Settings` class with descriptors to enforce validation rules, such as range limits or format checks.
- Implement custom descriptors to validate data types, ensuring each setting conforms to the expected structure.
- Use descriptors to manage dependencies between settings, like requiring a URL to be set before API keys.

24. **Chapter 24 - Class Metaprogramming**: **ORM (Object-Relational Mapper)**

- Build a mini ORM using metaclasses to automatically generate SQL commands based on class definitions.
- Use metaclasses to register models, define fields, and create CRUD operations.
- Experiment with class decorators and metaclasses to handle dynamic table creation and data mapping.

Each of these projects will deepen your understanding of the

chapter’s concepts, and together, they create a strong foundation to build the combined Project Management System (PMS) later.
