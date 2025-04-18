# send_query

設計支援システムとの連携API

## Arg

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Distributed catalog send query API url** | **str**] | 分散カタログサービスのURL | 
**SPARQL SQL * | **str**] | 発行したいSPARQL Query | 

## Example

```python
from drone_distract.lib_distribute_catalog import send_query

def main():
    send_query(
        'http://example.com/v1/api/sendQuery',  # 分散カタログサービスのURL
        "SELECT ?s ?p ?o WHERE { ?s ?p ?o .  }")  # 発行したいSPARQL Query

if __name__ == '__main__':
    main()
~
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


