from ckanapi import RemoteCKAN


def main():
    ua = "ckanapiexample/1.0 (+http://example.com/my/website)"
    swiss_data = RemoteCKAN("https://ckan.opendata.swiss", user_agent=ua)

    # groups = swiss_data.action.status_show()
    # print(groups)

    # organization_list = swiss_data.action.organization_list()
    # print(organization_list)

    # Datasets
    # datasets = swiss_data.action.package_list()
    # for dataset in datasets:
    #     print(dataset)
    # print(len(datasets))

    # dataset = swiss_data.action.package_show(id="scheurmann-karte-bleistift")
    # for resource in dataset.get("resources", []):
    #     print(resource)
    # print(dataset)

    # search_results = swiss_data.action.package_search(
    #     fq="organization:bundesamt-fur-statistik-bfs"
    # )
    # for dataset in search_results["results"]:
    #     print(f"- {dataset['title']}")

    # params = {"facet.field": '["tags"]', "facet.limit": 100, "rows": 0}
    #
    # # Execute the search
    # results = swiss_data.action.package_search(**params)
    #
    # # Access the facets
    # tags_facets = results.get("search_facets", {}).get("tags", {}).get("items", [])
    #
    # for tag in tags_facets:
    #     print(f"Tag: {tag['display_name']} | Count: {tag['count']}")


if __name__ == "__main__":
    main()
