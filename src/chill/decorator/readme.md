### Python OOP & Decorator Challenge: Secure File Processor

**Objective:** Build a class that handles file operations (reading and writing), but with added functionality for logging and access control, implemented via decorators. This will test your understanding of class structure, instance state, and how decorators can elegantly modify or wrap method behavior.

**The Scenario:**

Imagine you are building a system component, a `FileProcessor`, that needs to interact with the filesystem. For security and auditing purposes, you have two requirements:

1.  **Audit Trail:** Every time a file is read or written, the action must be logged to the console.
2.  **Access Control:** Only users with an 'admin' role should be allowed to write or delete files. Users with a 'viewer' role should only be able to read.

Decorators are a perfect, pythonic way to implement this cross-cutting logic without cluttering your core business logic (the reading and writing of files).

---

#### **Your Tasks:**

**Part 1: The Decorators**

First, implement two decorators.

1.  **`@log_action` decorator:**
    * This decorator should print a log message *before* the decorated function is called, and another one *after* it completes.
    * **Example Log Output:**
        ```
        [LOG] Calling 'read_file' with args: ('my_data.txt',), kwargs: {}
        [LOG] 'read_file' executed successfully.
        ```

2.  **`@requires_permission(required_role)` decorator:**
    * This is a decorator that accepts an argument (`required_role`, e.g., 'admin').
    * When applied to a method of the `FileProcessor` class, it should check the `role` of the instance (`self.role`).
    * If `self.role` is not equal to the `required_role`, it should raise a `PermissionError` with a clear message and prevent the method from running.
    * If the roles match, the method should execute as normal.
    * **Hint:** This requires creating a decorator that returns another decorator (a closure).

**Part 2: The `FileProcessor` Class**

Next, create the `FileProcessor` class.

**Requirements:**

1.  **Initialization (`__init__`):**
    * The constructor should accept a `role` (e.g., 'viewer' or 'admin') and store it as an instance attribute (e.g., `self.role`).

2.  **Methods:**
    * Create a method `read_file(self, path)`. This method can simply print a message like `Reading from {path}` and return a dummy string `"file content"`.
    * Create a method `write_file(self, path, data)`. This can simply print `Writing '{data}' to {path}`.

3.  **Applying the Decorators:**
    * Apply the `@log_action` decorator to *both* `read_file` and `write_file`.
    * Apply the `@requires_permission('admin')` decorator to the `write_file` method.

---

**Part 3: Demonstration**

Show how your class and decorators work.

1.  Create an instance of `FileProcessor` with the role 'viewer'.
    * Call `read_file` on it. It should succeed and show the log messages.
    * Call `write_file` on it. It should fail with a `PermissionError`. Use a `try...except` block to catch the error gracefully.

2.  Create an instance of `FileProcessor` with the role 'admin'.
    * Call `read_file` on it.
    * Call `write_file` on it. Both should succeed and show the log messages.

This exercise will solidify your understanding of how `self` works within methods, and how decorators can inspect and interact with the arguments and instance of the method they are wrapping. Good luck!