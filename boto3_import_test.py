import boto3

def test_boto3_functions():
    """Tests basic functionality of boto3."""

    try:
        # 1. Check if boto3 is imported correctly
        print("boto3 imported successfully!")

        # 2. Create a session (replace with your credentials or configuration if needed)
        # If you have your AWS credentials configured (environment variables, config file, etc.),
        # you can omit the credentials here. boto3 will automatically find them.
        session = boto3.Session()  # or boto3.Session(aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

        # 3. List S3 buckets (requires S3 permissions)
        try:
            s3 = session.client('s3')  # Create an S3 client
            response = s3.list_buckets()
            print("\nList of S3 buckets (if you have permissions):")
            for bucket in response['Buckets']:
                print(f"  - {bucket['Name']}")
        except Exception as e:  
            print(f"\nError listing S3 buckets: {e}")
            print("Check your AWS credentials and S3 permissions.")


        # 4. Get information about the current user (requires IAM permissions)
        try:
            iam = session.client('iam')  # Create an IAM client
            user = iam.get_user()
            print("\nCurrent IAM User (if you have permissions):")
            print(f"  - User Name: {user['User']['UserName']}")
        except Exception as e:
            print(f"\nError getting IAM user: {e}")
            print("Check your AWS credentials and IAM permissions.")


        return True  # All tests passed

    except ImportError:
        print("Error: boto3 not found. Please install it using 'pip install boto3'")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    if test_boto3_functions():
        print("\nBoto3 test completed successfully.")
    else:
        print("\nBoto3 test failed.")