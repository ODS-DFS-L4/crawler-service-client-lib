# get_route_operator

航路運営者サーバーを取得します

## Arg

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Distributed catalog send query API url** | **str** | DiscoveryFinder のURL | 
**DistributedCatalog WebAPI** | **str** | 分散カタログサービスの　SendQuery WebAPI | 

## Example

```python
from drone_distcat.lib_distribute_catalog import get_route_operator

def main():
    print(get_route_operator(
        'http://example.com',  # DiscoveryFinder　URL
        'http://example.com:8081'))  # DistributedCatalog WebAPI

if __name__ == '__main__':
    main()
~
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


