"""Generated message classes for accesscontextmanager version v1alpha.

An API for setting attribute based access control to requests to GCP services.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'accesscontextmanager'


class AccessLevel(_messages.Message):
  r"""An `AccessLevel` is a label that can be applied to requests to GCP
  services, along with a list of requirements necessary for the label to be
  applied.

  Fields:
    basic: A `BasicLevel` composed of `Conditions`.
    createTime: Output only. Time the `AccessLevel` was created in UTC.
    description: Description of the `AccessLevel` and its use. Does not affect
      behavior.
    name: Required. Resource name for the Access Level. The `short_name`
      component must begin with a letter and only include alphanumeric and
      '_'. Format: `accessPolicies/{policy_id}/accessLevels/{short_name}`
    title: Human readable title. Must be unique within the Policy.
    updateTime: Output only. Time the `AccessLevel` was updated in UTC.
  """

  basic = _messages.MessageField('BasicLevel', 1)
  createTime = _messages.StringField(2)
  description = _messages.StringField(3)
  name = _messages.StringField(4)
  title = _messages.StringField(5)
  updateTime = _messages.StringField(6)


class AccessPolicy(_messages.Message):
  r"""`AccessPolicy` is a container for `AccessLevels` (which define the
  necessary attributes to use GCP services) and `ServicePerimeters` (which
  define regions of services able to freely pass data within a perimeter). An
  access policy is globally visible within an organization, and the
  restrictions it specifies apply to all projects within an organization.

  Fields:
    createTime: Output only. Time the `AccessPolicy` was created in UTC.
    name: Output only. Resource name of the `AccessPolicy`. Format:
      `accessPolicies/{policy_id}`
    parent: Required. The parent of this `AccessPolicy` in the Cloud Resource
      Hierarchy. Currently immutable once created. Format:
      `organizations/{organization_id}`
    title: Required. Human readable title. Does not affect behavior.
    updateTime: Output only. Time the `AccessPolicy` was updated in UTC.
  """

  createTime = _messages.StringField(1)
  name = _messages.StringField(2)
  parent = _messages.StringField(3)
  title = _messages.StringField(4)
  updateTime = _messages.StringField(5)


class AccesscontextmanagerAccessPoliciesAccessLevelsCreateRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesAccessLevelsCreateRequest object.

  Fields:
    accessLevel: A AccessLevel resource to be passed as the request body.
    parent: Required. Resource name for the access policy which owns this
      Access Level.  Format: `accessPolicies/{policy_id}`
  """

  accessLevel = _messages.MessageField('AccessLevel', 1)
  parent = _messages.StringField(2, required=True)


class AccesscontextmanagerAccessPoliciesAccessLevelsDeleteRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesAccessLevelsDeleteRequest object.

  Fields:
    name: Required. Resource name for the Access Level.  Format:
      `accessPolicies/{policy_id}/accessLevels/{access_level_id}`
  """

  name = _messages.StringField(1, required=True)


class AccesscontextmanagerAccessPoliciesAccessLevelsGetRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesAccessLevelsGetRequest object.

  Enums:
    AccessLevelFormatValueValuesEnum: Whether to return `BasicLevels` in the
      Cloud Common Expression Language rather than as `BasicLevels`. Defaults
      to AS_DEFINED, where Access Levels are returned as `BasicLevels` or
      `CustomLevels` based on how they were created. If set to CEL, all Access
      Levels are returned as `CustomLevels`. In the CEL case, `BasicLevels`
      are translated to equivalent `CustomLevels`.

  Fields:
    accessLevelFormat: Whether to return `BasicLevels` in the Cloud Common
      Expression Language rather than as `BasicLevels`. Defaults to
      AS_DEFINED, where Access Levels are returned as `BasicLevels` or
      `CustomLevels` based on how they were created. If set to CEL, all Access
      Levels are returned as `CustomLevels`. In the CEL case, `BasicLevels`
      are translated to equivalent `CustomLevels`.
    name: Required. Resource name for the Access Level.  Format:
      `accessPolicies/{policy_id}/accessLevels/{access_level_id}`
  """

  class AccessLevelFormatValueValuesEnum(_messages.Enum):
    r"""Whether to return `BasicLevels` in the Cloud Common Expression
    Language rather than as `BasicLevels`. Defaults to AS_DEFINED, where
    Access Levels are returned as `BasicLevels` or `CustomLevels` based on how
    they were created. If set to CEL, all Access Levels are returned as
    `CustomLevels`. In the CEL case, `BasicLevels` are translated to
    equivalent `CustomLevels`.

    Values:
      LEVEL_FORMAT_UNSPECIFIED: <no description>
      AS_DEFINED: <no description>
      CEL: <no description>
    """
    LEVEL_FORMAT_UNSPECIFIED = 0
    AS_DEFINED = 1
    CEL = 2

  accessLevelFormat = _messages.EnumField('AccessLevelFormatValueValuesEnum', 1)
  name = _messages.StringField(2, required=True)


class AccesscontextmanagerAccessPoliciesAccessLevelsListRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesAccessLevelsListRequest object.

  Enums:
    AccessLevelFormatValueValuesEnum: Whether to return `BasicLevels` in the
      Cloud Common Expression language, as `CustomLevels`, rather than as
      `BasicLevels`. Defaults to returning `AccessLevels` in the format they
      were defined.

  Fields:
    accessLevelFormat: Whether to return `BasicLevels` in the Cloud Common
      Expression language, as `CustomLevels`, rather than as `BasicLevels`.
      Defaults to returning `AccessLevels` in the format they were defined.
    pageSize: Number of Access Levels to include in the list. Default 100.
    pageToken: Next page token for the next batch of Access Level instances.
      Defaults to the first page of results.
    parent: Required. Resource name for the access policy to list Access
      Levels from.  Format: `accessPolicies/{policy_id}`
  """

  class AccessLevelFormatValueValuesEnum(_messages.Enum):
    r"""Whether to return `BasicLevels` in the Cloud Common Expression
    language, as `CustomLevels`, rather than as `BasicLevels`. Defaults to
    returning `AccessLevels` in the format they were defined.

    Values:
      LEVEL_FORMAT_UNSPECIFIED: <no description>
      AS_DEFINED: <no description>
      CEL: <no description>
    """
    LEVEL_FORMAT_UNSPECIFIED = 0
    AS_DEFINED = 1
    CEL = 2

  accessLevelFormat = _messages.EnumField('AccessLevelFormatValueValuesEnum', 1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class AccesscontextmanagerAccessPoliciesAccessLevelsPatchRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesAccessLevelsPatchRequest object.

  Fields:
    accessLevel: A AccessLevel resource to be passed as the request body.
    name: Required. Resource name for the Access Level. The `short_name`
      component must begin with a letter and only include alphanumeric and
      '_'. Format: `accessPolicies/{policy_id}/accessLevels/{short_name}`
    updateMask: Required. Mask to control which fields get updated. Must be
      non-empty.
  """

  accessLevel = _messages.MessageField('AccessLevel', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class AccesscontextmanagerAccessPoliciesDeleteRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesDeleteRequest object.

  Fields:
    name: Required. Resource name for the access policy to delete.  Format
      `accessPolicies/{policy_id}`
  """

  name = _messages.StringField(1, required=True)


class AccesscontextmanagerAccessPoliciesGetRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesGetRequest object.

  Fields:
    name: Required. Resource name for the access policy to get.  Format
      `accessPolicies/{policy_id}`
  """

  name = _messages.StringField(1, required=True)


class AccesscontextmanagerAccessPoliciesListRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesListRequest object.

  Fields:
    pageSize: Number of AccessPolicy instances to include in the list. Default
      100.
    pageToken: Next page token for the next batch of AccessPolicy instances.
      Defaults to the first page of results.
    parent: Required. Resource name for the container to list AccessPolicy
      instances from.  Format: `organizations/{org_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3)


class AccesscontextmanagerAccessPoliciesPatchRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesPatchRequest object.

  Fields:
    accessPolicy: A AccessPolicy resource to be passed as the request body.
    name: Output only. Resource name of the `AccessPolicy`. Format:
      `accessPolicies/{policy_id}`
    updateMask: Required. Mask to control which fields get updated. Must be
      non-empty.
  """

  accessPolicy = _messages.MessageField('AccessPolicy', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class AccesscontextmanagerAccessPoliciesServicePerimetersCreateRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesServicePerimetersCreateRequest
  object.

  Fields:
    parent: Required. Resource name for the access policy which owns this
      Service Perimeter.  Format: `accessPolicies/{policy_id}`
    servicePerimeter: A ServicePerimeter resource to be passed as the request
      body.
  """

  parent = _messages.StringField(1, required=True)
  servicePerimeter = _messages.MessageField('ServicePerimeter', 2)


class AccesscontextmanagerAccessPoliciesServicePerimetersDeleteRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesServicePerimetersDeleteRequest
  object.

  Fields:
    name: Required. Resource name for the Service Perimeter.  Format:
      `accessPolicies/{policy_id}/servicePerimeters/{service_perimeter_id}`
  """

  name = _messages.StringField(1, required=True)


class AccesscontextmanagerAccessPoliciesServicePerimetersGetRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesServicePerimetersGetRequest object.

  Fields:
    name: Required. Resource name for the Service Perimeter.  Format:
      `accessPolicies/{policy_id}/servicePerimeters/{service_perimeters_id}`
  """

  name = _messages.StringField(1, required=True)


class AccesscontextmanagerAccessPoliciesServicePerimetersListRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesServicePerimetersListRequest object.

  Fields:
    pageSize: Number of Service Perimeters to include in the list. Default
      100.
    pageToken: Next page token for the next batch of Service Perimeter
      instances. Defaults to the first page of results.
    parent: Required. Resource name for the access policy to list Service
      Perimeters from.  Format: `accessPolicies/{policy_id}`
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class AccesscontextmanagerAccessPoliciesServicePerimetersPatchRequest(_messages.Message):
  r"""A AccesscontextmanagerAccessPoliciesServicePerimetersPatchRequest
  object.

  Fields:
    name: Required. Resource name for the ServicePerimeter.  The `short_name`
      component must begin with a letter and only include alphanumeric and
      '_'. Format: `accessPolicies/{policy_id}/servicePerimeters/{short_name}`
    servicePerimeter: A ServicePerimeter resource to be passed as the request
      body.
    updateMask: Required. Mask to control which fields get updated. Must be
      non-empty.
  """

  name = _messages.StringField(1, required=True)
  servicePerimeter = _messages.MessageField('ServicePerimeter', 2)
  updateMask = _messages.StringField(3)


class AccesscontextmanagerOperationsGetRequest(_messages.Message):
  r"""A AccesscontextmanagerOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class BasicLevel(_messages.Message):
  r"""`BasicLevel` is an `AccessLevel` using a set of recommended features.

  Enums:
    CombiningFunctionValueValuesEnum: How the `conditions` list should be
      combined to determine if a request is granted this `AccessLevel`. If AND
      is used, each `Condition` in `conditions` must be satisfied for the
      `AccessLevel` to be applied. If OR is used, at least one `Condition` in
      `conditions` must be satisfied for the `AccessLevel` to be applied.
      Default behavior is AND.

  Fields:
    combiningFunction: How the `conditions` list should be combined to
      determine if a request is granted this `AccessLevel`. If AND is used,
      each `Condition` in `conditions` must be satisfied for the `AccessLevel`
      to be applied. If OR is used, at least one `Condition` in `conditions`
      must be satisfied for the `AccessLevel` to be applied. Default behavior
      is AND.
    conditions: Required. A list of requirements for the `AccessLevel` to be
      granted.
  """

  class CombiningFunctionValueValuesEnum(_messages.Enum):
    r"""How the `conditions` list should be combined to determine if a request
    is granted this `AccessLevel`. If AND is used, each `Condition` in
    `conditions` must be satisfied for the `AccessLevel` to be applied. If OR
    is used, at least one `Condition` in `conditions` must be satisfied for
    the `AccessLevel` to be applied. Default behavior is AND.

    Values:
      AND: All `Conditions` must be true for the `BasicLevel` to be true.
      OR: If at least one `Condition` is true, then the `BasicLevel` is true.
    """
    AND = 0
    OR = 1

  combiningFunction = _messages.EnumField('CombiningFunctionValueValuesEnum', 1)
  conditions = _messages.MessageField('Condition', 2, repeated=True)


class Condition(_messages.Message):
  r"""A condition necessary for an `AccessLevel` to be granted. The Condition
  is an AND over its fields. So a Condition is true if: 1) the request IP is
  from one of the listed subnetworks AND 2) the originating device complies
  with the listed device policy AND 3) all listed access levels are granted
  AND 4) the request was sent at a time allowed by the DateTimeRestriction.

  Fields:
    devicePolicy: Device specific restrictions, all restrictions must hold for
      the Condition to be true. If not specified, all devices are allowed.
    ipSubnetworks: CIDR block IP subnetwork specification. May be IPv4 or
      IPv6. Note that for a CIDR IP address block, the specified IP address
      portion must be properly truncated (i.e. all the host bits must be zero)
      or the input is considered malformed. For example, "192.0.2.0/24" is
      accepted but "192.0.2.1/24" is not. Similarly, for IPv6, "2001:db8::/32"
      is accepted whereas "2001:db8::1/32" is not. The originating IP of a
      request must be in one of the listed subnets in order for this Condition
      to be true. If empty, all IP addresses are allowed.
    members: The request must be made by one of the provided user or service
      accounts. Groups are not supported. Syntax: `user:{emailid}`
      `serviceAccount:{emailid}` If not specified, a request may come from any
      user.
    negate: Whether to negate the Condition. If true, the Condition becomes a
      NAND over its non-empty fields, each field must be false for the
      Condition overall to be satisfied. Defaults to false.
    regions: The request must originate from one of the provided
      countries/regions. Must be valid ISO 3166-1 alpha-2 codes.
    requiredAccessLevels: A list of other access levels defined in the same
      `Policy`, referenced by resource name. Referencing an `AccessLevel`
      which does not exist is an error. All access levels listed must be
      granted for the Condition to be true. Example:
      "`accessPolicies/MY_POLICY/accessLevels/LEVEL_NAME"`
  """

  devicePolicy = _messages.MessageField('DevicePolicy', 1)
  ipSubnetworks = _messages.StringField(2, repeated=True)
  members = _messages.StringField(3, repeated=True)
  negate = _messages.BooleanField(4)
  regions = _messages.StringField(5, repeated=True)
  requiredAccessLevels = _messages.StringField(6, repeated=True)


class DevicePolicy(_messages.Message):
  r"""`DevicePolicy` specifies device specific restrictions necessary to
  acquire a given access level. A `DevicePolicy` specifies requirements for
  requests from devices to be granted access levels, it does not do any
  enforcement on the device. `DevicePolicy` acts as an AND over all specified
  fields, and each repeated field is an OR over its elements. Any unset fields
  are ignored. For example, if the proto is { os_type : DESKTOP_WINDOWS,
  os_type : DESKTOP_LINUX, encryption_status: ENCRYPTED}, then the
  DevicePolicy will be true for requests originating from encrypted Linux
  desktops and encrypted Windows desktops.

  Enums:
    AllowedDeviceManagementLevelsValueListEntryValuesEnum:
    AllowedEncryptionStatusesValueListEntryValuesEnum:

  Fields:
    allowedDeviceManagementLevels: Allowed device management levels, an empty
      list allows all management levels.
    allowedEncryptionStatuses: Allowed encryptions statuses, an empty list
      allows all statuses.
    osConstraints: Allowed OS versions, an empty list allows all types and all
      versions.
    requireAdminApproval: Whether the device needs to be approved by the
      customer admin.
    requireCorpOwned: Whether the device needs to be corp owned.
    requireScreenlock: Whether or not screenlock is required for the
      DevicePolicy to be true. Defaults to `false`.
  """

  class AllowedDeviceManagementLevelsValueListEntryValuesEnum(_messages.Enum):
    r"""AllowedDeviceManagementLevelsValueListEntryValuesEnum enum type.

    Values:
      MANAGEMENT_UNSPECIFIED: <no description>
      NONE: <no description>
      BASIC: <no description>
      COMPLETE: <no description>
    """
    MANAGEMENT_UNSPECIFIED = 0
    NONE = 1
    BASIC = 2
    COMPLETE = 3

  class AllowedEncryptionStatusesValueListEntryValuesEnum(_messages.Enum):
    r"""AllowedEncryptionStatusesValueListEntryValuesEnum enum type.

    Values:
      ENCRYPTION_UNSPECIFIED: <no description>
      ENCRYPTION_UNSUPPORTED: <no description>
      UNENCRYPTED: <no description>
      ENCRYPTED: <no description>
    """
    ENCRYPTION_UNSPECIFIED = 0
    ENCRYPTION_UNSUPPORTED = 1
    UNENCRYPTED = 2
    ENCRYPTED = 3

  allowedDeviceManagementLevels = _messages.EnumField('AllowedDeviceManagementLevelsValueListEntryValuesEnum', 1, repeated=True)
  allowedEncryptionStatuses = _messages.EnumField('AllowedEncryptionStatusesValueListEntryValuesEnum', 2, repeated=True)
  osConstraints = _messages.MessageField('OsConstraint', 3, repeated=True)
  requireAdminApproval = _messages.BooleanField(4)
  requireCorpOwned = _messages.BooleanField(5)
  requireScreenlock = _messages.BooleanField(6)


class ListAccessLevelsResponse(_messages.Message):
  r"""A response to `ListAccessLevelsRequest`.

  Fields:
    accessLevels: List of the Access Level instances.
    nextPageToken: The pagination token to retrieve the next page of results.
      If the value is empty, no further results remain.
  """

  accessLevels = _messages.MessageField('AccessLevel', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListAccessPoliciesResponse(_messages.Message):
  r"""A response to `ListAccessPoliciesRequest`.

  Fields:
    accessPolicies: List of the AccessPolicy instances.
    nextPageToken: The pagination token to retrieve the next page of results.
      If the value is empty, no further results remain.
  """

  accessPolicies = _messages.MessageField('AccessPolicy', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListServicePerimetersResponse(_messages.Message):
  r"""A response to `ListServicePerimetersRequest`.

  Fields:
    nextPageToken: The pagination token to retrieve the next page of results.
      If the value is empty, no further results remain.
    servicePerimeters: List of the Service Perimeter instances.
  """

  nextPageToken = _messages.StringField(1)
  servicePerimeters = _messages.MessageField('ServicePerimeter', 2, repeated=True)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OsConstraint(_messages.Message):
  r"""A restriction on the OS type and version of devices making requests.

  Enums:
    OsTypeValueValuesEnum: Required. The allowed OS type.

  Fields:
    minimumVersion: The minimum allowed OS version. If not set, any version of
      this OS satisfies the constraint. Format: `"major.minor.patch"`.
      Examples: `"10.5.301"`, `"9.2.1"`.
    osType: Required. The allowed OS type.
    requireVerifiedChromeOs: Only allows requests from devices with a verified
      Chrome OS. Verifications includes requirements that the device is
      enterprise-managed, conformant to domain policies, and the caller has
      permission to call the API targeted by the request.
  """

  class OsTypeValueValuesEnum(_messages.Enum):
    r"""Required. The allowed OS type.

    Values:
      OS_UNSPECIFIED: The operating system of the device is not specified or
        not known.
      DESKTOP_MAC: A desktop Mac operating system.
      DESKTOP_WINDOWS: A desktop Windows operating system.
      DESKTOP_LINUX: A desktop Linux operating system.
      DESKTOP_CHROME_OS: A desktop ChromeOS operating system.
    """
    OS_UNSPECIFIED = 0
    DESKTOP_MAC = 1
    DESKTOP_WINDOWS = 2
    DESKTOP_LINUX = 3
    DESKTOP_CHROME_OS = 4

  minimumVersion = _messages.StringField(1)
  osType = _messages.EnumField('OsTypeValueValuesEnum', 2)
  requireVerifiedChromeOs = _messages.BooleanField(3)


class ServicePerimeter(_messages.Message):
  r"""`ServicePerimeter` describes a set of GCP resources which can freely
  import and export data amongst themselves, but not export outside of the
  `ServicePerimeter`. If a request with a source within this
  `ServicePerimeter` has a target outside of the `ServicePerimeter`, the
  request will be blocked. Otherwise the request is allowed. There are two
  types of Service Perimeter - Regular and Bridge. Regular Service Perimeters
  cannot overlap, a single GCP project can only belong to a single regular
  Service Perimeter. Service Perimeter Bridges can contain only GCP projects
  as members, a single GCP project may belong to multiple Service Perimeter
  Bridges.

  Enums:
    PerimeterTypeValueValuesEnum: Perimeter type indicator. A single project
      is allowed to be a member of single regular perimeter, but multiple
      service perimeter bridges. A project cannot be a included in a perimeter
      bridge without being included in regular perimeter. For perimeter
      bridges, the restricted service list as well as access level lists must
      be empty.

  Fields:
    createTime: Output only. Time the `ServicePerimeter` was created in UTC.
    description: Description of the `ServicePerimeter` and its use. Does not
      affect behavior.
    name: Required. Resource name for the ServicePerimeter.  The `short_name`
      component must begin with a letter and only include alphanumeric and
      '_'. Format: `accessPolicies/{policy_id}/servicePerimeters/{short_name}`
    perimeterType: Perimeter type indicator. A single project is allowed to be
      a member of single regular perimeter, but multiple service perimeter
      bridges. A project cannot be a included in a perimeter bridge without
      being included in regular perimeter. For perimeter bridges, the
      restricted service list as well as access level lists must be empty.
    status: Current ServicePerimeter configuration. Specifies sets of
      resources, restricted services and access levels that determine
      perimeter content and boundaries.
    title: Human readable title. Must be unique within the Policy.
    updateTime: Output only. Time the `ServicePerimeter` was updated in UTC.
  """

  class PerimeterTypeValueValuesEnum(_messages.Enum):
    r"""Perimeter type indicator. A single project is allowed to be a member
    of single regular perimeter, but multiple service perimeter bridges. A
    project cannot be a included in a perimeter bridge without being included
    in regular perimeter. For perimeter bridges, the restricted service list
    as well as access level lists must be empty.

    Values:
      PERIMETER_TYPE_REGULAR: Regular Perimeter.
      PERIMETER_TYPE_BRIDGE: Perimeter Bridge.
    """
    PERIMETER_TYPE_REGULAR = 0
    PERIMETER_TYPE_BRIDGE = 1

  createTime = _messages.StringField(1)
  description = _messages.StringField(2)
  name = _messages.StringField(3)
  perimeterType = _messages.EnumField('PerimeterTypeValueValuesEnum', 4)
  status = _messages.MessageField('ServicePerimeterConfig', 5)
  title = _messages.StringField(6)
  updateTime = _messages.StringField(7)


class ServicePerimeterConfig(_messages.Message):
  r"""`ServicePerimeterConfig` specifies a set of GCP resources that describe
  specific Service Perimeter configuration.

  Fields:
    accessLevels: A list of `AccessLevel` resource names that allow resources
      within the `ServicePerimeter` to be accessed from the internet.
      `AccessLevels` listed must be in the same policy as this
      `ServicePerimeter`. Referencing a nonexistent `AccessLevel` is a syntax
      error. If no `AccessLevel` names are listed, resources within the
      perimeter can only be accessed via GCP calls with request origins within
      the perimeter. Example:
      `"accessPolicies/MY_POLICY/accessLevels/MY_LEVEL"`. For Service
      Perimeter Bridge, must be empty.
    resources: A list of GCP resources that are inside of the service
      perimeter. Currently only projects are allowed. Format:
      `projects/{project_number}`
    restrictedServices: GCP services that are subject to the Service Perimeter
      restrictions. For example, if `storage.googleapis.com` is specified,
      access to the storage buckets inside the perimeter must meet the
      perimeter's access restrictions.
  """

  accessLevels = _messages.StringField(1, repeated=True)
  resources = _messages.StringField(2, repeated=True)
  restrictedServices = _messages.StringField(3, repeated=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
