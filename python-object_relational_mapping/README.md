# Python Object Relational Mapping (ORM) Project

This project demonstrates Object-Relational Mapping (ORM) concepts using Python with MySQL database. The project includes both raw MySQL database operations and SQLAlchemy ORM implementations.

## 📋 Requirements

### General Requirements
- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS with Python 3.8.5
- **Database**: MySQL 2.0.x
- **ORM**: SQLAlchemy 1.4.x
- **Code Style**: pycodestyle version 2.7.*
- **Execution**: All files must be executable
- **Documentation**: All modules, classes, and functions must have proper documentation

### Technical Requirements
- First line of all files: `#!/usr/bin/python3`
- All files should end with a new line
- Code should not be executed when imported (`if __name__ == "__main__":`)
- No use of `execute` with SQLAlchemy

## 🚀 Installation

### Prerequisites
Make sure you have MySQL server running. If using Docker:

```bash
# Check if MySQL is running
mysql --version
```

### Install Required Python Packages

```bash
# Install MySQL client
pip3 install mysqlclient==2.0.3

# Install SQLAlchemy ORM
pip3 install SQLAlchemy==1.4.22
```

### System Dependencies (if needed)
If you encounter installation errors, install these system packages:

```bash
sudo apt-get update
sudo apt-get install -y libmysqlclient-dev python3-dev build-essential pkg-config
```

### Verify Installation

```bash
# Check MySQLdb installation
python3 -c "import MySQLdb; print('MySQLdb installed successfully')"

# Check SQLAlchemy installation
python3 -c "import sqlalchemy; print(f'SQLAlchemy version: {sqlalchemy.__version__}')"
```

## 📚 Usage Examples

### Task 0: Basic MySQL Connection
```bash
# Create and populate database
cat 0-select_states.sql | mysql -uroot -p

# Run the script
./0-select_states.py root password hbtn_0e_0_usa
```

Expected output:
```
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

### Task 6+: SQLAlchemy ORM Examples
```bash
# Run ORM examples
./6-model_state.py root password hbtn_0e_0_usa
./7-model_state_fetch_all.py root password hbtn_0e_0_usa
```

## 🧪 Testing

### Manual Testing
Each script can be tested individually:

```bash
# Make script executable
chmod +x script_name.py

# Run with required arguments
./script_name.py username password database_name
```

### Verification Commands
```bash
# Check code style
pycodestyle *.py

# Verify documentation
python3 -c "print(__import__('module_name').__doc__)"
python3 -c "print(__import__('module_name').ClassName.__doc__)"
python3 -c "print(__import__('module_name').function_name.__doc__)"
```

## 🐛 Common Issues and Solutions

### Issue: mysqlclient installation fails
**Solution**: Install system dependencies first
```bash
sudo apt-get install libmysqlclient-dev python3-dev build-essential
```

### Issue: Permission denied when running scripts
**Solution**: Make files executable
```bash
chmod +x *.py
```

### Issue: MySQL connection refused
**Solution**: Check MySQL service status
```bash
sudo service mysql status
sudo service mysql start  # if not running
```

### Issue: Import errors in SQLAlchemy
**Solution**: Verify correct versions
```bash
pip3 list | grep -i sqlalchemy
pip3 list | grep -i mysql
```


## 📝 Notes

- All scripts are designed to be executed directly, not imported
- Database connections are properly managed with cleanup
- Error handling follows Python best practices
- Code is compatible with Python 3.8.5 and specified package versions

## 🔗 Additional Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [MySQL Python Connector Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [Python PEP 8 Style Guide](https://pep8.org/)
- [SQL Injection Prevention](https://owasp.org/www-community/attacks/SQL_Injection)

---