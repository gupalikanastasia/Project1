from functools import wraps

def type_checker(**expected_types):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig = inspect.signature(func)

            try:
                bound_args = sig.bind(*args, **kwargs)
                bound_args.apply_defaults()
                actual_args = bound_args.arguments
            except TypeError as e:
                raise TypeError(f"Помилка при виклику функції '{func.__name__}': {e}")

            for arg_name, expected_type in expected_types.items():
                if arg_name in actual_args:
                    actual_value = actual_args[arg_name]
                    if not isinstance(actual_value, expected_type):
                        raise TypeError(
                            f"Помилка типу в аргументі '{arg_name}' функції '{func.__name__}': "
                            f"Очікувався тип **{expected_type.__name__}**, отримано **{type(actual_value).__name__}** "
                            f"зі значенням '{actual_value}'."
                        )

            return func(*args, **kwargs)

        return wrapper

    return decorator