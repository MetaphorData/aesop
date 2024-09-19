from rich import print

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.graphql.generated.custom_fields import InfoFields, OIDCFields, SAMLFields
from aesop.graphql.generated.custom_queries import Query


@exception_handler(command="info", exception_type=Exception)
def info(config: AesopConfig) -> None:
    # TODO uncomment me!
    # info_query = Query.info(config=config.config).fields(
    #     InfoFields.oidc().fields(OIDCFields.sign_in_redirect_url),
    #     InfoFields.saml().fields(
    #         SAMLFields.entity_id, SAMLFields.reply_acs_url, SAMLFields.sign_on_url
    #     ),
    # )
    res = config.get_graphql_client().query(Query.crawler_ip_addresses(), operation_name="getInfo")
    print(res)
