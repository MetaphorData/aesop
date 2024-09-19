from rich import print

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.graphql.generated.custom_fields import OIDCFields, SAMLFields, SetupInfoFields
from aesop.graphql.generated.custom_queries import Query


@exception_handler(command="info", exception_type=Exception)
def info(config: AesopConfig) -> None:
    setup_info_query = Query.setup_info().fields(
        SetupInfoFields.oidc().fields(OIDCFields.signInRedirectUrl),
        SetupInfoFields.saml().fields(
            SAMLFields.entityId, SAMLFields.replyACSUrl, SAMLFields.signOnUrl
        ),
        SetupInfoFields.crawlerIpAddresses,
    )
    res = config.get_graphql_client().query(setup_info_query, operation_name="getInfo")
    print(res)
