import sys, os
import cx_Oracle
import traceback
import Banner_Connections.ODSP_Creds as creds
import Banner_Connections.queries as query

def banner_odsp_handler():
  """Function to initialize an object from the cx_Oracle Connection class
  :returns a cx_Oracle Connection object if valid credentials exist otherwise
  prints a traceback error"""
  host = creds.host
  port = creds.port
  sid = creds.sid
  username = creds.username
  password = creds.password

  try:
    dsn = cx_Oracle.makedsn(host, port, sid)
    #print(dsn)
    connection = cx_Oracle.Connection("%s/%s@%s" % (username, password, dsn))
    return connection
  except cx_Oracle.DatabaseError as exc:
    error, = exc.args
    print(sys.stderr, "Oracle-Error-Code:", error.code)
    print(sys.stderr, "Oracle-Error-Message:", error.message)
    tb = traceback.format_exc()
    return tb


def banner_ODSP_tele(connection, query_name):
  """The banner_ODSP_tele function takes in an connection
  argument to connect to ODSP. It then accepts a specific query
  as the second argument and returns the query results"""
  cursor = connection.cursor()
  cursor.execute(query_name)
  try:
    query_result = [(area_code, number) for area_code, number in cursor]
    cleaned_number = [''.join(number) for number in query_result]
    return cleaned_number
  finally:
    cursor.close()
    connection.close()


def banner_ODSP_emails(connection, query_name):
  """The banner_ODSP_tele function takes in an connection
  argument to connect to ODSP. It then accepts a specific query
  as the second argument and returns the query results"""
  cursor = connection.cursor()
  cursor.execute(query_name)
  try:
    query_result = [email[0] for email in cursor]
    cleaned_email = ''.join(email for email in query_result)
    return cleaned_email
  finally:
    cursor.close()
    connection.close()

#if __name__ == "__main__":
#   print(banner_ODSP_emails(banner_odsp_handler(), query.run_single_email_query()))