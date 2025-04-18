from drone_distcat.lib_distribute_catalog import send_query


def main():
    send_query(
        'http://crawler-service.example.com/v1/api/sendQuery',
        "SELECT ?s ?p ?o WHERE { ?s ?p ?o .  }")


if __name__ == '__main__':
    main()
