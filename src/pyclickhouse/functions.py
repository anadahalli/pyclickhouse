from typing import Any, Callable

from pyclickhouse import Function


def to_args(args: dict[str, Any]) -> list[Any]:
    return [v for v in args.values() if v is not None]


class FunctionWrapper:
    """Auto generated ClickHouse functions."""

    # fallback for undefined functions
    def __getattr__(self, name: str) -> Callable[..., Function]:
        def wrapper(*args: Any) -> Function:
            return Function(name, *args)

        return wrapper
    
    @staticmethod
    def BLAKE3(message: Any) -> Function:
        """
        BLAKE3(message)

        Args:
        - `message` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the 32-byte BLAKE3 hash of the input string as a fixed-length string. [`FixedString(32)`](/sql-reference/data-types/fixedstring)
        """
        return Function("BLAKE3", *to_args(locals()))
    
    @staticmethod
    def CAST(x: Any, T: Any) -> Function:
        """
        CAST(x, T)
        or CAST(x AS T)
        or x::T

        Args:
        - `x` — A value of any type. [`Any`](/sql-reference/data-types)
        - `T` — The target data type. [`String`](/sql-reference/data-types/string)

        Returns the converted value with the target data type. [`Any`](/sql-reference/data-types)
        """
        return Function("CAST", *to_args(locals()))
    
    @staticmethod
    def CRC32(s: Any) -> Function:
        """
        CRC32(s)

        Args:
        - `s` — String to calculate CRC32 for. [`String`](/sql-reference/data-types/string)

        Returns the CRC32 checksum of the string. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("CRC32", *to_args(locals()))
    
    @staticmethod
    def CRC32IEEE(s: Any) -> Function:
        """
        CRC32IEEE(s)

        Args:
        - `s` — String to calculate CRC32 for. [`String`](/sql-reference/data-types/string)

        Returns the CRC32 checksum of the string. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("CRC32IEEE", *to_args(locals()))
    
    @staticmethod
    def CRC64(s: Any) -> Function:
        """
        CRC64(s)

        Args:
        - `s` — String to calculate CRC64 for. [`String`](/sql-reference/data-types/string)

        Returns the CRC64 checksum of the string. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("CRC64", *to_args(locals()))
    
    @staticmethod
    def DATE(expr: Any) -> Function:
        """
        DATE(expr)

        Args:
        - `expr` — The value to convert. [`String`](/sql-reference/data-types/string) or [`UInt32`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns a Date value. [`Date`](/sql-reference/data-types/date)
        """
        return Function("DATE", *to_args(locals()))
    
    @staticmethod
    def FQDN() -> Function:
        """
        FQDN()

        
        Returns the fully qualified domain name of the ClickHouse server. [`String`](/sql-reference/data-types/string)
        """
        return Function("FQDN", *to_args(locals()))
    
    @staticmethod
    def HMAC(mode: Any, message: Any, key: Any) -> Function:
        """
        HMAC(mode, message, key)

        Args:
        - `mode` — Hash algorithm name (case-insensitive). Supported: md5, sha1, sha224, sha256, sha384, sha512. [`String`](/sql-reference/data-types/string)
        - `message` — Message to be authenticated. [`String`](/sql-reference/data-types/string)
        - `key` — Secret key for HMAC. [`String`](/sql-reference/data-types/string)

        Returns a binary string containing the HMAC digest. [`String`](/sql-reference/data-types/string)
        """
        return Function("HMAC", *to_args(locals()))
    
    @staticmethod
    def IPv4CIDRToRange(ipv4: Any, cidr: Any) -> Function:
        """
        IPv4CIDRToRange(ipv4, cidr)

        Args:
        - `ipv4` — IPv4 address. [`IPv4`](/sql-reference/data-types/ipv4) or [`String`](/sql-reference/data-types/string)
        - `cidr` — CIDR value. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two IPv4 addresses representing the subnet range. [`Tuple(IPv4, IPv4)`](/sql-reference/data-types/tuple)
        """
        return Function("IPv4CIDRToRange", *to_args(locals()))
    
    @staticmethod
    def IPv4NumToString(num: Any) -> Function:
        """
        IPv4NumToString(num)

        Args:
        - `num` — IPv4 address as UInt32 number. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns a number representing the MAC address, or `0` if the format is invalid. [`String`](/sql-reference/data-types/string)
        """
        return Function("IPv4NumToString", *to_args(locals()))
    
    @staticmethod
    def IPv4NumToStringClassC(num: Any) -> Function:
        """
        IPv4NumToStringClassC(num)

        Args:
        - `num` — IPv4 address as UInt32 number. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns the IPv4 address string with xxx replacing the last octet. [`String`](/sql-reference/data-types/string)
        """
        return Function("IPv4NumToStringClassC", *to_args(locals()))
    
    @staticmethod
    def IPv4StringToNum(string: Any) -> Function:
        """
        IPv4StringToNum(string)

        Args:
        - `string` — IPv4 address string. [`String`](/sql-reference/data-types/string)

        Returns theIPv4 address. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("IPv4StringToNum", *to_args(locals()))
    
    @staticmethod
    def IPv4StringToNumOrDefault(string: Any) -> Function:
        """
        IPv4StringToNumOrDefault(string)

        Args:
        - `string` — IPv4 address string. [`String`](/sql-reference/data-types/string)

        Returns the IPv4 address, or `0` if invalid. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("IPv4StringToNumOrDefault", *to_args(locals()))
    
    @staticmethod
    def IPv4StringToNumOrNull(string: Any) -> Function:
        """
        IPv4StringToNumOrNull(string)

        Args:
        - `string` — IPv4 address string. [`String`](/sql-reference/data-types/string)

        Returns the IPv4 address, or `NULL` if invalid. [`Nullable(UInt32)`](/sql-reference/data-types/nullable)
        """
        return Function("IPv4StringToNumOrNull", *to_args(locals()))
    
    @staticmethod
    def IPv4ToIPv6(x: Any) -> Function:
        """
        IPv4ToIPv6(x)

        Args:
        - `x` — IPv4 address. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns an IPv6 address in binary format. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("IPv4ToIPv6", *to_args(locals()))
    
    @staticmethod
    def IPv6CIDRToRange(ipv6: Any, cidr: Any) -> Function:
        """
        IPv6CIDRToRange(ipv6, cidr)

        Args:
        - `ipv6` — IPv6 address. [`IPv6`](/sql-reference/data-types/ipv6) or [`String`](/sql-reference/data-types/string)
        - `cidr` — CIDR value. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two IPv6 addresses representing the subnet range. [`Tuple(IPv6, IPv6)`](/sql-reference/data-types/tuple)
        """
        return Function("IPv6CIDRToRange", *to_args(locals()))
    
    @staticmethod
    def IPv6NumToString(x: Any) -> Function:
        """
        IPv6NumToString(x)

        Args:
        - `x` — IPv6 address in binary format. [`FixedString(16)`](/sql-reference/data-types/fixedstring) or [`IPv6`](/sql-reference/data-types/ipv6)

        Returns the IPv6 address string in text format. [`String`](/sql-reference/data-types/string)
        """
        return Function("IPv6NumToString", *to_args(locals()))
    
    @staticmethod
    def IPv6StringToNum(string: Any) -> Function:
        """
        IPv6StringToNum(string)

        Args:
        - `string` — IPv6 address string. [`String`](/sql-reference/data-types/string)

        Returns theIPv6 address in binary format. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("IPv6StringToNum", *to_args(locals()))
    
    @staticmethod
    def IPv6StringToNumOrDefault(string: Any) -> Function:
        """
        IPv6StringToNumOrDefault(string)

        Args:
        - `string` — IPv6 address string. [`String`](/sql-reference/data-types/string)

        IPv6 address in binary format, or zero-filled FixedString(16) if invalid. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("IPv6StringToNumOrDefault", *to_args(locals()))
    
    @staticmethod
    def IPv6StringToNumOrNull(string: Any) -> Function:
        """
        IPv6StringToNumOrNull(string)

        Args:
        - `string` — IPv6 address string. [`String`](/sql-reference/data-types/string)

        Returns IPv6 address in binary format, or `NULL` if invalid. [`Nullable(FixedString(16))`](/sql-reference/data-types/nullable)
        """
        return Function("IPv6StringToNumOrNull", *to_args(locals()))
    
    @staticmethod
    def JSONAllPaths(json: Any) -> Function:
        """
        JSONAllPaths(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns an array of all paths in the JSON column. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONAllPaths", *to_args(locals()))
    
    @staticmethod
    def JSONAllPathsWithTypes(json: Any) -> Function:
        """
        JSONAllPathsWithTypes(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns a map of all paths and their data types in the JSON column. [`Map(String, String)`](/sql-reference/data-types/map)
        """
        return Function("JSONAllPathsWithTypes", *to_args(locals()))
    
    @staticmethod
    def JSONArrayLength(json: Any) -> Function:
        """
        JSONArrayLength(json)

        Args:
        - `json` — String with valid JSON. [`String`](/sql-reference/data-types/string)

        Returns the number of array elements if `json` is a valid JSON array string, otherwise returns `NULL`. [`Nullable(UInt64)`](/sql-reference/data-types/nullable)
        """
        return Function("JSONArrayLength", *to_args(locals()))
    
    @staticmethod
    def JSONDynamicPaths(json: Any) -> Function:
        """
        JSONDynamicPaths(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns an array of dynamic paths in the JSON column. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONDynamicPaths", *to_args(locals()))
    
    @staticmethod
    def JSONDynamicPathsWithTypes(json: Any) -> Function:
        """
        JSONDynamicPathsWithTypes(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns a map of dynamic paths and their data types in the JSON column. [`Map(String, String)`](/sql-reference/data-types/map)
        """
        return Function("JSONDynamicPathsWithTypes", *to_args(locals()))
    
    @staticmethod
    def JSONExtract(json: Any, indices_or_keys: Any | None = None, return_type: Any | None = None) -> Function:
        """
        JSONExtract(json[, indices_or_keys, ...], return_type)

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `return_type` — ClickHouse data type to return. [`String`](/sql-reference/data-types/string)

        Returns a value of specified ClickHouse data type if possible, otherwise returns the default value for that type.
        """
        return Function("JSONExtract", *to_args(locals()))
    
    @staticmethod
    def JSONExtractArrayRaw(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractArrayRaw(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of strings with JSON array elements. If the part is not an array or does not exist, an empty array will be returned. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractArrayRaw", *to_args(locals()))
    
    @staticmethod
    def JSONExtractArrayRawCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractArrayRawCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the array. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of raw JSON strings. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractArrayRawCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractBool(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractBool(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a Bool value if it exists, otherwise returns `0`. [`Bool`](/sql-reference/data-types/boolean)
        """
        return Function("JSONExtractBool", *to_args(locals()))
    
    @staticmethod
    def JSONExtractBoolCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractBoolCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the extracted boolean value (1 for true, 0 for false), 0 if not found. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONExtractBoolCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractCaseInsensitive(json: Any, indices_or_keys: Any | None = None, return_type: Any | None = None) -> Function:
        """
        JSONExtractCaseInsensitive(json [, indices_or_keys...], return_type)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `return_type` — The ClickHouse data type to extract [`String`](/sql-reference/data-types/string)

        Returns the extracted value in the specified data type. [`Any`](/sql-reference/data-types)
        """
        return Function("JSONExtractCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractFloat(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractFloat(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a Float value if it exists, otherwise returns `0`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("JSONExtractFloat", *to_args(locals()))
    
    @staticmethod
    def JSONExtractFloatCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractFloatCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the extracted Float value, 0 if not found or cannot be converted. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("JSONExtractFloatCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractInt(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractInt(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an Int value if it exists, otherwise returns `0`. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONExtractInt", *to_args(locals()))
    
    @staticmethod
    def JSONExtractIntCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractIntCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the extracted Int value, 0 if not found or cannot be converted. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONExtractIntCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractKeys(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractKeys(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array with the keys of the JSON object. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractKeys", *to_args(locals()))
    
    @staticmethod
    def JSONExtractKeysAndValues(json: Any, indices_or_keys: Any | None = None, value_type: Any | None = None) -> Function:
        """
        JSONExtractKeysAndValues(json[, indices_or_keys, ...], value_type)

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `value_type` — ClickHouse data type of the values. [`String`](/sql-reference/data-types/string)

        Returns an array of tuples with the parsed key-value pairs. [`Array(Tuple(String, value_type))`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractKeysAndValues", *to_args(locals()))
    
    @staticmethod
    def JSONExtractKeysAndValuesCaseInsensitive(json: Any, indices_or_keys: Any | None = None, value_type: Any | None = None) -> Function:
        """
        JSONExtractKeysAndValuesCaseInsensitive(json [, indices_or_keys...], value_type)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the object. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `value_type` — The ClickHouse data type of the values [`String`](/sql-reference/data-types/string)

        Returns an array of tuples containing key-value pairs. [`Array(Tuple(String, T))`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractKeysAndValuesCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractKeysAndValuesRaw(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractKeysAndValuesRaw(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of tuples with parsed key-value pairs where values are unparsed strings. [`Array(Tuple(String, String))`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractKeysAndValuesRaw", *to_args(locals()))
    
    @staticmethod
    def JSONExtractKeysAndValuesRawCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractKeysAndValuesRawCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the object. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of tuples containing key-value pairs as raw strings. [`Array(Tuple(String, String))`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractKeysAndValuesRawCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractKeysCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractKeysCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the object. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of keys from the JSON object. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONExtractKeysCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractRaw(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractRaw(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the part of JSON as an unparsed string. If the part does not exist or has a wrong type, an empty string will be returned. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSONExtractRaw", *to_args(locals()))
    
    @staticmethod
    def JSONExtractRawCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractRawCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the raw JSON string of the extracted element. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSONExtractRawCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractString(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractString(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a String value if it exists, otherwise returns an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSONExtractString", *to_args(locals()))
    
    @staticmethod
    def JSONExtractStringCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractStringCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the extracted string value, empty string if not found. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSONExtractStringCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONExtractUInt(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractUInt(json [, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — A list of zero or more arguments each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a UInt value if it exists, otherwise returns `0`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONExtractUInt", *to_args(locals()))
    
    @staticmethod
    def JSONExtractUIntCaseInsensitive(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONExtractUIntCaseInsensitive(json [, indices_or_keys]...)

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional. Indices or keys to navigate to the field. Keys use case-insensitive matching [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the extracted UInt value, 0 if not found or cannot be converted. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONExtractUIntCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def JSONHas(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONHas(json[ ,indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `[ ,indices_or_keys, ...]` — A list of zero or more arguments. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns `1` if the value exists in `json`, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONHas", *to_args(locals()))
    
    @staticmethod
    def JSONKey(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONKey(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse. [`String`](/sql-reference/data-types/string)
        - `indices_or_keys` — Optional list of indices or keys specifying a path to a nested element. Each argument can be either a string (access by key) or an integer (access by index starting from 1). [`String`](/sql-reference/data-types/string) or [`Int*`](/sql-reference/data-types/int-uint)

        Returns the key name at the specified position in the JSON object. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSONKey", *to_args(locals()))
    
    @staticmethod
    def JSONLength(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONLength(json [, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `[, indices_or_keys, ...]` — Optional. A list of zero or more arguments. [`String`](/sql-reference/data-types/string) or [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the length of the JSON array or JSON object, otherwise returns `0` if the value does not exist or has the wrong type. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("JSONLength", *to_args(locals()))
    
    @staticmethod
    def JSONMergePatch(json1: Any, json2: Any | None = None) -> Function:
        """
        JSONMergePatch(json1[, json2, ...])

        Args:
        - `json1[, json2, ...]` — One or more strings with valid JSON. [`String`](/sql-reference/data-types/string)

        Returns the merged JSON object string, if the JSON object strings are valid. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSONMergePatch", *to_args(locals()))
    
    @staticmethod
    def JSONSharedDataPaths(json: Any) -> Function:
        """
        JSONSharedDataPaths(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns an array of paths stored in shared data structure in the JSON column. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("JSONSharedDataPaths", *to_args(locals()))
    
    @staticmethod
    def JSONSharedDataPathsWithTypes(json: Any) -> Function:
        """
        JSONSharedDataPathsWithTypes(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns a map of paths stored in shared data structure and their data types in the JSON column. [`Map(String, String)`](/sql-reference/data-types/map)
        """
        return Function("JSONSharedDataPathsWithTypes", *to_args(locals()))
    
    @staticmethod
    def JSONType(json: Any, indices_or_keys: Any | None = None) -> Function:
        """
        JSONType(json[, indices_or_keys, ...])

        Args:
        - `json` — JSON string to parse [`String`](/sql-reference/data-types/string)
        - `json[, indices_or_keys, ...]` — A list of zero or more arguments, each of which can be either string or integer. [`String`](/sql-reference/data-types/string) or [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the type of a JSON value as a string, otherwise if the value doesn't exist it returns `Null=0` [`Enum`](/sql-reference/data-types/enum)
        """
        return Function("JSONType", *to_args(locals()))
    
    @staticmethod
    def JSON_EXISTS(json: Any, path: Any) -> Function:
        """
        JSON_EXISTS(json, path)

        Args:
        - `json` — A string with valid JSON. [`String`](/sql-reference/data-types/string)
        - `path` — A string representing the path. [`String`](/sql-reference/data-types/string)

        Returns `1` if the value exists in the JSON document, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("JSON_EXISTS", *to_args(locals()))
    
    @staticmethod
    def JSON_QUERY(json: Any, path: Any) -> Function:
        """
        JSON_QUERY(json, path)

        Args:
        - `json` — A string with valid JSON. [`String`](/sql-reference/data-types/string)
        - `path` — A string representing the path. [`String`](/sql-reference/data-types/string)

        Returns the extracted JSON array or JSON object as a string, or an empty string if the value does not exist. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSON_QUERY", *to_args(locals()))
    
    @staticmethod
    def JSON_VALUE(json: Any, path: Any) -> Function:
        """
        JSON_VALUE(json, path)

        Args:
        - `json` — A string with valid JSON. [`String`](/sql-reference/data-types/string)
        - `path` — A string representing the path. [`String`](/sql-reference/data-types/string)

        Returns the extracted JSON scalar as a string, or an empty string if the value does not exist. [`String`](/sql-reference/data-types/string)
        """
        return Function("JSON_VALUE", *to_args(locals()))
    
    @staticmethod
    def L1Distance(vector1: Any, vector2: Any) -> Function:
        """
        L1Distance(vector1, vector2)

        Args:
        - `vector1` — First vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `vector2` — Second vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the 1-norm distance. [`UInt32`](/sql-reference/data-types/int-uint) or [`Float64`](/sql-reference/data-types/float)
        """
        return Function("L1Distance", *to_args(locals()))
    
    @staticmethod
    def L1Norm(vector: Any) -> Function:
        """
        L1Norm(vector)

        Args:
        - `vector` — Vector or tuple of numeric values. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the L1-norm or [taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry) distance. [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        """
        return Function("L1Norm", *to_args(locals()))
    
    @staticmethod
    def L1Normalize(tuple: Any) -> Function:
        """
        L1Normalize(tuple)

        Args:
        - `tuple` — A tuple of numeric values. [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the unit vector. [`Tuple(Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("L1Normalize", *to_args(locals()))
    
    @staticmethod
    def L2Distance(vector1: Any, vector2: Any) -> Function:
        """
        L2Distance(vector1, vector2)

        Args:
        - `vector1` — First vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `vector2` — Second vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the 2-norm distance. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("L2Distance", *to_args(locals()))
    
    @staticmethod
    def L2DistanceTransposed(vector1: Any, vector2: Any, p: Any) -> Function:
        """
        L2DistanceTransposed(vector1, vector2, p)

        Args:
        - `vectors` — Vectors. [`QBit(T, UInt64)`](/sql-reference/data-types/qbit)
        - `reference` — Reference vector. [`Array(T)`](/sql-reference/data-types/array)
        - `p` — Number of bits from each vector element to use in the distance calculation (1 to element bit-width). The quantization level controls the precision-speed trade-off. Using fewer bits results in faster I/O and calculations with reduced accuracy, while using more bits increases accuracy at the cost of performance. [`UInt`](/sql-reference/data-types/int-uint)

        Returns the approximate 2-norm distance. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("L2DistanceTransposed", *to_args(locals()))
    
    @staticmethod
    def L2Norm(vector: Any) -> Function:
        """
        L2Norm(vector)

        Args:
        - `vector` — Vector or tuple of numeric values. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the L2-norm or [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance). [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("L2Norm", *to_args(locals()))
    
    @staticmethod
    def L2Normalize(tuple: Any) -> Function:
        """
        L2Normalize(tuple)

        Args:
        - `tuple` — A tuple of numeric values. [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the unit vector. [`Tuple(Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("L2Normalize", *to_args(locals()))
    
    @staticmethod
    def L2SquaredDistance(vector1: Any, vector2: Any) -> Function:
        """
        L2SquaredDistance(vector1, vector2)

        Args:
        - `vector1` — First vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `vector2` — Second vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the sum of the squares of the difference between the corresponding elements of two vectors. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("L2SquaredDistance", *to_args(locals()))
    
    @staticmethod
    def L2SquaredNorm(vector: Any) -> Function:
        """
        L2SquaredNorm(vector)

        Args:
        - `vector` — Vector or tuple of numeric values. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the L2-norm squared. [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        """
        return Function("L2SquaredNorm", *to_args(locals()))
    
    @staticmethod
    def LinfDistance(vector1: Any, vector2: Any) -> Function:
        """
        LinfDistance(vector1, vector2)

        Args:
        - `vector1` — First vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `vector2` — Second vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the Infinity-norm distance. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("LinfDistance", *to_args(locals()))
    
    @staticmethod
    def LinfNorm(vector: Any) -> Function:
        """
        LinfNorm(vector)

        Args:
        - `vector` — Vector or tuple of numeric values. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the Linf-norm or the maximum absolute value. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("LinfNorm", *to_args(locals()))
    
    @staticmethod
    def LinfNormalize(tuple: Any) -> Function:
        """
        LinfNormalize(tuple)

        Args:
        - `tuple` — A tuple of numeric values. [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the unit vector. [`Tuple(Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("LinfNormalize", *to_args(locals()))
    
    @staticmethod
    def LpDistance(vector1: Any, vector2: Any, p: Any) -> Function:
        """
        LpDistance(vector1, vector2, p)

        Args:
        - `vector1` — First vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `vector2` — Second vector. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `p` — The power. Possible values: real number from `[1; inf)`. [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the p-norm distance. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("LpDistance", *to_args(locals()))
    
    @staticmethod
    def LpNorm(vector: Any, p: Any) -> Function:
        """
        LpNorm(vector, p)

        Args:
        - `vector` — Vector or tuple of numeric values. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `p` — The power. Possible values are real numbers in the range `[1; inf)`. [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the [Lp-norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#p-norm). [`Float64`](/sql-reference/data-types/float)
        """
        return Function("LpNorm", *to_args(locals()))
    
    @staticmethod
    def LpNormalize(tuple: Any, p: Any) -> Function:
        """
        LpNormalize(tuple, p)

        Args:
        - `tuple` — A tuple of numeric values. [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `p` — The power. Possible values are any number in the range range from `[1; inf)`. [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the unit vector. [`Tuple(Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("LpNormalize", *to_args(locals()))
    
    @staticmethod
    def MACNumToString(num: Any) -> Function:
        """
        MACNumToString(num)

        Args:
        - `num` — UInt64 number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a MAC address in format AA:BB:CC:DD:EE:FF. [`String`](/sql-reference/data-types/string)
        """
        return Function("MACNumToString", *to_args(locals()))
    
    @staticmethod
    def MACStringToNum(s: Any) -> Function:
        """
        MACStringToNum(s)

        Args:
        - `s` — MAC address string. [`String`](/sql-reference/data-types/string)

        Returns a UInt64 number. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("MACStringToNum", *to_args(locals()))
    
    @staticmethod
    def MACStringToOUI(s: Any) -> Function:
        """
        MACStringToOUI(s)

        Args:
        - `s` — MAC address string. [`String`](/sql-reference/data-types/string)

        First three octets as UInt64 number. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("MACStringToOUI", *to_args(locals()))
    
    @staticmethod
    def MD4(s: Any) -> Function:
        """
        MD4(s)

        Args:
        - `s` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the MD4 hash of the given input string as a fixed-length string. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("MD4", *to_args(locals()))
    
    @staticmethod
    def MD5(s: Any) -> Function:
        """
        MD5(s)

        Args:
        - `s` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the MD5 hash of the given input string as a fixed-length string. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("MD5", *to_args(locals()))
    
    @staticmethod
    def RIPEMD160(s: Any) -> Function:
        """
        RIPEMD160(s)

        Args:
        - `s` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the RIPEMD160 hash of the given input string as a fixed-length string. [`FixedString(20)`](/sql-reference/data-types/fixedstring)
        """
        return Function("RIPEMD160", *to_args(locals()))
    
    @staticmethod
    def SHA1(s: Any) -> Function:
        """
        SHA1(s)

        Args:
        - `s` — The input string to hash [`String`](/sql-reference/data-types/string)

        Returns the SHA1 hash of the given input string as a fixed-length string. [`FixedString(20)`](/sql-reference/data-types/fixedstring)
        """
        return Function("SHA1", *to_args(locals()))
    
    @staticmethod
    def SHA224(s: Any) -> Function:
        """
        SHA224(s)

        Args:
        - `s` — The input value to hash. [`String`](/sql-reference/data-types/string)

        Returns the SHA224 hash of the given input string as a fixed-length string. [`FixedString(28)`](/sql-reference/data-types/fixedstring)
        """
        return Function("SHA224", *to_args(locals()))
    
    @staticmethod
    def SHA256(s: Any) -> Function:
        """
        SHA256(s)

        Args:
        - `s` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the SHA256 hash of the given input string as a fixed-length string. [`FixedString(32)`](/sql-reference/data-types/fixedstring)
        """
        return Function("SHA256", *to_args(locals()))
    
    @staticmethod
    def SHA384(s: Any) -> Function:
        """
        SHA384(s)

        Args:
        - `s` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the SHA384 hash of the given input string as a fixed-length string. [`FixedString(48)`](/sql-reference/data-types/fixedstring)
        """
        return Function("SHA384", *to_args(locals()))
    
    @staticmethod
    def SHA512(s: Any) -> Function:
        """
        SHA512(s)

        Args:
        - `s` — The input string to hash [`String`](/sql-reference/data-types/string)

        Returns the SHA512 hash of the given input string as a fixed-length string. [`FixedString(64)`](/sql-reference/data-types/fixedstring)
        """
        return Function("SHA512", *to_args(locals()))
    
    @staticmethod
    def SHA512_256(s: Any) -> Function:
        """
        SHA512_256(s)

        Args:
        - `s` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the SHA512_256 hash of the given input string as a fixed-length string. [`FixedString(32)`](/sql-reference/data-types/fixedstring)
        """
        return Function("SHA512_256", *to_args(locals()))
    
    @staticmethod
    def ULIDStringToDateTime(ulid: Any, timezone: Any | None = None) -> Function:
        """
        ULIDStringToDateTime(ulid[, timezone])

        Args:
        - `ulid` — Input ULID. [`String`](/sql-reference/data-types/string) or [`FixedString(26)`](/sql-reference/data-types/fixedstring)
        - `timezone` — Optional. Timezone name for the returned value. [`String`](/sql-reference/data-types/string)

        Timestamp with milliseconds precision. [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("ULIDStringToDateTime", *to_args(locals()))
    
    @staticmethod
    def URLHash(url: Any, N: Any | None = None) -> Function:
        """
        URLHash(url[, N])

        Args:
        - `url` — URL string to hash. [`String`](/sql-reference/data-types/string)
        - `N` — Optional. Level in the URL hierarchy. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the computed hash value of `url`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("URLHash", *to_args(locals()))
    
    @staticmethod
    def URLHierarchy(url: Any) -> Function:
        """
        URLHierarchy(url)

        Args:
        - `url` — The URL to process. [`String`](/sql-reference/data-types/string)

        Returns an array of progressively longer URLs forming a hierarchy. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("URLHierarchy", *to_args(locals()))
    
    @staticmethod
    def URLPathHierarchy(url: Any) -> Function:
        """
        URLPathHierarchy(url)

        Args:
        - `url` — The URL to process. [`String`](/sql-reference/data-types/string)

        Returns an array of progressively longer URL path components forming a hierarchy. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("URLPathHierarchy", *to_args(locals()))
    
    @staticmethod
    def UTCTimestamp() -> Function:
        """
        UTCTimestamp()

        
        Returns the current date and time at the moment of query analysis. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("UTCTimestamp", *to_args(locals()))
    
    @staticmethod
    def UUIDNumToString(binary: Any, variant: Any | None = None) -> Function:
        """
        UUIDNumToString(binary[, variant])

        Args:
        - `binary` — Binary representation of a UUID. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        - `variant` — Variant as specified by [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122#section-4.1.1). 1 = `Big-endian` (default), 2 = `Microsoft`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the UUID as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("UUIDNumToString", *to_args(locals()))
    
    @staticmethod
    def UUIDStringToNum(string: Any, variant : Any | None =  1) -> Function:
        """
        UUIDStringToNum(string[, variant = 1])

        Args:
        - `string` — A string or fixed-string of 36 characters) [`String`](/sql-reference/data-types/string) or [`FixedString(36)`](/sql-reference/data-types/fixedstring)
        - `variant` — Variant as specified by [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122#section-4.1.1). 1 = `Big-endian` (default), 2 = `Microsoft`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the binary representation of `string`. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("UUIDStringToNum", *to_args(locals()))
    
    @staticmethod
    def UUIDToNum(uuid: Any, variant : Any | None =  1) -> Function:
        """
        UUIDToNum(uuid[, variant = 1])

        Args:
        - `uuid` — UUID. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `variant` — Variant as specified by [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122#section-4.1.1). 1 = `Big-endian` (default), 2 = `Microsoft`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a binary representation of the UUID. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("UUIDToNum", *to_args(locals()))
    
    @staticmethod
    def UUIDv7ToDateTime(uuid: Any, timezone: Any | None = None) -> Function:
        """
        UUIDv7ToDateTime(uuid[, timezone])

        Args:
        - `uuid` — A UUID version 7. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. [Timezone name](../../operations/server-configuration-parameters/settings.md#timezone) for the returned value. [`String`](/sql-reference/data-types/string)

        Returns a timestamp with milliseconds precision. If the UUID is not a valid version 7 UUID, it returns `1970-01-01 00:00:00.000`. [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("UUIDv7ToDateTime", *to_args(locals()))
    
    @staticmethod
    def YYYYMMDDToDate(YYYYMMDD: Any) -> Function:
        """
        YYYYMMDDToDate(YYYYMMDD)

        Args:
        - `YYYYMMDD` — Number containing the year, month and day. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a `Date` value from the provided arguments [`Date`](/sql-reference/data-types/date)
        """
        return Function("YYYYMMDDToDate", *to_args(locals()))
    
    @staticmethod
    def YYYYMMDDToDate32(YYYYMMDD: Any) -> Function:
        """
        YYYYMMDDToDate32(YYYYMMDD)

        Args:
        - `YYYYMMDD` — Number containing the year, month and day. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a `Date32` value from the provided arguments [`Date32`](/sql-reference/data-types/date32)
        """
        return Function("YYYYMMDDToDate32", *to_args(locals()))
    
    @staticmethod
    def YYYYMMDDhhmmssToDateTime(YYYYMMDDhhmmss: Any, timezone: Any | None = None) -> Function:
        """
        YYYYMMDDhhmmssToDateTime(YYYYMMDDhhmmss[, timezone])

        Args:
        - `YYYYMMDDhhmmss` — Number containing the year, month, day, hour, minute, and second. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `timezone` — Timezone name. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime` value from the provided arguments [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("YYYYMMDDhhmmssToDateTime", *to_args(locals()))
    
    @staticmethod
    def YYYYMMDDhhmmssToDateTime64(YYYYMMDDhhmmss: Any, precision: Any | None = None, timezone: Any | None = None) -> Function:
        """
        YYYYMMDDhhmmssToDateTime64(YYYYMMDDhhmmss[, precision[, timezone]])

        Args:
        - `YYYYMMDDhhmmss` — Number containing the year, month, day, hour, minute, and second. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `precision` — Precision for the fractional part (0-9). [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Timezone name. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime64` value from the provided arguments [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("YYYYMMDDhhmmssToDateTime64", *to_args(locals()))
    
    @staticmethod
    def abs(x: Any) -> Function:
        """
        abs(x)

        Args:
        - `x` — Value to get the absolute value of 
        The absolute value of `x`
        """
        return Function("abs", *to_args(locals()))
    
    @staticmethod
    def accurateCast(x: Any, T: Any) -> Function:
        """
        accurateCast(x, T)

        Args:
        - `x` — A value to convert. [`Any`](/sql-reference/data-types)
        - `T` — The target data type name. [`String`](/sql-reference/data-types/string)

        Returns the converted value with the target data type. [`Any`](/sql-reference/data-types)
        """
        return Function("accurateCast", *to_args(locals()))
    
    @staticmethod
    def accurateCastOrDefault(x: Any, T: Any, default_value: Any | None = None) -> Function:
        """
        accurateCastOrDefault(x, T[, default_value])

        Args:
        - `x` — A value to convert. [`Any`](/sql-reference/data-types)
        - `T` — The target data type name. [`const String`](/sql-reference/data-types/string)
        - `default_value` — Optional. Default value to return if conversion fails. [`Any`](/sql-reference/data-types)

        Returns the converted value with the target data type, or the default value if conversion is not possible. [`Any`](/sql-reference/data-types)
        """
        return Function("accurateCastOrDefault", *to_args(locals()))
    
    @staticmethod
    def accurateCastOrNull(x: Any, T: Any) -> Function:
        """
        accurateCastOrNull(x, T)

        Args:
        - `x` — A value to convert. [`Any`](/sql-reference/data-types)
        - `T` — The target data type name. [`String`](/sql-reference/data-types/string)

        Returns the converted value with the target data type, or `NULL` if conversion is not possible. [`Any`](/sql-reference/data-types)
        """
        return Function("accurateCastOrNull", *to_args(locals()))
    
    @staticmethod
    def acos(x: Any) -> Function:
        """
        acos(x)

        Args:
        - `x` — The value for which to find arc cosine of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the arc cosine of x [`Float*`](/sql-reference/data-types/float)
        """
        return Function("acos", *to_args(locals()))
    
    @staticmethod
    def acosh(x: Any) -> Function:
        """
        acosh(x)

        Args:
        - `x` — Hyperbolic cosine of angle. Values from the interval: `1 ≤ x < +∞`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the angle, in radians. Values from the interval: `0 ≤ acosh(x) < +∞`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("acosh", *to_args(locals()))
    
    @staticmethod
    def addDate(datetime: Any, interval: Any) -> Function:
        """
        addDate(datetime, interval)

        Args:
        - `datetime` — The date or date with time to which `interval` is added. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `interval` — Interval to add. [`Interval`](/sql-reference/data-types/int-uint)

        Returns date or date with time obtained by adding `interval` to `datetime`. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addDate", *to_args(locals()))
    
    @staticmethod
    def addDays(datetime: Any, num: Any) -> Function:
        """
        addDays(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of days to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of days to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` days. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addDays", *to_args(locals()))
    
    @staticmethod
    def addHours(datetime: Any, num: Any) -> Function:
        """
        addHours(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of hours to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of hours to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` hours [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("addHours", *to_args(locals()))
    
    @staticmethod
    def addInterval(interval_1: Any, interval_2: Any) -> Function:
        """
        addInterval(interval_1, interval_2)

        Args:
        - `interval_1` — First interval or tuple of intervals. [`Interval`](/sql-reference/data-types/int-uint) or [`Tuple(Interval)`](/sql-reference/data-types/tuple)
        - `interval_2` — Second interval to be added. [`Interval`](/sql-reference/data-types/int-uint)

        Returns a tuple of intervals [`Tuple(Interval)`](/sql-reference/data-types/tuple)
        """
        return Function("addInterval", *to_args(locals()))
    
    @staticmethod
    def addMicroseconds(datetime: Any, num: Any) -> Function:
        """
        addMicroseconds(datetime, num)

        Args:
        - `datetime` — Date with time to add specified number of microseconds to. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of microseconds to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `date_time` plus `num` microseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addMicroseconds", *to_args(locals()))
    
    @staticmethod
    def addMilliseconds(datetime: Any, num: Any) -> Function:
        """
        addMilliseconds(datetime, num)

        Args:
        - `datetime` — Date with time to add specified number of milliseconds to. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of milliseconds to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` milliseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addMilliseconds", *to_args(locals()))
    
    @staticmethod
    def addMinutes(datetime: Any, num: Any) -> Function:
        """
        addMinutes(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of minutes to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of minutes to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` minutes [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("addMinutes", *to_args(locals()))
    
    @staticmethod
    def addMonths(datetime: Any, num: Any) -> Function:
        """
        addMonths(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of months to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of months to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` months [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addMonths", *to_args(locals()))
    
    @staticmethod
    def addNanoseconds(datetime: Any, num: Any) -> Function:
        """
        addNanoseconds(datetime, num)

        Args:
        - `datetime` — Date with time to add specified number of nanoseconds to. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of nanoseconds to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` nanoseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addNanoseconds", *to_args(locals()))
    
    @staticmethod
    def addQuarters(datetime: Any, num: Any) -> Function:
        """
        addQuarters(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of quarters to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of quarters to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` quarters [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addQuarters", *to_args(locals()))
    
    @staticmethod
    def addSeconds(datetime: Any, num: Any) -> Function:
        """
        addSeconds(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of seconds to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of seconds to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` seconds [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("addSeconds", *to_args(locals()))
    
    @staticmethod
    def addTupleOfIntervals(datetime: Any, intervals: Any) -> Function:
        """
        addTupleOfIntervals(datetime, intervals)

        Args:
        - `datetime` — Date or date with time to add intervals to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `intervals` — Tuple of intervals to add to `datetime`. [`Tuple(Interval)`](/sql-reference/data-types/tuple)

        Returns `date` with added `intervals` [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addTupleOfIntervals", *to_args(locals()))
    
    @staticmethod
    def addWeeks(datetime: Any, num: Any) -> Function:
        """
        addWeeks(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of weeks to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of weeks to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` weeks [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addWeeks", *to_args(locals()))
    
    @staticmethod
    def addYears(datetime: Any, num: Any) -> Function:
        """
        addYears(datetime, num)

        Args:
        - `datetime` — Date or date with time to add specified number of years to. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of years to add. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` plus `num` years [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("addYears", *to_args(locals()))
    
    @staticmethod
    def addressToLine(address_of_binary_instruction: Any) -> Function:
        """
        addressToLine(address_of_binary_instruction)

        Args:
        - `address_of_binary_instruction` — Address of instruction in a running process. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a source code filename and line number delimited by a colon, for example, `/build/obj-x86_64-linux-gnu/../src/Common/ThreadPool.cpp:199`. Returns the name of a binary, if no debug information could be found, otherwise an empty string, if the address is not valid. [`String`](/sql-reference/data-types/string)
        """
        return Function("addressToLine", *to_args(locals()))
    
    @staticmethod
    def addressToLineWithInlines(address_of_binary_instruction: Any) -> Function:
        """
        addressToLineWithInlines(address_of_binary_instruction)

        Args:
        - `address_of_binary_instruction` — The address of an instruction in a running process. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array whose first element is the source code filename and line number delimited by a colon. The second, third, etc. element list inline functions' source code filenames, line numbers and function names. If no debug information could be found, then an array with a single element equal to the name of the binary is returned, otherwise an empty array is returned if the address is not valid. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("addressToLineWithInlines", *to_args(locals()))
    
    @staticmethod
    def addressToSymbol(address_of_binary_instruction: Any) -> Function:
        """
        addressToSymbol(address_of_binary_instruction)

        Args:
        - `address_of_binary_instruction` — Address of instruction in a running process. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the symbol from ClickHouse object files or an empty string, if the address is not valid. [`String`](/sql-reference/data-types/string)
        """
        return Function("addressToSymbol", *to_args(locals()))
    
    @staticmethod
    def aes_decrypt_mysql(mode: Any, ciphertext: Any, key: Any, iv: Any | None = None) -> Function:
        """
        aes_decrypt_mysql(mode, ciphertext, key[, iv])

        Args:
        - `mode` — Decryption mode. [`String`](/sql-reference/data-types/string)
        - `ciphertext` — Encrypted text that needs to be decrypted. [`String`](/sql-reference/data-types/string)
        - `key` — Decryption key. [`String`](/sql-reference/data-types/string)
        - `iv` — Optional. Initialization vector. [`String`](/sql-reference/data-types/string)

        Returns the decrypted String. [`String`](/sql-reference/data-types/string)
        """
        return Function("aes_decrypt_mysql", *to_args(locals()))
    
    @staticmethod
    def aes_encrypt_mysql(mode: Any, plaintext: Any, key: Any, iv: Any | None = None) -> Function:
        """
        aes_encrypt_mysql(mode, plaintext, key[, iv])

        Args:
        - `mode` — Encryption mode. [`String`](/sql-reference/data-types/string)
        - `plaintext` — Text that should be encrypted. [`String`](/sql-reference/data-types/string)
        - `key` — Encryption key. If the key is longer than required by `mode`, MySQL-specific key folding is performed. [`String`](/sql-reference/data-types/string)
        - `iv` — Optional. Initialization vector. Only the first 16 bytes are taken into account. [`String`](/sql-reference/data-types/string)

        Ciphertext binary string. [`String`](/sql-reference/data-types/string)
        """
        return Function("aes_encrypt_mysql", *to_args(locals()))
    
    @staticmethod
    def age(unit: Any, startdate: Any, enddate: Any, timezone: Any | None = None) -> Function:
        """
        age('unit', startdate, enddate[, timezone])

        Args:
        - `unit` — The type of interval for result.

        | Unit        | Possible values                          |
        |-------------|------------------------------------------|
        | nanosecond  | `nanosecond`, `nanoseconds`, `ns`        |
        | microsecond | `microsecond`, `microseconds`, `us`, `u` |
        | millisecond | `millisecond`, `milliseconds`, `ms`      |
        | second      | `second`, `seconds`, `ss`, `s`           |
        | minute      | `minute`, `minutes`, `mi`, `n`           |
        | hour        | `hour`, `hours`, `hh`, `h`               |
        | day         | `day`, `days`, `dd`, `d`                 |
        | week        | `week`, `weeks`, `wk`, `ww`              |
        | month       | `month`, `months`, `mm`, `m`             |
        | quarter     | `quarter`, `quarters`, `qq`, `q`         |
        | year        | `year`, `years`, `yyyy`, `yy`            |
         - `startdate` — The first time value to subtract (the subtrahend). [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `enddate` — The second time value to subtract from (the minuend). [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone name. If specified, it is applied to both startdate and enddate. If not specified, timezones of startdate and enddate are used. If they are not the same, the result is unspecified. [`String`](/sql-reference/data-types/string)

        Returns the difference between enddate and startdate expressed in unit. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("age", *to_args(locals()))
    
    @staticmethod
    def aggThrow(throw_prob: Any) -> Function:
        """
        aggThrow(throw_prob)

        Args:
        - `throw_prob` — Probability to throw on creation. [`Float64`](/sql-reference/data-types/float)

        Returns an exception: `Code: 503. DB::Exception: Aggregate function aggThrow has thrown exception successfully`.
        """
        return Function("aggThrow", *to_args(locals()))
    
    @staticmethod
    def alphaTokens(s: Any, max_substrings: Any | None = None) -> Function:
        """
        alphaTokens(s[, max_substrings])

        Args:
        - `s` — The string to split. [`String`](/sql-reference/data-types/string)
        - `max_substrings` — Optional. When `max_substrings > 0`, the number of returned substrings will be no more than `max_substrings`, otherwise the function will return as many substrings as possible. [`Int64`](/sql-reference/data-types/int-uint)

        Returns an array of selected substrings of `s`. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("alphaTokens", *to_args(locals()))
    
    @staticmethod
    def analysisOfVariance(val: Any, group_no: Any) -> Function:
        """
        analysisOfVariance(val, group_no)

        Args:
        - `val` — Value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `group_no` — Group number that `val` belongs to. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple with the F-statistic and p-value. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("analysisOfVariance", *to_args(locals()))
    
    @staticmethod
    def and_(val1: Any, val2: Any) -> Function:
        """
        and(val1, val2[, ...])

        Args:
        - `val1, val2[, ...]` — List of at least two values. [`Nullable((U)Int*)`](/sql-reference/data-types/nullable) or [`Nullable(Float*)`](/sql-reference/data-types/nullable)

        Returns:
        - `0`, if at least one argument evaluates to `false`
        - `NULL`, if no argument evaluates to `false` and at least one argument is `NULL`
        - `1`, otherwise
                 [`Nullable(UInt8)`](/sql-reference/data-types/nullable)
        """
        return Function("and", *to_args(locals()))
    
    @staticmethod
    def any(column: Any) -> Function:
        """
        any(column)[ RESPECT NULLS]

        Args:
        - `column` — The column name. [`Any`](/sql-reference/data-types)

        Returns the first value encountered.
             [`Any`](/sql-reference/data-types)
        """
        return Function("any", *to_args(locals()))
    
    @staticmethod
    def anyHeavy(column: Any) -> Function:
        """
        anyHeavy(column)

        Args:
        - `column` — The column name. [`String`](/sql-reference/data-types/string)

        Returns a frequently occurring value. The result is nondeterministic. [`Any`](/sql-reference/data-types)
        """
        return Function("anyHeavy", *to_args(locals()))
    
    @staticmethod
    def anyLast(column: Any) -> Function:
        """
        anyLast(column) [RESPECT NULLS]

        Args:
        - `column` — The column name. [`Any`](/sql-reference/data-types)

        Returns the last value encountered. [`Any`](/sql-reference/data-types)
        """
        return Function("anyLast", *to_args(locals()))
    
    @staticmethod
    def anyLast_respect_nulls(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("anyLast_respect_nulls", *to_args(locals()))
    
    @staticmethod
    def any_respect_nulls(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("any_respect_nulls", *to_args(locals()))
    
    @staticmethod
    def appendTrailingCharIfAbsent(s: Any, c: Any) -> Function:
        """
        appendTrailingCharIfAbsent(s, c)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)
        - `c` — Character to append if absent. [`String`](/sql-reference/data-types/string)

        Returns string `s` with character `c` appended if `s` does not end with `c`. [`String`](/sql-reference/data-types/string)
        """
        return Function("appendTrailingCharIfAbsent", *to_args(locals()))
    
    @staticmethod
    def approx_top_k(N: Any, reserved: Any | None = None) -> Function:
        """
        approx_top_k(N[, reserved])(column)

        Args:
        - `column` — The name of the column for which to find the most frequent values. [`String`](/sql-reference/data-types/string)

        Returns an array of the approximately most frequent values and their counts, sorted in descending order of approximate frequency. [`Array`](/sql-reference/data-types/array)
        """
        return Function("approx_top_k", *to_args(locals()))
    
    @staticmethod
    def approx_top_sum(N: Any, reserved: Any | None = None) -> Function:
        """
        approx_top_sum(N[, reserved])(column, weight)

        Args:
        - `column` — The name of the column for which to find the most frequent values. [`String`](/sql-reference/data-types/string)
        - `weight` — The weight. Every value is accounted `weight` times for frequency calculation. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of the approximately most frequent values and their counts, sorted in descending order of approximate frequency. [`Array`](/sql-reference/data-types/array)
        """
        return Function("approx_top_sum", *to_args(locals()))
    
    @staticmethod
    def areaCartesian(object: Any) -> Function:
        """
        areaCartesian(object)

        Args:
        - `object` — geometry object [`Geometry`](/sql-reference/data-types/geo)

        Returns the area of the object. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("areaCartesian", *to_args(locals()))
    
    @staticmethod
    def areaSpherical(object: Any) -> Function:
        """
        areaSpherical(object)

        Args:
        - `object` — geometry object [`Geometry`](/sql-reference/data-types/geo)

        Returns the area of the object. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("areaSpherical", *to_args(locals()))
    
    @staticmethod
    def argAndMax(arg: Any, val: Any) -> Function:
        """
        argAndMax(arg, val)

        Args:
        - `arg` — Argument for which to find the maximum value. [`const String`](/sql-reference/data-types/string)
        - `val` — The maximum value. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Tuple`](/sql-reference/data-types/tuple)

        Returns a tuple containing the `arg` value that corresponds to maximum `val` value and the maximum `val` value. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("argAndMax", *to_args(locals()))
    
    @staticmethod
    def argAndMin(arg: Any, val: Any) -> Function:
        """
        argAndMin(arg, val)

        Args:
        - `arg` — Argument for which to find the minimum value. [`const String`](/sql-reference/data-types/string)
        - `val` — The minimum value. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Tuple`](/sql-reference/data-types/tuple)

        Returns a tuple containing the `arg` value that corresponds to minimum `val` value and the minimum `val` value. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("argAndMin", *to_args(locals()))
    
    @staticmethod
    def argMax(arg: Any, val: Any) -> Function:
        """
        argMax(arg, val)

        Args:
        - `arg` — Argument for which to find the maximum value. [`const String`](/sql-reference/data-types/string)
        - `val` — The maximum value. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Tuple`](/sql-reference/data-types/tuple)

        Returns the `arg` value that corresponds to maximum `val` value. Type matches `arg` type.
        """
        return Function("argMax", *to_args(locals()))
    
    @staticmethod
    def argMin(arg: Any, val: Any) -> Function:
        """
        argMin(arg, val)

        Args:
        - `arg` — Argument for which to find the maximum value. [`const String`](/sql-reference/data-types/string)
        - `val` — The minimum value. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Tuple`](/sql-reference/data-types/tuple)

        Returns the `arg` value that corresponds to minimum `val` value. Type matches `arg` type.
        """
        return Function("argMin", *to_args(locals()))
    
    @staticmethod
    def array(x1: Any, x2: Any | None = None, xN: Any | None = None) -> Function:
        """
        array(x1 [, x2, ..., xN])

        Args:
        - `x1` — Constant value of any type T. If only this argument is provided, the array will be of type T. - `[, x2, ..., xN]` — Additional N constant values sharing a common supertype with `x1` 
        Returns an array, where 'T' is the smallest common type out of the passed arguments. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("array", *to_args(locals()))
    
    @staticmethod
    def arrayAUCPR(scores: Any, labels: Any, partial_offsets: Any | None = None) -> Function:
        """
        arrayAUCPR(scores, labels[, partial_offsets])

        Args:
        - `cores` — Scores prediction model gives. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `labels` — Labels of samples, usually 1 for positive sample and 0 for negative sample. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Array(Enum)`](/sql-reference/data-types/array)
        - `partial_offsets` — 
        - Optional. An [`Array(T)`](/sql-reference/data-types/array) of three non-negative integers for calculating a partial area under the PR curve (equivalent to a vertical band of the PR space) instead of the whole AUC. This option is useful for distributed computation of the PR AUC. The array must contain the following elements [`higher_partitions_tp`, `higher_partitions_fp`, `total_positives`].
            - `higher_partitions_tp`: The number of positive labels in the higher-scored partitions.
            - `higher_partitions_fp`: The number of negative labels in the higher-scored partitions.
            - `total_positives`: The total number of positive samples in the entire dataset.

        note
        When `arr_partial_offsets` is used, the `arr_scores` and `arr_labels` should be only a partition of the entire dataset, containing an interval of scores.
        The dataset should be divided into contiguous partitions, where each partition contains the subset of the data whose scores fall within a specific range.
        For example:
        - One partition could contain all scores in the range [0, 0.5).
        - Another partition could contain scores in the range [0.5, 1.0].

         
        Returns area under the precision-recall (PR) curve. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayAUCPR", *to_args(locals()))
    
    @staticmethod
    def arrayAll(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayAll(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `cond1_arr, ...` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns `1` if the lambda function returns true for all elements, `0` otherwise [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayAll", *to_args(locals()))
    
    @staticmethod
    def arrayAvg(func: Any | None = None, x: Any | None = None, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayAvg([func(x[, y1, ..., yN])], source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — Optional. A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the average of elements in the source array, or the average of elements of the lambda results if provided. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayAvg", *to_args(locals()))
    
    @staticmethod
    def arrayCompact(arr: Any) -> Function:
        """
        arrayCompact(arr)

        Args:
        - `arr` — An array to remove duplicates from. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array without duplicate values [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayCompact", *to_args(locals()))
    
    @staticmethod
    def arrayConcat(arr1: Any, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayConcat(arr1 [, arr2, ... , arrN])

        Args:
        - `arr1 [, arr2, ... , arrN]` — N number of arrays to concatenate. [`Array(T)`](/sql-reference/data-types/array)

        Returns a single combined array from the provided array arguments. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayConcat", *to_args(locals()))
    
    @staticmethod
    def arrayCount(func: Any | None = None, arr1: Any | None = None) -> Function:
        """
        arrayCount([func, ] arr1, ...)

        Args:
        - `func` — Optional. Function to apply to each element of the array(s). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr1, ..., arrN` — N arrays. [`Array(T)`](/sql-reference/data-types/array)

        Returns the number of elements for which `func` returns true. Otherwise, returns the number of non-zero elements in the array. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayCount", *to_args(locals()))
    
    @staticmethod
    def arrayCumSum(func: Any | None = None, arr1: Any | None = None, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayCumSum([func,] arr1[, arr2, ... , arrN])

        Args:
        - `func` — Optional. A lambda function to apply to the array elements at each position. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr1` — The source array of numeric values. [`Array(T)`](/sql-reference/data-types/array)
        - `[arr2, ..., arrN]` — Optional. Additional arrays of the same size, passed as arguments to the lambda function if specified. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of the partial sums of the elements in the source array. The result type matches the input array's numeric type. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayCumSum", *to_args(locals()))
    
    @staticmethod
    def arrayCumSumNonNegative(func: Any | None = None, arr1: Any | None = None, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayCumSumNonNegative([func,] arr1[, arr2, ... , arrN])

        Args:
        - `func` — Optional. A lambda function to apply to the array elements at each position. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr1` — The source array of numeric values. [`Array(T)`](/sql-reference/data-types/array)
        - `[arr2, ..., arrN]` — Optional. Additional arrays of the same size, passed as arguments to the lambda function if specified. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of the partial sums of the elements in the source array, with any negative running sum replaced by zero. The result type matches the input array's numeric type. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayCumSumNonNegative", *to_args(locals()))
    
    @staticmethod
    def arrayDifference(arr: Any) -> Function:
        """
        arrayDifference(arr)

        Args:
        - `arr` — Array for which to calculate differences between adjacent elements. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of differences between adjacent array elements [`UInt*`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayDifference", *to_args(locals()))
    
    @staticmethod
    def arrayDistinct(arr: Any) -> Function:
        """
        arrayDistinct(arr)

        Args:
        - `arr` — Array for which to extract distinct elements. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array containing the distinct elements [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayDistinct", *to_args(locals()))
    
    @staticmethod
    def arrayDotProduct(v1: Any, v2: Any) -> Function:
        """
        arrayDotProduct(v1, v2)

        Args:
        - `v1` — First vector. [`Array((U)Int* | Float* | Decimal)`](/sql-reference/data-types/array) or [`Tuple((U)Int* | Float* | Decimal)`](/sql-reference/data-types/tuple)
        - `v2` — Second vector. [`Array((U)Int* | Float* | Decimal)`](/sql-reference/data-types/array) or [`Tuple((U)Int* | Float* | Decimal)`](/sql-reference/data-types/tuple)

        The dot product of the two vectors.

        note
        The return type is determined by the type of the arguments. If Arrays or Tuples contain mixed element types then the result type is the supertype.


         [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        """
        return Function("arrayDotProduct", *to_args(locals()))
    
    @staticmethod
    def arrayElement(arr: Any, n: Any) -> Function:
        """
        arrayElement(arr, n)

        Args:
        - `arr` — The array to search. [`Array(T)`](/sql-reference/data-types/array). - `n` — Position of the element to get. [`(U)Int*`](/sql-reference/data-types/int-uint). 
        Returns a single combined array from the provided array arguments [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayElement", *to_args(locals()))
    
    @staticmethod
    def arrayElementOrNull(arrays: Any) -> Function:
        """
        arrayElementOrNull(arrays)

        Args:
        - `arrays` — Arbitrary number of array arguments. [`Array`](/sql-reference/data-types/array)

        Returns a single combined array from the provided array arguments. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayElementOrNull", *to_args(locals()))
    
    @staticmethod
    def arrayEnumerate(arr: Any) -> Function:
        """
        arrayEnumerate(arr)

        Args:
        - `arr` — The array to enumerate. [`Array`](/sql-reference/data-types/array)

        Returns the array `[1, 2, 3, ..., length (arr)]`. [`Array(UInt32)`](/sql-reference/data-types/array)
        """
        return Function("arrayEnumerate", *to_args(locals()))
    
    @staticmethod
    def arrayEnumerateDense(arr: Any) -> Function:
        """
        arrayEnumerateDense(arr)

        Args:
        - `arr` — The array to enumerate. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of the same size as `arr`, indicating where each element first appears in the source array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayEnumerateDense", *to_args(locals()))
    
    @staticmethod
    def arrayEnumerateDenseRanked(clear_depth: Any, arr: Any, max_array_depth: Any) -> Function:
        """
        arrayEnumerateDenseRanked(clear_depth, arr, max_array_depth)

        Args:
        - `clear_depth` — Enumerate elements at the specified level separately. Must be less than or equal to `max_arr_depth`. [`UInt*`](/sql-reference/data-types/int-uint)
        - `arr` — N-dimensional array to enumerate. [`Array(T)`](/sql-reference/data-types/array)
        - `max_array_depth` — The maximum effective depth. Must be less than or equal to the depth of `arr`. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an array denoting where each element first appears in the source array [`Array`](/sql-reference/data-types/array)
        """
        return Function("arrayEnumerateDenseRanked", *to_args(locals()))
    
    @staticmethod
    def arrayEnumerateUniq(arr1: Any, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayEnumerateUniq(arr1[, arr2, ... , arrN])

        Args:
        - `arr1` — First array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `arr2, ...` — Optional. Additional arrays of the same size for tuple uniqueness. [`Array(UInt32)`](/sql-reference/data-types/array)

        Returns an array where each element is the position among elements with the same value or tuple. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayEnumerateUniq", *to_args(locals()))
    
    @staticmethod
    def arrayEnumerateUniqRanked(clear_depth: Any, arr: Any, max_array_depth: Any) -> Function:
        """
        arrayEnumerateUniqRanked(clear_depth, arr, max_array_depth)

        Args:
        - `clear_depth` — Enumerate elements at the specified level separately. Positive integer less than or equal to `max_arr_depth`. [`UInt*`](/sql-reference/data-types/int-uint)
        - `arr` — N-dimensional array to enumerate. [`Array(T)`](/sql-reference/data-types/array)
        - `max_array_depth` — The maximum effective depth. Positive integer less than or equal to the depth of `arr`. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an N-dimensional array the same size as `arr` with each element showing the position of that element in relation to other elements of the same value. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayEnumerateUniqRanked", *to_args(locals()))
    
    @staticmethod
    def arrayExcept(source: Any, except_: Any) -> Function:
        """
        arrayExcept(source, except)

        Args:
        - `source` — The source array containing elements to filter.  [`Array(T)`](/sql-reference/data-types/array)
        - `except` — The array containing elements to exclude from the result.  [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of the same type as the input array containing elements from `source` that weren't found in `except`.  [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayExcept", *to_args(locals()))
    
    @staticmethod
    def arrayExists(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayExists(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns `1` if the lambda function returns true for at least one element, `0` otherwise [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayExists", *to_args(locals()))
    
    @staticmethod
    def arrayFill(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayFill(func(x [, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x [, y1, ..., yN])` — A lambda function `func(x [, y1, y2, ... yN]) → F(x [, y1, y2, ... yN])` which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayFill", *to_args(locals()))
    
    @staticmethod
    def arrayFilter(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayFilter(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])]

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns a subset of the source array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayFilter", *to_args(locals()))
    
    @staticmethod
    def arrayFirst(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayFirst(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [Lambda function](/sql-reference/functions/overview#arrow-operator-and-lambda). - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array). - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array). 
        Returns the first element of the source array for which `λ` is true, otherwise returns the default value of `T`.
        """
        return Function("arrayFirst", *to_args(locals()))
    
    @staticmethod
    def arrayFirstIndex(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayFirstIndex(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [Lambda function](/sql-reference/functions/overview#arrow-operator-and-lambda). - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array). - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array). 
        Returns the index of the first element of the source array for which `func` is true, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayFirstIndex", *to_args(locals()))
    
    @staticmethod
    def arrayFirstOrNull(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayFirstOrNull(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the first element of the source array for which `func` is true, otherwise returns `NULL`.
        """
        return Function("arrayFirstOrNull", *to_args(locals()))
    
    @staticmethod
    def arrayFlatten(arr: Any) -> Function:
        """
        arrayFlatten(arr)

        Args:
        - `arr` — A multidimensional array. [`Array(Array(T))`](/sql-reference/data-types/array)

        Returns a flattened array from the multidimensional array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayFlatten", *to_args(locals()))
    
    @staticmethod
    def arrayFold(λ: Any, acc: Any, x1: Any, x2: Any | None = None, x3: Any | None = None, xN: Any | None = None) -> Function:
        """
        arrayFold(λ(acc, x1 [, x2, x3, ... xN]), arr1 [, arr2, arr3, ... arrN], acc)

        Args:
        - `λ(x, x1 [, x2, x3, ... xN])` — A lambda function `λ(acc, x1 [, x2, x3, ... xN]) → F(acc, x1 [, x2, x3, ... xN])` where `F` is an operation applied to `acc` and array values from `x` with the result of `acc` re-used. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr1 [, arr2, arr3, ... arrN]` — N arrays over which to operate. [`Array(T)`](/sql-reference/data-types/array)
        - `acc` — Accumulator value with the same type as the return type of the Lambda function. 
        Returns the final `acc` value.
        """
        return Function("arrayFold", *to_args(locals()))
    
    @staticmethod
    def arrayIntersect(arr: Any, arr1: Any, arrN: Any) -> Function:
        """
        arrayIntersect(arr, arr1, ..., arrN)

        Args:
        - `arrN` — N arrays from which to make the new array. [`Array(T)`](/sql-reference/data-types/array). 
        Returns an array with distinct elements that are present in all N arrays [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayIntersect", *to_args(locals()))
    
    @staticmethod
    def arrayJaccardIndex(arr_x: Any, arr_y: Any) -> Function:
        """
        arrayJaccardIndex(arr_x, arr_y)

        Args:
        - `arr_x` — First array. [`Array(T)`](/sql-reference/data-types/array)
        - `arr_y` — Second array. [`Array(T)`](/sql-reference/data-types/array)

        Returns the Jaccard index of `arr_x` and `arr_y` [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayJaccardIndex", *to_args(locals()))
    
    @staticmethod
    def arrayJoin(arr: Any) -> Function:
        """
        arrayJoin(arr)

        Args:
        - `arr` — An array to unfold. [`Array(T)`](/sql-reference/data-types/array)

        Returns a set of rows unfolded from `arr`.
        """
        return Function("arrayJoin", *to_args(locals()))
    
    @staticmethod
    def arrayLast(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayLast(func(x[, y1, ..., yN]), source[, cond1, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [Lambda function](/sql-reference/functions/overview#arrow-operator-and-lambda). - `source` — The source array to process. [`Array(T)`](/sql-reference/data-types/array). - `[, cond1, ... , condN]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array). 
        Returns the last element of the source array for which `func` is true, otherwise returns the default value of `T`.
        """
        return Function("arrayLast", *to_args(locals()))
    
    @staticmethod
    def arrayLastIndex(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayLastIndex(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the index of the last element of the source array for which `func` is true, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayLastIndex", *to_args(locals()))
    
    @staticmethod
    def arrayLastOrNull(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayLastOrNull(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x [, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [Lambda function](/sql-reference/functions/overview#arrow-operator-and-lambda). - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array). - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array). 
        Returns the last element of the source array for which `λ` is not true, otherwise returns `NULL`.
        """
        return Function("arrayLastOrNull", *to_args(locals()))
    
    @staticmethod
    def arrayLevenshteinDistance(from_: Any, to: Any) -> Function:
        """
        arrayLevenshteinDistance(from, to)

        Args:
        - `from` — The first array. [`Array(T)`](/sql-reference/data-types/array). - `to` — The second array. [`Array(T)`](/sql-reference/data-types/array). 
        Levenshtein distance between the first and the second arrays. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayLevenshteinDistance", *to_args(locals()))
    
    @staticmethod
    def arrayLevenshteinDistanceWeighted(from_: Any, to: Any, from_weights: Any, to_weights: Any) -> Function:
        """
        arrayLevenshteinDistanceWeighted(from, to, from_weights, to_weights)

        Args:
        - `from` — first array. [`Array(T)`](/sql-reference/data-types/array). - `to` — second array. [`Array(T)`](/sql-reference/data-types/array). - `from_weights` — weights for the first array. [`Array((U)Int*|Float*)`](/sql-reference/data-types/array)
        - `to_weights` — weights for the second array. [`Array((U)Int*|Float*)`](/sql-reference/data-types/array)

        Levenshtein distance between the first and the second arrays with custom weights for each element [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayLevenshteinDistanceWeighted", *to_args(locals()))
    
    @staticmethod
    def arrayMap(func: Any, arr: Any) -> Function:
        """
        arrayMap(func, arr)

        Args:
        - `func` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr` — N arrays to process. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array from the lambda results [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayMap", *to_args(locals()))
    
    @staticmethod
    def arrayMax(func: Any | None = None, x: Any | None = None, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayMax([func(x[, y1, ..., yN])], source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — Optional. A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the maximum element in the source array, or the maximum element of the lambda results if provided.
        """
        return Function("arrayMax", *to_args(locals()))
    
    @staticmethod
    def arrayMin(func: Any | None = None, x: Any | None = None, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayMin([func(x[, y1, ..., yN])], source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — Optional. A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `cond1_arr, ...` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the minimum element in the source array, or the minimum element of the lambda results if provided.
        """
        return Function("arrayMin", *to_args(locals()))
    
    @staticmethod
    def arrayNormalizedGini(predicted: Any, label: Any) -> Function:
        """
        arrayNormalizedGini(predicted, label)

        Args:
        - `predicted` — The predicted value. [`Array(T)`](/sql-reference/data-types/array)
        - `label` — The actual value. [`Array(T)`](/sql-reference/data-types/array)

        A tuple containing the Gini coefficients of the predicted values, the Gini coefficient of the normalized values, and the normalized Gini coefficient (= the ratio of the former two Gini coefficients) [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("arrayNormalizedGini", *to_args(locals()))
    
    @staticmethod
    def arrayPartialReverseSort(f: Any | None = None, arr: Any | None = None, arr1: Any | None = None, arrN: Any | None = None, limit: Any | None = None) -> Function:
        """
        arrayPartialReverseSort([f,] arr [, arr1, ... ,arrN], limit)

        Args:
        - `f(arr[, arr1, ... ,arrN])` — The lambda function to apply to elements of array `x`. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr` — Array to be sorted. [`Array(T)`](/sql-reference/data-types/array)
        - `arr1, ... ,arrN` — N additional arrays, in the case when `f` accepts multiple arguments. [`Array(T)`](/sql-reference/data-types/array)
        - `limit` — Index value up until which sorting will occur. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of the same size as the original array where elements in the range `[1..limit]` are sorted
        in descending order. The remaining elements `(limit..N]` are in an unspecified order.
        """
        return Function("arrayPartialReverseSort", *to_args(locals()))
    
    @staticmethod
    def arrayPartialShuffle(arr: Any, limit: Any | None = None, seed: Any | None = None) -> Function:
        """
        arrayPartialShuffle(arr [, limit[, seed]])

        Args:
        - `arr` — The array to shuffle. [`Array(T)`](/sql-reference/data-types/array)
        - `seed` — Optional. The seed to be used with random number generation. If not provided, a random one is used. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `limit` — Optional. The number to limit element swaps to, in the range `[1..N]`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Array with elements partially shuffled. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayPartialShuffle", *to_args(locals()))
    
    @staticmethod
    def arrayPartialSort(f: Any | None = None, arr: Any | None = None, arr1: Any | None = None, arrN: Any | None = None, limit: Any | None = None) -> Function:
        """
        arrayPartialSort([f,] arr [, arr1, ... ,arrN], limit)

        Args:
        - `f(arr[, arr1, ... ,arrN])` — The lambda function to apply to elements of array `x`. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `arr` — Array to be sorted. [`Array(T)`](/sql-reference/data-types/array)
        - `arr1, ... ,arrN` — N additional arrays, in the case when `f` accepts multiple arguments. [`Array(T)`](/sql-reference/data-types/array)
        - `limit` — Index value up until which sorting will occur. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array of the same size as the original array where elements in the range `[1..limit]` are sorted
        in ascending order. The remaining elements `(limit..N]` are in an unspecified order.
        """
        return Function("arrayPartialSort", *to_args(locals()))
    
    @staticmethod
    def arrayPopBack(arr: Any) -> Function:
        """
        arrayPopBack(arr)

        Args:
        - `arr` — The array for which to remove the last element from. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array identical to `arr` but without the last element of `arr` [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayPopBack", *to_args(locals()))
    
    @staticmethod
    def arrayPopFront(arr: Any) -> Function:
        """
        arrayPopFront(arr)

        Args:
        - `arr` — The array for which to remove the first element from. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array identical to `arr` but without the first element of `arr` [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayPopFront", *to_args(locals()))
    
    @staticmethod
    def arrayProduct(func: Any | None = None, x: Any | None = None, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayProduct([func(x[, y1, ..., yN])], source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — Optional. A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the product of elements in the source array, or the product of elements of the lambda results if provided. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayProduct", *to_args(locals()))
    
    @staticmethod
    def arrayPushBack(arr: Any, x: Any) -> Function:
        """
        arrayPushBack(arr, x)

        Args:
        - `arr` — The array for which to add value `x` to the end of. [`Array(T)`](/sql-reference/data-types/array)
        - `x` — 
        - Single value to add to the end of the array. [`Array(T)`](/sql-reference/data-types/array).

        note
        - Only numbers can be added to an array with numbers, and only strings can be added to an array of strings.
        - When adding numbers, ClickHouse automatically sets the type of `x` for the data type of the array.
        - Can be `NULL`. The function adds a `NULL` element to an array, and the type of array elements converts to `Nullable`.

        For more information about the types of data in ClickHouse, see [Data types](/sql-reference/data-types).

             
        Returns an array identical to `arr` but with an additional value `x` at the end of the array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayPushBack", *to_args(locals()))
    
    @staticmethod
    def arrayPushFront(arr: Any, x: Any) -> Function:
        """
        arrayPushFront(arr, x)

        Args:
        - `arr` — The array for which to add value `x` to the end of. [`Array(T)`](/sql-reference/data-types/array). - `x` — 
        - Single value to add to the start of the array. [`Array(T)`](/sql-reference/data-types/array).

        note
        - Only numbers can be added to an array with numbers, and only strings can be added to an array of strings.
        - When adding numbers, ClickHouse automatically sets the type of `x` for the data type of the array.
        - Can be `NULL`. The function adds a `NULL` element to an array, and the type of array elements converts to `Nullable`.

        For more information about the types of data in ClickHouse, see [Data types](/sql-reference/data-types).

             
        Returns an array identical to `arr` but with an additional value `x` at the beginning of the array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayPushFront", *to_args(locals()))
    
    @staticmethod
    def arrayROCAUC(scores: Any, labels: Any, scale: Any | None = None, partial_offsets: Any | None = None) -> Function:
        """
        arrayROCAUC(scores, labels[, scale[, partial_offsets]])

        Args:
        - `scores` — Scores prediction model gives. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `labels` — Labels of samples, usually 1 for positive sample and 0 for negative sample. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Enum`](/sql-reference/data-types/enum)
        - `scale` — Optional. Decides whether to return the normalized area. If false, returns the area under the TP (true positives) x FP (false positives) curve instead. Default value: true. [`Bool`](/sql-reference/data-types/boolean)
        - `partial_offsets` — 
        - An array of four non-negative integers for calculating a partial area under the ROC curve (equivalent to a vertical band of the ROC space) instead of the whole AUC. This option is useful for distributed computation of the ROC AUC. The array must contain the following elements [`higher_partitions_tp`, `higher_partitions_fp`, `total_positives`, `total_negatives`]. [Array](/sql-reference/data-types/array) of non-negative [Integers](../data-types/int-uint.md). Optional.
            - `higher_partitions_tp`: The number of positive labels in the higher-scored partitions.
            - `higher_partitions_fp`: The number of negative labels in the higher-scored partitions.
            - `total_positives`: The total number of positive samples in the entire dataset.
            - `total_negatives`: The total number of negative samples in the entire dataset.

        note
        When `arr_partial_offsets` is used, the `arr_scores` and `arr_labels` should be only a partition of the entire dataset, containing an interval of scores.
        The dataset should be divided into contiguous partitions, where each partition contains the subset of the data whose scores fall within a specific range.
        For example:
        - One partition could contain all scores in the range [0, 0.5).
        - Another partition could contain scores in the range [0.5, 1.0].

         
        Returns area under the receiver operating characteristic (ROC) curve. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arrayROCAUC", *to_args(locals()))
    
    @staticmethod
    def arrayRandomSample(arr: Any, samples: Any) -> Function:
        """
        arrayRandomSample(arr, samples)

        Args:
        - `arr` — The input array or multidimensional array from which to sample elements. [`Array(T)`](/sql-reference/data-types/array)
        - `samples` — The number of elements to include in the random sample. [`(U)Int*`](/sql-reference/data-types/int-uint)

        An array containing a random sample of elements from the input array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayRandomSample", *to_args(locals()))
    
    @staticmethod
    def arrayReduce(agg_f: Any, arr1: Any, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayReduce(agg_f, arr1 [, arr2, ... , arrN)])

        Args:
        - `agg_f` — The name of an aggregate function which should be a constant. [`String`](/sql-reference/data-types/string)
        - `arr1 [, arr2, ... , arrN)]` — N arrays corresponding to the arguments of `agg_f`. [`Array(T)`](/sql-reference/data-types/array)

        Returns the result of the aggregate function
        """
        return Function("arrayReduce", *to_args(locals()))
    
    @staticmethod
    def arrayReduceInRanges(agg_f: Any, ranges: Any, arr1: Any, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayReduceInRanges(agg_f, ranges, arr1 [, arr2, ... ,arrN)])

        Args:
        - `agg_f` — The name of the aggregate function to use. [`String`](/sql-reference/data-types/string)
        - `ranges` — The range over which to aggregate. An array of tuples, `(i, r)` containing the index `i` from which to begin from and the range `r` over which to aggregate. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `arr1 [, arr2, ... ,arrN)]` — N arrays as arguments to the aggregate function. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array containing results of the aggregate function over the specified ranges [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayReduceInRanges", *to_args(locals()))
    
    @staticmethod
    def arrayRemove(arr: Any, elem: Any) -> Function:
        """
        arrayRemove(arr, elem)

        Args:
        - `arr` — Array(T) - `elem` — T 
        Returns a subset of the source array [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayRemove", *to_args(locals()))
    
    @staticmethod
    def arrayResize(arr: Any, size: Any, extender: Any | None = None) -> Function:
        """
        arrayResize(arr, size[, extender])

        Args:
        - `arr` — Array to resize. [`Array(T)`](/sql-reference/data-types/array)
        - `size` — 
        -The new length of the array.
        If `size` is less than the original size of the array, the array is truncated from the right.
        If `size` is larger than the initial size of the array, the array is extended to the right with `extender` values or default values for the data type of the array items.
         - `extender` — Value to use for extending the array. Can be `NULL`. 
        An array of length `size`. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayResize", *to_args(locals()))
    
    @staticmethod
    def arrayReverse(arr: Any) -> Function:
        """
        arrayReverse(arr)

        Args:
        - `arr` — The array to reverse. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of the same size as the original array containing the elements in reverse order [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayReverse", *to_args(locals()))
    
    @staticmethod
    def arrayReverseFill(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayReverseFill(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array with elements of the source array replaced by the results of the lambda. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayReverseFill", *to_args(locals()))
    
    @staticmethod
    def arrayReverseSort(f: Any | None = None, arr: Any | None = None, arr1: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayReverseSort([f,] arr [, arr1, ... ,arrN)

        Args:
        - `f(y1[, y2 ... yN])` — The lambda function to apply to elements of array `x`. - `arr` — An array to be sorted. [`Array(T)`](/sql-reference/data-types/array) - `arr1, ..., yN` — Optional. N additional arrays, in the case when `f` accepts multiple arguments. 
        Returns the array `x` sorted in descending order if no lambda function is provided, otherwise
        it returns an array sorted according to the logic of the provided lambda function, and then reversed. [`Array(T)`](/sql-reference/data-types/array).
        """
        return Function("arrayReverseSort", *to_args(locals()))
    
    @staticmethod
    def arrayReverseSplit(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arrayReverseSplit(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of arrays. [`Array(Array(T))`](/sql-reference/data-types/array)
        """
        return Function("arrayReverseSplit", *to_args(locals()))
    
    @staticmethod
    def arrayRotateLeft(arr: Any, n: Any) -> Function:
        """
        arrayRotateLeft(arr, n)

        Args:
        - `arr` — The array for which to rotate the elements.[`Array(T)`](/sql-reference/data-types/array). - `n` — Number of elements to rotate. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint). 
        An array rotated to the left by the specified number of elements [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayRotateLeft", *to_args(locals()))
    
    @staticmethod
    def arrayRotateRight(arr: Any, n: Any) -> Function:
        """
        arrayRotateRight(arr, n)

        Args:
        - `arr` — The array for which to rotate the elements.[`Array(T)`](/sql-reference/data-types/array). - `n` — Number of elements to rotate. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint). 
        An array rotated to the right by the specified number of elements [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayRotateRight", *to_args(locals()))
    
    @staticmethod
    def arrayShiftLeft(arr: Any, n: Any, default: Any | None = None) -> Function:
        """
        arrayShiftLeft(arr, n[, default])

        Args:
        - `arr` — The array for which to shift the elements.[`Array(T)`](/sql-reference/data-types/array). - `n` — Number of elements to shift.[`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint). - `default` — Optional. Default value for new elements. 
        An array shifted to the left by the specified number of elements [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayShiftLeft", *to_args(locals()))
    
    @staticmethod
    def arrayShiftRight(arr: Any, n: Any, default: Any | None = None) -> Function:
        """
        arrayShiftRight(arr, n[, default])

        Args:
        - `arr` — The array for which to shift the elements. [`Array(T)`](/sql-reference/data-types/array)
        - `n` — Number of elements to shift. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `default` — Optional. Default value for new elements. 
        An array shifted to the right by the specified number of elements [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayShiftRight", *to_args(locals()))
    
    @staticmethod
    def arrayShuffle(arr: Any, seed: Any | None = None) -> Function:
        """
        arrayShuffle(arr [, seed])

        Args:
        - `arr` — The array to shuffle. [`Array(T)`](/sql-reference/data-types/array)
        - `seed (optional)` — Optional. The seed to be used with random number generation. If not provided a random one is used. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Array with elements shuffled [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayShuffle", *to_args(locals()))
    
    @staticmethod
    def arraySimilarity(from_: Any, to: Any, from_weights: Any, to_weights: Any) -> Function:
        """
        arraySimilarity(from, to, from_weights, to_weights)

        Args:
        - `from` — first array [`Array(T)`](/sql-reference/data-types/array)
        - `to` — second array [`Array(T)`](/sql-reference/data-types/array)
        - `from_weights` — weights for the first array. [`Array((U)Int*|Float*)`](/sql-reference/data-types/array)
        - `to_weights` — weights for the second array. [`Array((U)Int*|Float*)`](/sql-reference/data-types/array)

        Returns the similarity between `0` and `1` of the two arrays based on the weighted Levenshtein distance [`Float64`](/sql-reference/data-types/float)
        """
        return Function("arraySimilarity", *to_args(locals()))
    
    @staticmethod
    def arraySlice(arr: Any, offset: Any, length: Any | None = None) -> Function:
        """
        arraySlice(arr, offset [, length])

        Args:
        - `arr` — Array to slice. [`Array(T)`](/sql-reference/data-types/array)
        - `offset` — Indent from the edge of the array. A positive value indicates an offset on the left, and a negative value is an indent on the right. Numbering of the array items begins with `1`. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `length` — The length of the required slice. If you specify a negative value, the function returns an open slice `[offset, array_length - length]`. If you omit the value, the function returns the slice `[offset, the_end_of_array]`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a slice of the array with `length` elements from the specified `offset` [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arraySlice", *to_args(locals()))
    
    @staticmethod
    def arraySort(f: Any | None = None, arr: Any | None = None, arr1: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arraySort([f,] arr [, arr1, ... ,arrN])

        Args:
        - `f(y1[, y2 ... yN])` — The lambda function to apply to elements of array `x`. - `arr` — An array to be sorted. [`Array(T)`](/sql-reference/data-types/array) - `arr1, ..., yN` — Optional. N additional arrays, in the case when `f` accepts multiple arguments. 
        Returns the array `arr` sorted in ascending order if no lambda function is provided, otherwise
        it returns an array sorted according to the logic of the provided lambda function. [`Array(T)`](/sql-reference/data-types/array).
        """
        return Function("arraySort", *to_args(locals()))
    
    @staticmethod
    def arraySplit(func: Any, x: Any, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arraySplit(func(x[, y1, ..., yN]), source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`).[Lambda function](/sql-reference/functions/overview#arrow-operator-and-lambda). - `source_arr` — The source array to split [`Array(T)`](/sql-reference/data-types/array). - `[, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array). 
        Returns an array of arrays [`Array(Array(T))`](/sql-reference/data-types/array)
        """
        return Function("arraySplit", *to_args(locals()))
    
    @staticmethod
    def arrayStringConcat(arr: Any, separator: Any | None = None) -> Function:
        """
        arrayStringConcat(arr[, separator])

        Args:
        - `arr` — The array to concatenate. [`Array(T)`](/sql-reference/data-types/array)
        - `separator` — Optional. Separator string. By default an empty string. [`const String`](/sql-reference/data-types/string)

        Returns the concatenated string. [`String`](/sql-reference/data-types/string)
        """
        return Function("arrayStringConcat", *to_args(locals()))
    
    @staticmethod
    def arraySum(func: Any | None = None, x: Any | None = None, y1: Any | None = None, yN: Any | None = None) -> Function:
        """
        arraySum([func(x[, y1, ..., yN])], source_arr[, cond1_arr, ... , condN_arr])

        Args:
        - `func(x[, y1, ..., yN])` — Optional. A lambda function which operates on elements of the source array (`x`) and condition arrays (`y`). [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `source_arr` — The source array to process. [`Array(T)`](/sql-reference/data-types/array)
        - `, cond1_arr, ... , condN_arr]` — Optional. N condition arrays providing additional arguments to the lambda function. [`Array(T)`](/sql-reference/data-types/array)

        Returns the sum of elements in the source array, or the sum of elements of the lambda results if provided.
        """
        return Function("arraySum", *to_args(locals()))
    
    @staticmethod
    def arraySymmetricDifference(arr1: Any, arr2: Any, arrN: Any) -> Function:
        """
        arraySymmetricDifference(arr1, arr2, ... , arrN)

        Args:
        - `arrN` — N arrays from which to make the new array. [`Array(T)`](/sql-reference/data-types/array). 
        Returns an array of distinct elements not present in all source arrays [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arraySymmetricDifference", *to_args(locals()))
    
    @staticmethod
    def arrayUnion(arr1: Any, arr2: Any, arrN: Any) -> Function:
        """
        arrayUnion(arr1, arr2, ..., arrN)

        Args:
        - `arrN` — N arrays from which to make the new array. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array with distinct elements from the source arrays [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayUnion", *to_args(locals()))
    
    @staticmethod
    def arrayUniq(arr1: Any, arr2: Any | None = None, arrN: Any | None = None) -> Function:
        """
        arrayUniq(arr1[, arr2, ..., arrN])

        Args:
        - `arr1` — Array for which to count the number of unique elements. [`Array(T)`](/sql-reference/data-types/array)
        - `[, arr2, ..., arrN]` — Optional. Additional arrays used to count the number of unique tuples of elements at corresponding positions in multiple arrays. [`Array(T)`](/sql-reference/data-types/array)

        For a single argument returns the number of unique
        elements. For multiple arguments returns the number of unique tuples made from
        elements at corresponding positions across the arrays.
         [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("arrayUniq", *to_args(locals()))
    
    @staticmethod
    def arrayWithConstant(N: Any, x: Any) -> Function:
        """
        arrayWithConstant(N, x)

        Args:
        - `length` — Number of elements in the array. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `x` — The value of the `N` elements in the array, of any type. 
        Returns an Array with `N` elements of value `x`. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayWithConstant", *to_args(locals()))
    
    @staticmethod
    def arrayZip(arr1: Any, arr2: Any, arrN: Any) -> Function:
        """
        arrayZip(arr1, arr2, ... , arrN)

        Args:
        - `arr1, arr2, ... , arrN` — N arrays to combine into a single array. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array with elements from the source arrays grouped in tuples. Data types in the tuple are the same as types of the input arrays and in the same order as arrays are passed [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("arrayZip", *to_args(locals()))
    
    @staticmethod
    def arrayZipUnaligned(arr1: Any, arr2: Any, arrN: Any) -> Function:
        """
        arrayZipUnaligned(arr1, arr2, ..., arrN)

        Args:
        - `arr1, arr2, ..., arrN` — N arrays to combine into a single array. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array with elements from the source arrays grouped in tuples. Data types in the tuple are the same as types of the input arrays and in the same order as arrays are passed. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T1, T2, ...)`](/sql-reference/data-types/tuple)
        """
        return Function("arrayZipUnaligned", *to_args(locals()))
    
    @staticmethod
    def ascii(s: Any) -> Function:
        """
        ascii(s)

        Args:
        - `s` — String input. [`String`](/sql-reference/data-types/string)

        Returns the ASCII code point of the first character. If `s` is empty, the result is `0`. If the first character is not an ASCII character or not part of the Latin-1 supplement range of UTF-16, the result is undefined. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("ascii", *to_args(locals()))
    
    @staticmethod
    def asin(x: Any) -> Function:
        """
        asin(x)

        Args:
        - `x` — Argument for which to calculate arcsine of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the arcsine value of the provided argument `x` [`Float64`](/sql-reference/data-types/float)
        """
        return Function("asin", *to_args(locals()))
    
    @staticmethod
    def asinh(x: Any) -> Function:
        """
        asinh(x)

        Args:
        - `x` — Hyperbolic sine of angle. Values from the interval: `-∞ < x < +∞`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the angle, in radians. Values from the interval: `-∞ < asinh(x) < +∞`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("asinh", *to_args(locals()))
    
    @staticmethod
    def assumeNotNull(x: Any) -> Function:
        """
        assumeNotNull(x)

        Args:
        - `x` — The original value of any nullable type. [`Nullable(T)`](/sql-reference/data-types/nullable)

        Returns the non-nullable value, if the original value was not `NULL`, otherwise an arbitrary value, if the input value is `NULL`. [`Any`](/sql-reference/data-types)
        """
        return Function("assumeNotNull", *to_args(locals()))
    
    @staticmethod
    def atan(x: Any) -> Function:
        """
        atan(x)

        Args:
        - `x` — The value for which to find arc tangent of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the arc tangent of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("atan", *to_args(locals()))
    
    @staticmethod
    def atan2(y: Any, x: Any) -> Function:
        """
        atan2(y, x)

        Args:
        - `y` — y-coordinate of the point through which the ray passes. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        - `x` — x-coordinate of the point through which the ray passes. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the angle `θ` such that `-π < θ ≤ π`, in radians [`Float64`](/sql-reference/data-types/float)
        """
        return Function("atan2", *to_args(locals()))
    
    @staticmethod
    def atanh(x: Any) -> Function:
        """
        atanh(x)

        Args:
        - `x` — Hyperbolic tangent of angle. Values from the interval: -1 < x < 1. `(U)Int*`, `Float*` or `Decimal*`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the angle, in radians. Values from the interval: -∞ < atanh(x) < +∞ [`Float64`](/sql-reference/data-types/float)
        """
        return Function("atanh", *to_args(locals()))
    
    @staticmethod
    def authenticatedUser() -> Function:
        """
        authenticatedUser()

        
        The name of the authenticated user. [`String`](/sql-reference/data-types/string)
        """
        return Function("authenticatedUser", *to_args(locals()))
    
    @staticmethod
    def avg(x: Any) -> Function:
        """
        avg(x)

        Args:
        - `x` — Input values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the arithmetic mean, otherwise returns `NaN` if the input parameter `x` is empty. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("avg", *to_args(locals()))
    
    @staticmethod
    def avg2(x1: Any, x2: Any) -> Function:
        """
        avg2(x1, x2])

        Args:
        - `x1, x2]` — Accepts two values for averaging. 
        Returns the average value of the provided arguments, promoted to the largest compatible type.
        """
        return Function("avg2", *to_args(locals()))
    
    @staticmethod
    def avgWeighted(x: Any, weight: Any) -> Function:
        """
        avgWeighted(x, weight)

        Args:
        - `x` — Values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `weight` — Weights of the values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `NaN` if all the weights are equal to 0 or the supplied weights parameter is empty, or the weighted mean otherwise. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("avgWeighted", *to_args(locals()))
    
    @staticmethod
    def bar(x: Any, min: Any, max: Any, width: Any | None = None) -> Function:
        """
        bar(x, min, max[, width])

        Args:
        - `x` — Size to display. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `min` — The minimum value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `max` — The maximum value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `width` — Optional. The width of the bar in characters. The default is `80`. [`const (U)Int*`](/sql-reference/data-types/int-uint) or [`const Float*`](/sql-reference/data-types/float) or [`const Decimal`](/sql-reference/data-types/decimal)

        Returns a unicode-art bar string. [`String`](/sql-reference/data-types/string)
        """
        return Function("bar", *to_args(locals()))
    
    @staticmethod
    def base32Decode(encoded: Any) -> Function:
        """
        base32Decode(encoded)

        Args:
        - `encoded` — String column or constant. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("base32Decode", *to_args(locals()))
    
    @staticmethod
    def base32Encode(plaintext: Any) -> Function:
        """
        base32Encode(plaintext)

        Args:
        - `plaintext` — Plaintext to encode. [`String`](/sql-reference/data-types/string)

        Returns a string containing the encoded value of the argument. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        """
        return Function("base32Encode", *to_args(locals()))
    
    @staticmethod
    def base58Decode(encoded: Any) -> Function:
        """
        base58Decode(encoded)

        Args:
        - `encoded` — String column or constant to decode. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("base58Decode", *to_args(locals()))
    
    @staticmethod
    def base58Encode(plaintext: Any) -> Function:
        """
        base58Encode(plaintext)

        Args:
        - `plaintext` — Plaintext to encode. [`String`](/sql-reference/data-types/string)

        Returns a string containing the encoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("base58Encode", *to_args(locals()))
    
    @staticmethod
    def base64Decode(encoded: Any) -> Function:
        """
        base64Decode(encoded)

        Args:
        - `encoded` — String column or constant to decode. If the string is not valid Base64-encoded, an exception is thrown. [`String`](/sql-reference/data-types/string)

        Returns the decoded string. [`String`](/sql-reference/data-types/string)
        """
        return Function("base64Decode", *to_args(locals()))
    
    @staticmethod
    def base64Encode(plaintext: Any) -> Function:
        """
        base64Encode(plaintext)

        Args:
        - `plaintext` — Plaintext column or constant to decode. [`String`](/sql-reference/data-types/string)

        Returns a string containing the encoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("base64Encode", *to_args(locals()))
    
    @staticmethod
    def base64URLDecode(encoded: Any) -> Function:
        """
        base64URLDecode(encoded)

        Args:
        - `encoded` — String column or constant to encode. If the string is not valid Base64-encoded, an exception is thrown. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("base64URLDecode", *to_args(locals()))
    
    @staticmethod
    def base64URLEncode(plaintext: Any) -> Function:
        """
        base64URLEncode(plaintext)

        Args:
        - `plaintext` — Plaintext column or constant to encode. [`String`](/sql-reference/data-types/string)

        Returns a string containing the encoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("base64URLEncode", *to_args(locals()))
    
    @staticmethod
    def basename(expr: Any) -> Function:
        """
        basename(expr)

        Args:
        - `expr` — A string expression. Backslashes must be escaped. [`String`](/sql-reference/data-types/string)

        Returns the tail of the input string after its last slash or backslash. If the input string ends with a slash or backslash, the function returns an empty string. Returns the original string if there are no slashes or backslashes. [`String`](/sql-reference/data-types/string)
        """
        return Function("basename", *to_args(locals()))
    
    @staticmethod
    def bech32Decode(address: Any) -> Function:
        """
        bech32Decode(address)

        Args:
        - `address` — A Bech32 string to decode. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns a tuple consisting of `(hrp, data)` that was used to encode the string. The data is in binary format. [`Tuple(String, String)`](/sql-reference/data-types/tuple)
        """
        return Function("bech32Decode", *to_args(locals()))
    
    @staticmethod
    def bech32Encode(hrp: Any, data: Any, witver: Any | None = None) -> Function:
        """
        bech32Encode(hrp, data[, witver])

        Args:
        - `hrp` — A String of `1 - 83` lowercase characters specifying the "human-readable part" of the code. Usually 'bc' or 'tb'. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `data` — A String of binary data to encode. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `witver` — Optional. The witness version (default = 1). An `UInt*` specifying the version of the algorithm to run. `0` for Bech32 and `1` or greater for Bech32m. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns a Bech32 address string, consisting of the human-readable part, a separator character which is always '1', and a data part. The length of the string will never exceed 90 characters. If the algorithm cannot generate a valid address from the input, it will return an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("bech32Encode", *to_args(locals()))
    
    @staticmethod
    def bin(arg: Any) -> Function:
        """
        bin(arg)

        Args:
        - `arg` — A value to convert to binary. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns a string with the binary representation of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("bin", *to_args(locals()))
    
    @staticmethod
    def bitAnd(a: Any, b: Any) -> Function:
        """
        bitAnd(a, b)

        Args:
        - `a` — First value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `b` — Second value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the result of bitwise operation `a AND b`
        """
        return Function("bitAnd", *to_args(locals()))
    
    @staticmethod
    def bitCount(x: Any) -> Function:
        """
        bitCount(x)

        Args:
        - `x` — An integer or float value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the number of bits set to one in `x`. [`UInt8`](../data-types/int-uint.md).

        note
        The function does not convert the input value to a larger type ([sign extension](https://en.wikipedia.org/wiki/Sign_extension)).
        For example: `bitCount(toUInt8(-1)) = 8`.

        """
        return Function("bitCount", *to_args(locals()))
    
    @staticmethod
    def bitHammingDistance(x: Any, y: Any) -> Function:
        """
        bitHammingDistance(x, y)

        Args:
        - `x` — First number for Hamming distance calculation. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `y` — Second number for Hamming distance calculation. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the hamming distance between `x` and `y` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitHammingDistance", *to_args(locals()))
    
    @staticmethod
    def bitNot(a: Any) -> Function:
        """
        bitNot(a)

        Args:
        - `a` — Value for which to apply bitwise NOT operation. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns the result of `~a` i.e `a` with bits flipped.
        """
        return Function("bitNot", *to_args(locals()))
    
    @staticmethod
    def bitOr(a: Any, b: Any) -> Function:
        """
        bitOr(a, b)

        Args:
        - `a` — First value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `b` — Second value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the result of bitwise operation `a OR b`
        """
        return Function("bitOr", *to_args(locals()))
    
    @staticmethod
    def bitPositionsToArray(arg: Any) -> Function:
        """
        bitPositionsToArray(arg)

        Args:
        - `arg` — An integer value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array with the ascendingly ordered positions of 1 bits in the binary representation of the input. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("bitPositionsToArray", *to_args(locals()))
    
    @staticmethod
    def bitRotateLeft(a: Any, N: Any) -> Function:
        """
        bitRotateLeft(a, N)

        Args:
        - `a` — A value to rotate. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `N` — The number of positions to rotate left. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the rotated value with type equal to that of `a`. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitRotateLeft", *to_args(locals()))
    
    @staticmethod
    def bitRotateRight(a: Any, N: Any) -> Function:
        """
        bitRotateRight(a, N)

        Args:
        - `a` — A value to rotate. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `N` — The number of positions to rotate right. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the rotated value with type equal to that of `a`. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitRotateRight", *to_args(locals()))
    
    @staticmethod
    def bitShiftLeft(a: Any, N: Any) -> Function:
        """
        bitShiftLeft(a, N)

        Args:
        - `a` — A value to shift. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `N` — The number of positions to shift. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the shifted value with type equal to that of `a`.
        """
        return Function("bitShiftLeft", *to_args(locals()))
    
    @staticmethod
    def bitShiftRight(a: Any, N: Any) -> Function:
        """
        bitShiftRight(a, N)

        Args:
        - `a` — A value to shift. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `N` — The number of positions to shift. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the shifted value with type equal to that of `a`.
        """
        return Function("bitShiftRight", *to_args(locals()))
    
    @staticmethod
    def bitSlice(s: Any, offset: Any, length: Any | None = None) -> Function:
        """
        bitSlice(s, offset[, length])

        Args:
        - `s` — The String or Fixed String to slice. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `offset` — 
        Returns the starting bit position (1-based indexing).
        - Positive values: count from the beginning of the string.
        - Negative values: count from the end of the string.

                 [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `length` — 
        Optional. The number of bits to extract.
        - Positive values: extract `length` bits.
        - Negative values: extract from the offset to `(string_length - |length|)`.
        - Omitted: extract from offset to end of string.
        - If length is not a multiple of 8, the result is padded with zeros on the right.
                 [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns a string containing the extracted bits, represented as a binary sequence. The result is always padded to byte boundaries (multiples of 8 bits) [`String`](/sql-reference/data-types/string)
        """
        return Function("bitSlice", *to_args(locals()))
    
    @staticmethod
    def bitTest(a: Any, i: Any) -> Function:
        """
        bitTest(a, i)

        Args:
        - `a` — Number to convert. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `i` — Position of the bit to return. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the value of the bit at position `i` in the binary representation of `a` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitTest", *to_args(locals()))
    
    @staticmethod
    def bitTestAll(a: Any, index1: Any, index2: Any | None = None, indexN: Any | None = None) -> Function:
        """
        bitTestAll(a, index1[, index2, ... , indexN])

        Args:
        - `a` — An integer value. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `index1, ...` — One or multiple positions of bits. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the result of the logical conjunction [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitTestAll", *to_args(locals()))
    
    @staticmethod
    def bitTestAny(a: Any, index1: Any, index2: Any | None = None, indexN: Any | None = None) -> Function:
        """
        bitTestAny(a, index1[, index2, ... , indexN])

        Args:
        - `a` — An integer value. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `index1, ...` — One or multiple positions of bits. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the result of the logical disjunction [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitTestAny", *to_args(locals()))
    
    @staticmethod
    def bitXor(a: Any, b: Any) -> Function:
        """
        bitXor(a, b)

        Args:
        - `a` — First value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `b` — Second value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the result of bitwise operation `a XOR b`
        """
        return Function("bitXor", *to_args(locals()))
    
    @staticmethod
    def bitmapAnd(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapAnd(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns a bitmap containing bits present in both input bitmaps [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapAnd", *to_args(locals()))
    
    @staticmethod
    def bitmapAndCardinality(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapAndCardinality(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the number of set bits in the intersection of the two bitmaps [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapAndCardinality", *to_args(locals()))
    
    @staticmethod
    def bitmapAndnot(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapAndnot(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns a bitmap containing set bits present in the first bitmap but not in the second [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapAndnot", *to_args(locals()))
    
    @staticmethod
    def bitmapAndnotCardinality(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapAndnotCardinality(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the number of set bits in the result of `bitmap1 AND-NOT bitmap2` [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapAndnotCardinality", *to_args(locals()))
    
    @staticmethod
    def bitmapBuild(array: Any) -> Function:
        """
        bitmapBuild(array)

        Args:
        - `array` — Unsigned integer array. [`Array(UInt*)`](/sql-reference/data-types/array)

        Returns a bitmap from the provided array [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapBuild", *to_args(locals()))
    
    @staticmethod
    def bitmapCardinality(bitmap: Any) -> Function:
        """
        bitmapCardinality(bitmap)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the number of bits set in the bitmap [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapCardinality", *to_args(locals()))
    
    @staticmethod
    def bitmapContains(bitmap: Any, value: Any) -> Function:
        """
        bitmapContains(bitmap, value)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `value` — Element to check for. [(U)Int8/16/32/64](/sql-reference/data-types/int-uint/) 
        Returns `1` if the bitmap contains the specified value, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapContains", *to_args(locals()))
    
    @staticmethod
    def bitmapHasAll(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapHasAll(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns `1` if all set bits of the second bitmap are present in the first bitmap, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapHasAll", *to_args(locals()))
    
    @staticmethod
    def bitmapHasAny(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapHasAny(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns `1` if any bits of the second bitmap are present in the first bitmap, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapHasAny", *to_args(locals()))
    
    @staticmethod
    def bitmapMax(bitmap: Any) -> Function:
        """
        bitmapMax(bitmap)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the position of the greatest bit set in the bitmap, otherwise `0` [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapMax", *to_args(locals()))
    
    @staticmethod
    def bitmapMin(bitmap: Any) -> Function:
        """
        bitmapMin(bitmap)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the position of the smallest bit set in the bitmap, or `UINT32_MAX`/`UINT64_MAX` [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapMin", *to_args(locals()))
    
    @staticmethod
    def bitmapOr(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapOr(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns a bitmap containing set bits present in either input bitmap [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapOr", *to_args(locals()))
    
    @staticmethod
    def bitmapOrCardinality(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapOrCardinality(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the number of set bits in the union of the two bitmaps [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapOrCardinality", *to_args(locals()))
    
    @staticmethod
    def bitmapSubsetInRange(bitmap: Any, start: Any, end: Any) -> Function:
        """
        bitmapSubsetInRange(bitmap, start, end)

        Args:
        - `bitmap` — Bitmap to extract the subset from. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `start` — Start of the range (inclusive). [`UInt*`](/sql-reference/data-types/int-uint) - `end` — End of the range (exclusive). [`UInt*`](/sql-reference/data-types/int-uint) 
        Returns a bitmap containing only the set bits in the specified range [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapSubsetInRange", *to_args(locals()))
    
    @staticmethod
    def bitmapSubsetLimit(bitmap: Any, range_start: Any, cardinality_limit: Any) -> Function:
        """
        bitmapSubsetLimit(bitmap, range_start, cardinality_limit)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `range_start` — Start of the range (inclusive). [`UInt32`](/sql-reference/data-types/int-uint) - `cardinality_limit` — Maximum cardinality of the subset. [`UInt32`](/sql-reference/data-types/int-uint) 
        Returns a bitmap containing at most `cardinality_limit` set bits, starting from `range_start` [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapSubsetLimit", *to_args(locals()))
    
    @staticmethod
    def bitmapToArray(bitmap: Any) -> Function:
        """
        bitmapToArray(bitmap)

        Args:
        - `bitmap` — Bitmap to convert. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns an array of unsigned integers contained in the bitmap [`Array(UInt*)`](/sql-reference/data-types/array)
        """
        return Function("bitmapToArray", *to_args(locals()))
    
    @staticmethod
    def bitmapTransform(bitmap: Any, from_array: Any, to_array: Any) -> Function:
        """
        bitmapTransform(bitmap, from_array, to_array)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `from_array` — Array of original set bits to be replaced. [`Array(T)`](/sql-reference/data-types/array). - `to_array` — Array of new set bits to replace with. [`Array(T)`](/sql-reference/data-types/array). 
        Returns a bitmap with elements transformed according to the given mapping [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapTransform", *to_args(locals()))
    
    @staticmethod
    def bitmapXor(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapXor(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns a bitmap containing set bits present in either input bitmap, but not in both [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("bitmapXor", *to_args(locals()))
    
    @staticmethod
    def bitmapXorCardinality(bitmap1: Any, bitmap2: Any) -> Function:
        """
        bitmapXorCardinality(bitmap1, bitmap2)

        Args:
        - `bitmap1` — First bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `bitmap2` — Second bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). 
        Returns the number of set bits in the symmetric difference of the two bitmaps [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("bitmapXorCardinality", *to_args(locals()))
    
    @staticmethod
    def bitmaskToArray(num: Any) -> Function:
        """
        bitmaskToArray(num)

        Args:
        - `num` — An integer value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an array with the ascendingly ordered powers of two which sum up to the input number. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("bitmaskToArray", *to_args(locals()))
    
    @staticmethod
    def bitmaskToList(num: Any) -> Function:
        """
        bitmaskToList(num)

        Args:
        - `num` — An integer value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a string containing comma-separated powers of two. [`String`](/sql-reference/data-types/string)
        """
        return Function("bitmaskToList", *to_args(locals()))
    
    @staticmethod
    def blockNumber() -> Function:
        """
        blockNumber()

        
        Sequence number of the data block where the row is located. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("blockNumber", *to_args(locals()))
    
    @staticmethod
    def blockSerializedSize(x1: Any, x2: Any | None = None) -> Function:
        """
        blockSerializedSize(x1[, x2[, ...]])

        Args:
        - `x1[, x2, ...]` — Any number of values for which to get the uncompressed size of the block. [`Any`](/sql-reference/data-types)

        Returns the number of bytes that will be written to disk for a block of values without compression. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("blockSerializedSize", *to_args(locals()))
    
    @staticmethod
    def blockSize() -> Function:
        """
        blockSize()

        
        Returns the number of rows in the current block. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("blockSize", *to_args(locals()))
    
    @staticmethod
    def boundingRatio(x: Any, y: Any) -> Function:
        """
        boundingRatio(x, y)

        Args:
        - `x` — X-coordinate values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Y-coordinate values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the slope of the line between the leftmost and rightmost points, otherwise returns `NaN` if the data is empty. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("boundingRatio", *to_args(locals()))
    
    @staticmethod
    def buildId() -> Function:
        """
        buildId()

        
        Returns the build ID. [`String`](/sql-reference/data-types/string)
        """
        return Function("buildId", *to_args(locals()))
    
    @staticmethod
    def byteHammingDistance(s1: Any, s2: Any) -> Function:
        """
        byteHammingDistance(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the Hamming distance between the two strings. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("byteHammingDistance", *to_args(locals()))
    
    @staticmethod
    def byteSize(arg1: Any, arg2: Any | None = None) -> Function:
        """
        byteSize(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — Values of any data type for which to estimate the uncompressed byte size. [`Any`](/sql-reference/data-types)

        Returns an estimation of the byte size of the arguments in memory. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("byteSize", *to_args(locals()))
    
    @staticmethod
    def byteSwap(x: Any) -> Function:
        """
        byteSwap(x)

        Args:
        - `x` — An integer value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns `x` with bytes reversed. [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("byteSwap", *to_args(locals()))
    
    @staticmethod
    def caseFoldUTF8(str: Any) -> Function:
        """
        caseFoldUTF8(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        Case-folded UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("caseFoldUTF8", *to_args(locals()))
    
    @staticmethod
    def caseWithExpression(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("caseWithExpression", *to_args(locals()))
    
    @staticmethod
    def catboostEvaluate(path_to_model: Any, feature_1: Any, feature_2: Any | None = None, feature_n: Any | None = None) -> Function:
        """
        catboostEvaluate(path_to_model, feature_1[, feature_2, ..., feature_n])

        Args:
        - `path_to_model` — Path to catboost model. [`const String`](/sql-reference/data-types/string)
        - `feature` — One or more model features/arguments. [`Float*`](/sql-reference/data-types/float)

        Returns the model evaluation result. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("catboostEvaluate", *to_args(locals()))
    
    @staticmethod
    def categoricalInformationValue(category1: Any, category2: Any | None = None, tag: Any | None = None) -> Function:
        """
        categoricalInformationValue(category1[, category2, ...,]tag)

        Args:
        - `category1, category2, ...` — One or more categorical features to analyze. Each category should contain discrete values. [`UInt8`](/sql-reference/data-types/int-uint)
        - `tag` — Binary target variable for prediction. Should contain values 0 and 1. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns an array of Float64 values representing the information value for each unique combination of categories. Each value indicates the predictive strength of that category combination for the target variable. [`Array(Float64)`](/sql-reference/data-types/array)
        """
        return Function("categoricalInformationValue", *to_args(locals()))
    
    @staticmethod
    def cbrt(x: Any) -> Function:
        """
        cbrt(x)

        Args:
        - `x` — The value for which to find the cubic root of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the cubic root of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("cbrt", *to_args(locals()))
    
    @staticmethod
    def ceil(x: Any, N: Any | None = None) -> Function:
        """
        ceiling(x[, N])

        Args:
        - `x` — The value to round. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `N` — Optional. The number of decimal places to round to. Defaults to zero, which means rounding to an integer. Can be negative. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a rounded number of the same type as `x`. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("ceil", *to_args(locals()))
    
    @staticmethod
    def changeDay(date_or_datetime: Any, value: Any) -> Function:
        """
        changeDay(date_or_datetime, value)

        Args:
        - `date_or_datetime` — The value to change. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `value` — The new value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of the same type as `date_or_datetime` with modified day component. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("changeDay", *to_args(locals()))
    
    @staticmethod
    def changeHour(date_or_datetime: Any, value: Any) -> Function:
        """
        changeHour(date_or_datetime, value)

        Args:
        - `date_or_datetime` — The value to change. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `value` — The new value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of the same type as `date_or_datetime` with modified hour component. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("changeHour", *to_args(locals()))
    
    @staticmethod
    def changeMinute(date_or_datetime: Any, value: Any) -> Function:
        """
        changeMinute(date_or_datetime, value)

        Args:
        - `date_or_datetime` — The value to change. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `value` — The new value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of the same type as `date_or_datetime` with modified minute component. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("changeMinute", *to_args(locals()))
    
    @staticmethod
    def changeMonth(date_or_datetime: Any, value: Any) -> Function:
        """
        changeMonth(date_or_datetime, value)

        Args:
        - `date_or_datetime` — The value to change. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `value` — The new value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of the same type as `date_or_datetime` with modified month component. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("changeMonth", *to_args(locals()))
    
    @staticmethod
    def changeSecond(date_or_datetime: Any, value: Any) -> Function:
        """
        changeSecond(date_or_datetime, value)

        Args:
        - `date_or_datetime` — The value to change. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `value` — The new value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of the same type as `date_or_datetime` with modified seconds component. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("changeSecond", *to_args(locals()))
    
    @staticmethod
    def changeYear(date_or_datetime: Any, value: Any) -> Function:
        """
        changeYear(date_or_datetime, value)

        Args:
        - `date_or_datetime` — The value to change. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `value` — The new value. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of the same type as `date_or_datetime` with modified year component. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("changeYear", *to_args(locals()))
    
    @staticmethod
    def char(num1: Any, num2: Any | None = None) -> Function:
        """
        char(num1[, num2[, ...]])

        Args:
        - `num1[, num2[, num3 ...]]` — Numerical arguments interpreted as integers. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns a string of the given bytes. [`String`](/sql-reference/data-types/string)
        """
        return Function("char", *to_args(locals()))
    
    @staticmethod
    def cityHash64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        cityHash64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("cityHash64", *to_args(locals()))
    
    @staticmethod
    def clamp(value: Any, min: Any, max: Any) -> Function:
        """
        clamp(value, min, max)

        Args:
        - `value` — The value to clamp. - `min` — The minimum bound. - `max` — The maximum bound. 
        Returns the value, restricted to the [min, max] range.
        """
        return Function("clamp", *to_args(locals()))
    
    @staticmethod
    def coalesce(x: Any, y: Any | None = None) -> Function:
        """
        coalesce(x[, y, ...])

        Args:
        - `x[, y, ...]` — Any number of parameters of non-compound type. All parameters must be of mutually compatible data types. [`Any`](/sql-reference/data-types)

        Returns the first non-`NULL` argument, otherwise `NULL`, if all arguments are `NULL`. [`Any`](/sql-reference/data-types) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("coalesce", *to_args(locals()))
    
    @staticmethod
    def colorOKLABToSRGB(tuple: Any, gamma: Any | None = None) -> Function:
        """
        colorOKLABToSRGB(tuple [, gamma])

        Args:
        - `tuple` — A tuple of three numeric values `L`, `a`, `b`, where `L` is in the range `[0...1]`. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        - `gamma` — Optional. The exponent that is used to transform linear sRGB back to sRGB by applying `(x ^ (1 / gamma)) * 255` for each channel `x`. Defaults to `2.2`. [`Float64`](/sql-reference/data-types/float)

        Returns a tuple (R, G, B) representing sRGB color values. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("colorOKLABToSRGB", *to_args(locals()))
    
    @staticmethod
    def colorOKLCHToSRGB(tuple: Any, gamma: Any | None = None) -> Function:
        """
        colorOKLCHToSRGB(tuple [, gamma])

        Args:
        - `tuple` — A tuple of three numeric values `L`, `C`, `H`, where `L` is in the range `[0...1]`, `C >= 0` and `H` is in the range `[0...360]`. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        - `gamma` — Optional. The exponent that is used to transform linear sRGB back to sRGB by applying `(x ^ (1 / gamma)) * 255` for each channel `x`. Defaults to `2.2`. [`Float64`](/sql-reference/data-types/float)

        Returns a tuple (R, G, B) representing sRGB color values. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("colorOKLCHToSRGB", *to_args(locals()))
    
    @staticmethod
    def colorSRGBToOKLAB(tuple: Any, gamma: Any | None = None) -> Function:
        """
        colorSRGBToOKLAB(tuple[, gamma])

        Args:
        - `tuple` — Tuple of three values R, G, B in the range `[0...255]`. [`Tuple(UInt8, UInt8, UInt8)`](/sql-reference/data-types/tuple)
        - `gamma` — Optional. Exponent that is used to linearize sRGB by applying `(x / 255)^gamma` to each channel `x`. Defaults to `2.2`. [`Float64`](/sql-reference/data-types/float)

        Returns a tuple (L, a, b) representing the OKLAB color space values. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("colorSRGBToOKLAB", *to_args(locals()))
    
    @staticmethod
    def colorSRGBToOKLCH(tuple: Any, gamma: Any | None = None) -> Function:
        """
        colorSRGBToOKLCH(tuple[, gamma])

        Args:
        - `tuple` — Tuple of three values R, G, B in the range `[0...255]`. [`Tuple(UInt8, UInt8, UInt8)`](/sql-reference/data-types/tuple)
        - `gamma` — Optional. Exponent that is used to linearize sRGB by applying `(x / 255)^gamma` to each channel `x`. Defaults to `2.2`. [`Float64`](/sql-reference/data-types/float)

        Returns a tuple (L, C, H) representing the OKLCH color space values. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("colorSRGBToOKLCH", *to_args(locals()))
    
    @staticmethod
    def compareSubstrings(s1: Any, s2: Any, s1_offset: Any, s2_offset: Any, num_bytes: Any) -> Function:
        """
        compareSubstrings(s1, s2, s1_offset, s2_offset, num_bytes)

        Args:
        - `s1` — The first string to compare. [`String`](/sql-reference/data-types/string)
        - `s2` — The second string to compare. [`String`](/sql-reference/data-types/string)
        - `s1_offset` — The position (zero-based) in `s1` from which the comparison starts. [`UInt*`](/sql-reference/data-types/int-uint)
        - `s2_offset` — The position (zero-based index) in `s2` from which the comparison starts. [`UInt*`](/sql-reference/data-types/int-uint)
        - `num_bytes` — The maximum number of bytes to compare in both strings. If `s1_offset` (or `s2_offset`) + `num_bytes` exceeds the end of an input string, `num_bytes` will be reduced accordingly. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns:
        - `-1` if `s1`[`s1_offset` : `s1_offset` + `num_bytes`] < `s2`[`s2_offset` : `s2_offset` + `num_bytes`].
        - `0` if `s1`[`s1_offset` : `s1_offset` + `num_bytes`] = `s2`[`s2_offset` : `s2_offset` + `num_bytes`].
        - `1` if `s1`[`s1_offset` : `s1_offset` + `num_bytes`] > `s2`[`s2_offset` : `s2_offset` + `num_bytes`].
             [`Int8`](/sql-reference/data-types/int-uint)
        """
        return Function("compareSubstrings", *to_args(locals()))
    
    @staticmethod
    def concat(s1: Any | None = None, s2: Any | None = None) -> Function:
        """
        concat([s1, s2, ...])

        Args:
        - `s1, s2, ...` — Any number of values of arbitrary type. [`Any`](/sql-reference/data-types)

        Returns the String created by concatenating the arguments. If any of arguments is `NULL`, the function returns `NULL`. If there are no arguments, it returns an empty string. [`Nullable(String)`](/sql-reference/data-types/nullable)
        """
        return Function("concat", *to_args(locals()))
    
    @staticmethod
    def concatAssumeInjective(s1: Any | None = None, s2: Any | None = None) -> Function:
        """
        concatAssumeInjective([s1, s2, ...])

        Args:
        - `s1, s2, ...` — Any number of values of arbitrary type. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the string created by concatenating the arguments. If any of argument values is `NULL`, the function returns `NULL`. If no arguments are passed, it returns an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("concatAssumeInjective", *to_args(locals()))
    
    @staticmethod
    def concatWithSeparator(sep: Any, exp1: Any | None = None, exp2: Any | None = None) -> Function:
        """
        concatWithSeparator(sep[, exp1, exp2, ...])

        Args:
        - `sep` — The separator to use. [`const String`](/sql-reference/data-types/string) or [`const FixedString`](/sql-reference/data-types/fixedstring)
        - `exp1, exp2, ...` — Expression to be concatenated. Arguments which are not of type `String` or `FixedString` are converted to strings using their default serialization. As this decreases performance, it is not recommended to use non-String/FixedString arguments. [`Any`](/sql-reference/data-types)

        Returns the String created by concatenating the arguments. If any of the argument values is `NULL`, the function returns `NULL`. [`String`](/sql-reference/data-types/string)
        """
        return Function("concatWithSeparator", *to_args(locals()))
    
    @staticmethod
    def concatWithSeparatorAssumeInjective(sep: Any, exp1: Any | None = None, exp2: Any | None = None) -> Function:
        """
        concatWithSeparatorAssumeInjective(sep[, exp1, exp2, ... ])

        Args:
        - `sep` — The separator to use. [`const String`](/sql-reference/data-types/string) or [`const FixedString`](/sql-reference/data-types/fixedstring)
        - `exp1, exp2, ...` — Expression to be concatenated. Arguments which are not of type `String` or `FixedString` are converted to strings using their default serialization. As this decreases performance, it is not recommended to use non-String/FixedString arguments. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the String created by concatenating the arguments. If any of the argument values is `NULL`, the function returns `NULL`. [`String`](/sql-reference/data-types/string)
        """
        return Function("concatWithSeparatorAssumeInjective", *to_args(locals()))
    
    @staticmethod
    def connectionId() -> Function:
        """
        connectionId()

        
        Returns the connection ID of the current client. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("connectionId", *to_args(locals()))
    
    @staticmethod
    def contingency(column1: Any, column2: Any) -> Function:
        """
        contingency(column1, column2)

        Args:
        - `column1` — First column to compare. [`Any`](/sql-reference/data-types)
        - `column2` — Second column to compare. [`Any`](/sql-reference/data-types)

        Returns a value between 0 and 1. The larger the result, the closer the association of the two columns. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("contingency", *to_args(locals()))
    
    @staticmethod
    def conv(number: Any, from_base: Any, to_base: Any) -> Function:
        """
        conv(number, from_base, to_base)

        Args:
        - `number` — The number to convert. Can be a string or numeric type. - `from_base` — The source base (2-36). Must be an integer. - `to_base` — The target base (2-36). Must be an integer. 
        String representation of the number in the target base.
        """
        return Function("conv", *to_args(locals()))
    
    @staticmethod
    def convertCharset(s: Any, from_: Any, to: Any) -> Function:
        """
        convertCharset(s, from, to)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)
        - `from` — Source character encoding. [`String`](/sql-reference/data-types/string)
        - `to` — Target character encoding. [`String`](/sql-reference/data-types/string)

        Returns string `s` converted from encoding `from` to encoding `to`. [`String`](/sql-reference/data-types/string)
        """
        return Function("convertCharset", *to_args(locals()))
    
    @staticmethod
    def corr(x: Any, y: Any) -> Function:
        """
        corr(x, y)

        Args:
        - `x` — First variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `y` — Second variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the Pearson correlation coefficient. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("corr", *to_args(locals()))
    
    @staticmethod
    def corrMatrix(x1: Any, x2: Any | None = None) -> Function:
        """
        corrMatrix(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — One or more parameters for which to compute the correlation matrix over. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the correlation matrix. [`Array(Array(Float64))`](/sql-reference/data-types/array)
        """
        return Function("corrMatrix", *to_args(locals()))
    
    @staticmethod
    def corrStable(x: Any, y: Any) -> Function:
        """
        corrStable(x, y)

        Args:
        - `x` — First variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the Pearson correlation coefficient. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("corrStable", *to_args(locals()))
    
    @staticmethod
    def cos(x: Any) -> Function:
        """
        cos(x)

        Args:
        - `x` — The angle in radians. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the cosine of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("cos", *to_args(locals()))
    
    @staticmethod
    def cosh(x: Any) -> Function:
        """
        cosh(x)

        Args:
        - `x` — The angle, in radians. Values from the interval: `-∞ < x < +∞`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns values from the interval: `1 ≤ cosh(x) < +∞` [`Float64`](/sql-reference/data-types/float)
        """
        return Function("cosh", *to_args(locals()))
    
    @staticmethod
    def cosineDistance(vector1: Any, vector2: Any) -> Function:
        """
        cosineDistance(vector1, vector2)

        Args:
        - `vector1` — First tuple. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)
        - `vector2` — Second tuple. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the cosine of the angle between two vectors subtracted from one. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("cosineDistance", *to_args(locals()))
    
    @staticmethod
    def cosineDistanceTransposed(vector1: Any, vector2: Any, p: Any) -> Function:
        """
        cosineDistanceTransposed(vector1, vector2, p)

        Args:
        - `vectors` — Vectors. [`QBit(T, UInt64)`](/sql-reference/data-types/qbit)
        - `reference` — Reference vector. [`Array(T)`](/sql-reference/data-types/array)
        - `p` — Number of bits from each vector element to use in the distance calculation (1 to element bit-width). The quantization level controls the precision-speed trade-off. Using fewer bits results in faster I/O and calculations with reduced accuracy, while using more bits increases accuracy at the cost of performance. [`UInt`](/sql-reference/data-types/int-uint)

        Returns the approximate cosine of the angle between two vectors subtracted from one. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("cosineDistanceTransposed", *to_args(locals()))
    
    @staticmethod
    def count(expr: Any | None = None) -> Function:
        """
        count([expr])

        Args:
        - `expr` — Optional. An expression. The function counts how many times this expression returned not null. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns the a row count if the function is called without parameters, otherwise returns a count of how many times the passed expression returned not null. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("count", *to_args(locals()))
    
    @staticmethod
    def countDigits(x: Any) -> Function:
        """
        countDigits(x)

        Args:
        - `x` — An integer or decimal value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the number of digits needed to represent `x`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("countDigits", *to_args(locals()))
    
    @staticmethod
    def countEqual(arr: Any, x: Any) -> Function:
        """
        countEqual(arr, x)

        Args:
        - `arr` — Array to search. [`Array(T)`](/sql-reference/data-types/array)
        - `x` — Value in the array to count. Any type. 
        Returns the number of elements in the array equal to `x` [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("countEqual", *to_args(locals()))
    
    @staticmethod
    def countMatches(haystack: Any, pattern: Any) -> Function:
        """
        countMatches(haystack, pattern)

        Args:
        - `haystack` — The string to search in. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expression pattern. [`String`](/sql-reference/data-types/string)

        Returns the number of matches found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("countMatches", *to_args(locals()))
    
    @staticmethod
    def countMatchesCaseInsensitive(haystack: Any, pattern: Any) -> Function:
        """
        countMatchesCaseInsensitive(haystack, pattern)

        Args:
        - `haystack` — The string to search in. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expression pattern. [`const String`](/sql-reference/data-types/string)

        Returns the number of matches found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("countMatchesCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def countSubstrings(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        countSubstrings(haystack, needle[, start_pos])

        Args:
        - `haystack` — String in which the search is performed. [String](../../sql-reference/data-types/string.md) or [Enum](../../sql-reference/data-types/enum.md). - `needle` — Substring to be searched. [String](../../sql-reference/data-types/string.md). - `start_pos` — Position (1-based) in `haystack` at which the search starts. [UInt](../../sql-reference/data-types/int-uint.md). Optional. 
        The number of occurrences. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("countSubstrings", *to_args(locals()))
    
    @staticmethod
    def countSubstringsCaseInsensitive(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        countSubstringsCaseInsensitive(haystack, needle[, start_pos])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `start_pos` — Optional. Position (1-based) in `haystack` at which the search starts. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns the number of occurrences of the neddle in the haystack. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("countSubstringsCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def countSubstringsCaseInsensitiveUTF8(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        countSubstringsCaseInsensitiveUTF8(haystack, needle[, start_pos])

        Args:
        - `haystack` — UTF-8 string in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `start_pos` — Optional. Position (1-based) in `haystack` at which the search starts. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns the number of occurrences of the needle in the haystack. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("countSubstringsCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def covarPop(x: Any, y: Any) -> Function:
        """
        covarPop(x, y)

        Args:
        - `x` — First variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the population covariance between `x` and `y`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("covarPop", *to_args(locals()))
    
    @staticmethod
    def covarPopMatrix(x1: Any, x2: Any | None = None) -> Function:
        """
        covarPopMatrix(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — A variable number of parameters. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the population covariance matrix. [`Array(Array(Float64))`](/sql-reference/data-types/array)
        """
        return Function("covarPopMatrix", *to_args(locals()))
    
    @staticmethod
    def covarPopStable(x: Any, y: Any) -> Function:
        """
        covarPopStable(x, y)

        Args:
        - `x` — First variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the population covariance between `x` and `y`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("covarPopStable", *to_args(locals()))
    
    @staticmethod
    def covarSamp(x: Any, y: Any) -> Function:
        """
        covarSamp(x, y)

        Args:
        - `x` — First variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the sample covariance between `x` and `y`. For `n <= 1`, `nan` is returned. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("covarSamp", *to_args(locals()))
    
    @staticmethod
    def covarSampMatrix(x1: Any, x2: Any | None = None) -> Function:
        """
        covarSampMatrix(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — One or more parameters over which to compute the sample covariance matrix. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the sample covariance matrix. [`Array(Array(Float64))`](/sql-reference/data-types/array)
        """
        return Function("covarSampMatrix", *to_args(locals()))
    
    @staticmethod
    def covarSampStable(x: Any, y: Any) -> Function:
        """
        covarSampStable(x, y)

        Args:
        - `x` — First variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second variable. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the sample covariance between `x` and `y`. For `n <= 1`, `inf` is returned. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("covarSampStable", *to_args(locals()))
    
    @staticmethod
    def cramersV(column1: Any, column2: Any) -> Function:
        """
        cramersV(column1, column2)

        Args:
        - `column1` — First column to be compared. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `column2` — Second column to be compared. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a value between 0 (corresponding to no association between the columns' values) to 1 (complete association). [`Float64`](/sql-reference/data-types/float)
        """
        return Function("cramersV", *to_args(locals()))
    
    @staticmethod
    def cramersVBiasCorrected(column1: Any, column2: Any) -> Function:
        """
        cramersVBiasCorrected(column1, column2)

        Args:
        - `column1` — First column to be compared. [`Any`](/sql-reference/data-types)
        - `column2` — Second column to be compared. [`Any`](/sql-reference/data-types)

        Returns a value between 0 (corresponding to no association between the columns' values) to 1 (complete association). [`Float64`](/sql-reference/data-types/float)
        """
        return Function("cramersVBiasCorrected", *to_args(locals()))
    
    @staticmethod
    def cume_dist(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("cume_dist", *to_args(locals()))
    
    @staticmethod
    def currentDatabase() -> Function:
        """
        currentDatabase()

        
        Returns the current database name. [`String`](/sql-reference/data-types/string)
        """
        return Function("currentDatabase", *to_args(locals()))
    
    @staticmethod
    def currentProfiles() -> Function:
        """
        currentProfiles()

        
        Returns an array of setting profiles for the current user. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("currentProfiles", *to_args(locals()))
    
    @staticmethod
    def currentQueryID() -> Function:
        """
        currentQueryID()

        
        
        """
        return Function("currentQueryID", *to_args(locals()))
    
    @staticmethod
    def currentRoles() -> Function:
        """
        currentRoles()

        
        Returns an array of the roles which are assigned to the current user. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("currentRoles", *to_args(locals()))
    
    @staticmethod
    def currentSchemas(bool: Any) -> Function:
        """
        currentSchemas(bool)

        Args:
        - `bool` — A boolean value, which is ignored. [`Bool`](/sql-reference/data-types/boolean)

        Returns a single-element array with the name of the current database. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("currentSchemas", *to_args(locals()))
    
    @staticmethod
    def currentUser() -> Function:
        """
        currentUser()

        
        Returns the name of the current user, otherwise the login of the user who initiated the query. [`String`](/sql-reference/data-types/string)
        """
        return Function("currentUser", *to_args(locals()))
    
    @staticmethod
    def cutFragment(url: Any) -> Function:
        """
        cutFragment(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the URL with fragment identifier removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutFragment", *to_args(locals()))
    
    @staticmethod
    def cutIPv6(x: Any, bytesToCutForIPv6: Any, bytesToCutForIPv4: Any) -> Function:
        """
        cutIPv6(x, bytesToCutForIPv6, bytesToCutForIPv4)

        Args:
        - `x` — IPv6 address in binary format. [`FixedString(16)`](/sql-reference/data-types/fixedstring) or [`IPv6`](/sql-reference/data-types/ipv6)
        - `bytesToCutForIPv6` — Number of bytes to cut for IPv6. [`UInt8`](/sql-reference/data-types/int-uint)
        - `bytesToCutForIPv4` — Number of bytes to cut for IPv4. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a string containing the IPv6 address in text format with specified bytes removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutIPv6", *to_args(locals()))
    
    @staticmethod
    def cutQueryString(url: Any) -> Function:
        """
        cutQueryString(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the URL with query string removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutQueryString", *to_args(locals()))
    
    @staticmethod
    def cutQueryStringAndFragment(url: Any) -> Function:
        """
        cutQueryStringAndFragment(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the URL with query string and fragment identifier removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutQueryStringAndFragment", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomain(url: Any) -> Function:
        """
        cutToFirstSignificantSubdomain(url)

        Args:
        - `url` — URL or domain string to process. [`String`](/sql-reference/data-types/string)

        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain if possible, otherwise returns an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomain", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainCustom(url: Any, tld_list_name: Any) -> Function:
        """
        cutToFirstSignificantSubdomainCustom(url, tld_list_name)

        Args:
        - `url` — URL or domain string to process. [`String`](/sql-reference/data-types/string)
        - `tld_list_name` — Name of the custom TLD list configured in ClickHouse. [`const String`](/sql-reference/data-types/string)

        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainCustom", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainCustomRFC(url: Any, tld_list_name: Any) -> Function:
        """
        cutToFirstSignificantSubdomainCustomRFC(url, tld_list_name)

        Args:
        - `url` — URL or domain string to process according to RFC 3986. - `tld_list_name` — Name of the custom TLD list configured in ClickHouse. 
        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainCustomRFC", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainCustomWithWWW(url: Any, tld_list_name: Any) -> Function:
        """
        cutToFirstSignificantSubdomainCustomWithWWW(url, tld_list_name)

        Args:
        - `url` — URL or domain string to process. - `tld_list_name` — Name of the custom TLD list configured in ClickHouse. 
        Part of the domain that includes top-level subdomains up to the first significant subdomain without stripping 'www'. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainCustomWithWWW", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainCustomWithWWWRFC(url: Any, tld_list_name: Any) -> Function:
        """
        cutToFirstSignificantSubdomainCustomWithWWWRFC(url, tld_list_name)

        Args:
        - `url` — URL or domain string to process according to RFC 3986. - `tld_list_name` — Name of the custom TLD list configured in ClickHouse. 
        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain without stripping `www`. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainCustomWithWWWRFC", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainRFC(url: Any) -> Function:
        """
        cutToFirstSignificantSubdomainRFC(url)

        Args:
        - `url` — URL or domain string to process according to RFC 3986. [`String`](/sql-reference/data-types/string)

        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain if possible, otherwise returns an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainRFC", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainWithWWW(url: Any) -> Function:
        """
        cutToFirstSignificantSubdomainWithWWW(url)

        Args:
        - `url` — URL or domain string to process. [`String`](/sql-reference/data-types/string)

        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain (with www) if possible, otherwise returns an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainWithWWW", *to_args(locals()))
    
    @staticmethod
    def cutToFirstSignificantSubdomainWithWWWRFC(url: Any) -> Function:
        """
        cutToFirstSignificantSubdomainWithWWWRFC(url)

        Args:
        - `url` — URL or domain string to process according to RFC 3986. 
        Returns the part of the domain that includes top-level subdomains up to the first significant subdomain (with 'www') if possible, otherwise returns an empty string [`String`](/sql-reference/data-types/string)
        """
        return Function("cutToFirstSignificantSubdomainWithWWWRFC", *to_args(locals()))
    
    @staticmethod
    def cutURLParameter(url: Any, name: Any) -> Function:
        """
        cutURLParameter(url, name)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)
        - `name` — Name of URL parameter. [`String`](/sql-reference/data-types/string) or [`Array(String)`](/sql-reference/data-types/array)

        URL with `name` URL parameter removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutURLParameter", *to_args(locals()))
    
    @staticmethod
    def cutWWW(url: Any) -> Function:
        """
        cutWWW(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the URL with leading `www.` removed from the domain. [`String`](/sql-reference/data-types/string)
        """
        return Function("cutWWW", *to_args(locals()))
    
    @staticmethod
    def damerauLevenshteinDistance(s1: Any, s2: Any) -> Function:
        """
        damerauLevenshteinDistance(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the Damerau-Levenshtein distance between the two strings. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("damerauLevenshteinDistance", *to_args(locals()))
    
    @staticmethod
    def dateDiff(unit: Any, startdate: Any, enddate: Any, timezone: Any | None = None) -> Function:
        """
        dateDiff(unit, startdate, enddate[, timezone])

        Args:
        - `unit` — The type of interval for result.

        | Unit        | Possible values                           |
        |-------------|-------------------------------------------|
        | nanosecond  | `nanosecond`, `nanoseconds`, `ns`         |
        | microsecond | `microsecond`, `microseconds`, `us`, `u`  |
        | millisecond | `millisecond`, `milliseconds`, `ms`       |
        | second      | `second`, `seconds`, `ss`, `s`            |
        | minute      | `minute`, `minutes`, `mi`, `n`            |
        | hour        | `hour`, `hours`, `hh`, `h`                |
        | day         | `day`, `days`, `dd`, `d`                  |
        | week        | `week`, `weeks`, `wk`, `ww`               |
        | month       | `month`, `months`, `mm`, `m`              |
        | quarter     | `quarter`, `quarters`, `qq`, `q`          |
        | year        | `year`, `years`, `yyyy`, `yy`             |
         - `startdate` — The first time value to subtract (the subtrahend). [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `enddate` — The second time value to subtract from (the minuend). [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone name. If specified, it is applied to both `startdate` and `enddate`. If not specified, timezones of `startdate` and `enddate` are used. If they are not the same, the result is unspecified. [`String`](/sql-reference/data-types/string)

        Returns the difference between `enddate` and `startdate` expressed in `unit`. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("dateDiff", *to_args(locals()))
    
    @staticmethod
    def dateName(date_part: Any, date: Any, timezone: Any | None = None) -> Function:
        """
        dateName(date_part, date[, timezone])

        Args:
        - `date_part` — The part of the date that you want to extract. [`String`](/sql-reference/data-types/string)
        - `datetime` — A date or date with time value. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns the specified part of date. [`String`](/sql-reference/data-types/string)
        """
        return Function("dateName", *to_args(locals()))
    
    @staticmethod
    def dateTime64ToSnowflake(value: Any) -> Function:
        """
        dateTime64ToSnowflake(value)

        Args:
        - `value` — Date with time. [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the input value converted as the first Snowflake ID at that time. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("dateTime64ToSnowflake", *to_args(locals()))
    
    @staticmethod
    def dateTime64ToSnowflakeID(value: Any, epoch: Any | None = None) -> Function:
        """
        dateTime64ToSnowflakeID(value[, epoch])

        Args:
        - `value` — Date with time. [`DateTime64`](/sql-reference/data-types/datetime64)
        - `epoch` — Epoch of the Snowflake ID in milliseconds since 1970-01-01. Defaults to 0 (1970-01-01). For the Twitter/X epoch (2015-01-01), provide 1288834974657. [`UInt*`](/sql-reference/data-types/int-uint)

        Input value converted to [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("dateTime64ToSnowflakeID", *to_args(locals()))
    
    @staticmethod
    def dateTimeToSnowflake(value: Any) -> Function:
        """
        dateTimeToSnowflake(value)

        Args:
        - `value` — Date with time. [`DateTime`](/sql-reference/data-types/datetime)

        Returns the input value as the first Snowflake ID at that time. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("dateTimeToSnowflake", *to_args(locals()))
    
    @staticmethod
    def dateTimeToSnowflakeID(value: Any, epoch: Any | None = None) -> Function:
        """
        dateTimeToSnowflakeID(value[, epoch])

        Args:
        - `value` — Date with time. [`DateTime`](/sql-reference/data-types/datetime)
        - `epoch` — Epoch of the Snowflake ID in milliseconds since 1970-01-01. Defaults to 0 (1970-01-01). For the Twitter/X epoch (2015-01-01), provide 1288834974657. [`UInt*`](/sql-reference/data-types/int-uint)

        Input value converted to [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("dateTimeToSnowflakeID", *to_args(locals()))
    
    @staticmethod
    def dateTimeToUUIDv7(value: Any) -> Function:
        """
        dateTimeToUUIDv7(value)

        Args:
        - `value` — Date with time. [`DateTime`](/sql-reference/data-types/datetime)

        Returns a UUIDv7. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("dateTimeToUUIDv7", *to_args(locals()))
    
    @staticmethod
    def dateTrunc(unit: Any, datetime: Any, timezone: Any | None = None) -> Function:
        """
        dateTrunc(unit, datetime[, timezone])

        Args:
        - `unit` — 
        The type of interval to truncate the result. Possible values: `nanosecond` (only DateTime64), `microsecond` (only DateTime64), `millisecond` (only DateTime64), `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`.
         [`String`](/sql-reference/data-types/string)
        - `datetime` — Date and time. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone name for the returned datetime. If not specified, the function uses the timezone of the `datetime` parameter. [`String`](/sql-reference/data-types/string)

        Returns the truncated date and time value.

        | Unit Argument               | `datetime` Argument                   | Return Type                                                                            |
        |-----------------------------|---------------------------------------|----------------------------------------------------------------------------------------|
        | Year, Quarter, Month, Week  | `Date32` or `DateTime64` or `Date` or `DateTime` | [`Date32`](../data-types/date32.md) or [`Date`](../data-types/date.md)                 |
        | Day, Hour, Minute, Second   | `Date32`, `DateTime64`, `Date`, or `DateTime` | [`DateTime64`](../data-types/datetime64.md) or [`DateTime`](../data-types/datetime.md) |
        | Millisecond, Microsecond,   | Any                                   | [`DateTime64`](../data-types/datetime64.md)                                            |
        | Nanosecond                  |                                       | with scale 3, 6, or 9                                                                  |
        """
        return Function("dateTrunc", *to_args(locals()))
    
    @staticmethod
    def decodeHTMLComponent(s: Any) -> Function:
        """
        decodeHTMLComponent(s)

        Args:
        - `s` — String containing HTML entities to decode. [`String`](/sql-reference/data-types/string)

        Returns the string with HTML entities decoded. [`String`](/sql-reference/data-types/string)
        """
        return Function("decodeHTMLComponent", *to_args(locals()))
    
    @staticmethod
    def decodeURLComponent(url: Any) -> Function:
        """
        decodeURLComponent(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the decoded URL. [`String`](/sql-reference/data-types/string)
        """
        return Function("decodeURLComponent", *to_args(locals()))
    
    @staticmethod
    def decodeURLFormComponent(url: Any) -> Function:
        """
        decodeURLFormComponent(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the decoded URL. [`String`](/sql-reference/data-types/string)
        """
        return Function("decodeURLFormComponent", *to_args(locals()))
    
    @staticmethod
    def decodeXMLComponent(s: Any) -> Function:
        """
        decodeXMLComponent(s)

        Args:
        - `s` — String containing XML entities to decode. [`String`](/sql-reference/data-types/string)

        Returns the provided string with XML entities decoded. [`String`](/sql-reference/data-types/string)
        """
        return Function("decodeXMLComponent", *to_args(locals()))
    
    @staticmethod
    def decrypt(mode: Any, ciphertext: Any, key: Any, iv: Any | None = None, aad: Any | None = None) -> Function:
        """
        decrypt(mode, ciphertext, key[, iv, aad])

        Args:
        - `mode` — Decryption mode. [`String`](/sql-reference/data-types/string)
        - `ciphertext` — Encrypted text that should be decrypted. [`String`](/sql-reference/data-types/string)
        - `key` — Decryption key. [`String`](/sql-reference/data-types/string)
        - `iv` — Initialization vector. Required for `-gcm` modes, optional for others. [`String`](/sql-reference/data-types/string)
        - `aad` — Additional authenticated data. Won't decrypt if this value is incorrect. Works only in `-gcm` modes, for others throws an exception. [`String`](/sql-reference/data-types/string)

        Returns decrypted plaintext. [`String`](/sql-reference/data-types/string)
        """
        return Function("decrypt", *to_args(locals()))
    
    @staticmethod
    def defaultProfiles() -> Function:
        """
        defaultProfiles()

        
        Returns an array of default setting profile names for the current user. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("defaultProfiles", *to_args(locals()))
    
    @staticmethod
    def defaultRoles() -> Function:
        """
        defaultRoles()

        
        Returns an array of default roles for the current user. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("defaultRoles", *to_args(locals()))
    
    @staticmethod
    def defaultValueOfArgumentType(expression: Any) -> Function:
        """
        defaultValueOfArgumentType(expression)

        Args:
        - `expression` — Arbitrary type of value or an expression that results in a value of an arbitrary type. [`Any`](/sql-reference/data-types)

        Returns `0` for numbers, an empty string for strings or `NULL` for Nullable types. [`UInt8`](/sql-reference/data-types/int-uint) or [`String`](/sql-reference/data-types/string) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("defaultValueOfArgumentType", *to_args(locals()))
    
    @staticmethod
    def defaultValueOfTypeName(type: Any) -> Function:
        """
        defaultValueOfTypeName(type)

        Args:
        - `type` — A string representing a type name. [`String`](/sql-reference/data-types/string)

        Returns the default value for the given type name: `0` for numbers, an empty string for strings, or `NULL` for Nullable [`UInt8`](/sql-reference/data-types/int-uint) or [`String`](/sql-reference/data-types/string) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("defaultValueOfTypeName", *to_args(locals()))
    
    @staticmethod
    def degrees(x: Any) -> Function:
        """
        degrees(x)

        Args:
        - `x` — Input in radians. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the value of `x` in degrees. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("degrees", *to_args(locals()))
    
    @staticmethod
    def deltaSum(x1: Any, x2: Any | None = None) -> Function:
        """
        deltaSum(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — One or more input values. [`Integer`](/sql-reference/data-types/int-uint) or [`Float`](/sql-reference/data-types/float)

        Returns a gained arithmetic difference of the input values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("deltaSum", *to_args(locals()))
    
    @staticmethod
    def deltaSumTimestamp(value: Any, timestamp: Any) -> Function:
        """
        deltaSumTimestamp(value, timestamp)

        Args:
        - `value` — Input values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `timestamp` — The parameter for order values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns accumulated differences between consecutive values, ordered by the `timestamp` parameter. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("deltaSumTimestamp", *to_args(locals()))
    
    @staticmethod
    def demangle(symbol: Any) -> Function:
        """
        demangle(symbol)

        Args:
        - `symbol` — Symbol from an object file. [`String`](/sql-reference/data-types/string)

        Returns the name of the C++ function, or an empty string if the symbol is not valid. [`String`](/sql-reference/data-types/string)
        """
        return Function("demangle", *to_args(locals()))
    
    @staticmethod
    def denseRank(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("denseRank", *to_args(locals()))
    
    @staticmethod
    def detectCharset(s: Any) -> Function:
        """
        detectCharset(s)

        Args:
        - `s` — The text to analyze. [`String`](/sql-reference/data-types/string)

        Returns a string containing the code of the detected character set [`String`](/sql-reference/data-types/string)
        """
        return Function("detectCharset", *to_args(locals()))
    
    @staticmethod
    def detectLanguage(s: Any) -> Function:
        """
        detectLanguage(s)

        Args:
        - `text_to_be_analyzed` — The text to analyze. [`String`](/sql-reference/data-types/string)

        Returns the 2-letter ISO code of the detected language. Other possible results: `un` = unknown, can not detect any language, `other` = the detected language does not have 2 letter code. [`String`](/sql-reference/data-types/string)
        """
        return Function("detectLanguage", *to_args(locals()))
    
    @staticmethod
    def detectLanguageMixed(s: Any) -> Function:
        """
        detectLanguageMixed(s)

        Args:
        - `s` — The text to analyze [`String`](/sql-reference/data-types/string)

        Returns a map with keys which are 2-letter ISO codes and corresponding values which are a percentage of the text found for that language [`Map(String, Float32)`](/sql-reference/data-types/map)
        """
        return Function("detectLanguageMixed", *to_args(locals()))
    
    @staticmethod
    def detectLanguageUnknown(s: Any) -> Function:
        """
        detectLanguageUnknown('s')

        Args:
        - `s` — The text to analyze. [`String`](/sql-reference/data-types/string)

        Returns the 2-letter ISO code of the detected language. Other possible results: `un` = unknown, can not detect any language, `other` = the detected language does not have 2 letter code. [`String`](/sql-reference/data-types/string)
        """
        return Function("detectLanguageUnknown", *to_args(locals()))
    
    @staticmethod
    def detectTonality(s: Any) -> Function:
        """
        detectTonality(s)

        Args:
        - `s` — The text to be analyzed. [`String`](/sql-reference/data-types/string)

        Returns the average sentiment value of the words in text [`Float32`](/sql-reference/data-types/float)
        """
        return Function("detectTonality", *to_args(locals()))
    
    @staticmethod
    def dictGet(dict_name: Any, attr_names: Any, id_expr: Any) -> Function:
        """
        dictGet('dict_name', attr_names, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_names` — Name of the column of the dictionary, or tuple of column names. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning UInt64/Tuple(T). [`UInt64`](/sql-reference/data-types/int-uint) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to id_expr if the key is found.
        If the key is not found, returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.
        """
        return Function("dictGet", *to_args(locals()))
    
    @staticmethod
    def dictGetAll(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetAll(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetAll", *to_args(locals()))
    
    @staticmethod
    def dictGetChildren(dict_name: Any, key: Any) -> Function:
        """
        dictGetChildren(dict_name, key)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `key` — Key to be checked. [`const String`](/sql-reference/data-types/string)

        Returns the first-level descendants for the key. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("dictGetChildren", *to_args(locals()))
    
    @staticmethod
    def dictGetDate(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetDate(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetDate", *to_args(locals()))
    
    @staticmethod
    def dictGetDateOrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetDateOrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetDateOrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetDateTime(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetDateTime(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetDateTime", *to_args(locals()))
    
    @staticmethod
    def dictGetDateTimeOrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetDateTimeOrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetDateTimeOrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetDescendants(dict_name: Any, key: Any, level: Any) -> Function:
        """
        dictGetDescendants(dict_name, key, level)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `key` — Key to be checked. [`const String`](/sql-reference/data-types/string)
        - `level` — Key to be checked. Hierarchy level. If `level = 0` returns all descendants to the end. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the descendants for the key. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("dictGetDescendants", *to_args(locals()))
    
    @staticmethod
    def dictGetFloat32(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetFloat32(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetFloat32", *to_args(locals()))
    
    @staticmethod
    def dictGetFloat32OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetFloat32OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetFloat32OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetFloat64(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetFloat64(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetFloat64", *to_args(locals()))
    
    @staticmethod
    def dictGetFloat64OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetFloat64OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetFloat64OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetHierarchy(dict_name: Any, key: Any) -> Function:
        """
        dictGetHierarchy(dict_name, key)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `key` — Key value. [`const String`](/sql-reference/data-types/string)

        Returns parents for the key. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("dictGetHierarchy", *to_args(locals()))
    
    @staticmethod
    def dictGetIPv4(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetIPv4(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetIPv4", *to_args(locals()))
    
    @staticmethod
    def dictGetIPv4OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetIPv4OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetIPv4OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetIPv6(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetIPv6(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetIPv6", *to_args(locals()))
    
    @staticmethod
    def dictGetIPv6OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetIPv6OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetIPv6OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetInt16(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetInt16(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt16", *to_args(locals()))
    
    @staticmethod
    def dictGetInt16OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetInt16OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt16OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetInt32(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetInt32(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt32", *to_args(locals()))
    
    @staticmethod
    def dictGetInt32OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetInt32OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt32OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetInt64(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetInt64(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt64", *to_args(locals()))
    
    @staticmethod
    def dictGetInt64OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetInt64OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt64OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetInt8(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetInt8(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt8", *to_args(locals()))
    
    @staticmethod
    def dictGetInt8OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetInt8OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetInt8OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetKeys(dict_name: Any, attr_name: Any, value_expr: Any) -> Function:
        """
        dictGetKeys('dict_name', 'attr_name', value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Attribute to match. [`String`](/sql-reference/data-types/string)
        - `value_expr` — Value to match against the attribute. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        For single key dictionaries: an array of keys whose attribute equals `value_expr`. For multi key dictionaries: an array of tuples of keys whose attribute equals `value_expr`. If there is no attribute corresponding to `value_expr` in the dictionary, then an empty array is returned. ClickHouse throws an exception if it cannot parse the value of the attribute or the value cannot be converted to the attribute data type.
        """
        return Function("dictGetKeys", *to_args(locals()))
    
    @staticmethod
    def dictGetOrDefault(dict_name: Any, attr_names: Any, id_expr: Any, default_value: Any) -> Function:
        """
        dictGetOrDefault('dict_name', attr_names, id_expr, default_value)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_names` — Name of the column of the dictionary, or tuple of column names. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning UInt64/Tuple(T). [`UInt64`](/sql-reference/data-types/int-uint) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value` — Default value to return if the key is not found. Type must match the attribute's data type. 
        Returns the value of the dictionary attribute that corresponds to `id_expr` if the key is found.
        If the key is not found, returns the `default_value` provided.
        """
        return Function("dictGetOrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetOrNull(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetOrNull('dict_name', 'attr_name', id_expr)

        Args:
        - `dict_name` — Name of the dictionary. String literal. - `attr_name` — Name of the column to retrieve. String literal. - `id_expr` — Key value. Expression returning dictionary key-type value. 
        Returns the value of the dictionary attribute that corresponds to `id_expr` if the key is found.
        If the key is not found, returns `NULL`.
        """
        return Function("dictGetOrNull", *to_args(locals()))
    
    @staticmethod
    def dictGetString(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetString(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetString", *to_args(locals()))
    
    @staticmethod
    def dictGetStringOrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetStringOrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetStringOrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt16(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetUInt16(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt16", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt16OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetUInt16OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt16OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt32(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetUInt32(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt32", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt32OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetUInt32OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt32OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt64(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetUInt64(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt64", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt64OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetUInt64OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt64OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt8(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetUInt8(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt8", *to_args(locals()))
    
    @staticmethod
    def dictGetUInt8OrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetUInt8OrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUInt8OrDefault", *to_args(locals()))
    
    @staticmethod
    def dictGetUUID(dict_name: Any, attr_name: Any, id_expr: Any) -> Function:
        """
        dictGetUUID(dict_name, attr_name, id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. An expression returning a dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the content of the `<null_value>` element specified for the attribute in the dictionary configuration.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUUID", *to_args(locals()))
    
    @staticmethod
    def dictGetUUIDOrDefault(dict_name: Any, attr_name: Any, id_expr: Any, default_value_expr: Any) -> Function:
        """
        dictGetUUIDOrDefault(dict_name, attr_name, id_expr, default_value_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `attr_name` — Name of the column of the dictionary. [`String`](/sql-reference/data-types/string) or [`Tuple(String)`](/sql-reference/data-types/tuple)
        - `id_expr` — Key value. Expression returning dictionary key-type value or tuple value (dictionary configuration dependent). [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `default_value_expr` — Value(s) returned if the dictionary does not contain a row with the `id_expr` key. [`Expression`](/sql-reference/data-types/special-data-types/expression) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the value of the dictionary attribute that corresponds to `id_expr`,
        otherwise returns the value passed as the `default_value_expr` parameter.

        note
        ClickHouse throws an exception if it cannot parse the value of the attribute or the value does not match the attribute data type.

        """
        return Function("dictGetUUIDOrDefault", *to_args(locals()))
    
    @staticmethod
    def dictHas(dict_name: Any, id_expr: Any) -> Function:
        """
        dictHas('dict_name', id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `id_expr` — Key value [`const String`](/sql-reference/data-types/string)

        Returns `1` if the key exists, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("dictHas", *to_args(locals()))
    
    @staticmethod
    def dictIsIn(dict_name: Any, child_id_expr: Any, ancestor_id_expr: Any) -> Function:
        """
        dictIsIn(dict_name, child_id_expr, ancestor_id_expr)

        Args:
        - `dict_name` — Name of the dictionary. [`String`](/sql-reference/data-types/string)
        - `child_id_expr` — Key to be checked. [`String`](/sql-reference/data-types/string)
        - `ancestor_id_expr` — Alleged ancestor of the `child_id_expr` key. [`const String`](/sql-reference/data-types/string)

        Returns `0` if `child_id_expr` is not a child of `ancestor_id_expr`, `1` if `child_id_expr` is a child of `ancestor_id_expr` or if `child_id_expr` is an `ancestor_id_expr`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("dictIsIn", *to_args(locals()))
    
    @staticmethod
    def displayName() -> Function:
        """
        displayName()

        
        Returns the value of `display_name` from config or server FQDN if not set. [`String`](/sql-reference/data-types/string)
        """
        return Function("displayName", *to_args(locals()))
    
    @staticmethod
    def distinctDynamicTypes(dynamic: Any) -> Function:
        """
        distinctDynamicTypes(dynamic)

        Args:
        - `dynamic` — Dynamic column. [`Dynamic`](/sql-reference/data-types/dynamic)

        Returns the sorted list of data type names. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("distinctDynamicTypes", *to_args(locals()))
    
    @staticmethod
    def distinctJSONPaths(json: Any) -> Function:
        """
        distinctJSONPaths(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns the sorted list of paths. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("distinctJSONPaths", *to_args(locals()))
    
    @staticmethod
    def distinctJSONPathsAndTypes(json: Any) -> Function:
        """
        distinctJSONPathsAndTypes(json)

        Args:
        - `json` — JSON column. [`JSON`](/sql-reference/data-types/newjson)

        Returns the sorted map of paths and types. [`Map(String, Array(String))`](/sql-reference/data-types/map)
        """
        return Function("distinctJSONPathsAndTypes", *to_args(locals()))
    
    @staticmethod
    def divide(x: Any, y: Any) -> Function:
        """
        divide(x, y)

        Args:
        - `x` — Dividend - `y` — Divisor 
        The quotient of x and y
        """
        return Function("divide", *to_args(locals()))
    
    @staticmethod
    def divideDecimal(x: Any, y: Any, result_scale: Any | None = None) -> Function:
        """
        divideDecimal(x, y[, result_scale])

        Args:
        - `x` — First value: [Decimal](/sql-reference/data-types/decimal). - `y` — Second value: [Decimal](/sql-reference/data-types/decimal). - `result_scale` — Scale of result. Type [Int/UInt](/sql-reference/data-types/int-uint). 
        The result of division with given scale. [`Decimal256`](/sql-reference/data-types/decimal)
        """
        return Function("divideDecimal", *to_args(locals()))
    
    @staticmethod
    def divideOrNull(x: Any, y: Any) -> Function:
        """
        divideOrNull(x, y)

        Args:
        - `x` — Dividend - `y` — Divisor 
        The quotient of x and y, or NULL.
        """
        return Function("divideOrNull", *to_args(locals()))
    
    @staticmethod
    def domain(url: Any) -> Function:
        """
        domain(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the host name if the input string can be parsed as a URL, otherwise an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("domain", *to_args(locals()))
    
    @staticmethod
    def domainRFC(url: Any) -> Function:
        """
        domainRFC(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the host name if the input string can be parsed as a URL, otherwise an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("domainRFC", *to_args(locals()))
    
    @staticmethod
    def domainWithoutWWW(url: Any) -> Function:
        """
        domainWithoutWWW(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the domain name if the input string can be parsed as a URL (without leading `www.`), otherwise an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("domainWithoutWWW", *to_args(locals()))
    
    @staticmethod
    def domainWithoutWWWRFC(url: Any) -> Function:
        """
        domainWithoutWWWRFC(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the domain name if the input string can be parsed as a URL (without leading `www.`), otherwise an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("domainWithoutWWWRFC", *to_args(locals()))
    
    @staticmethod
    def dotProduct(vector1: Any, vector2: Any) -> Function:
        """
        dotProduct(vector1, vector2)

        Args:
        - `vector1` — First vector. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T)`](/sql-reference/data-types/tuple)
        - `vector2` — Second vector. Must be the same size as the first vector. [`Array(T)`](/sql-reference/data-types/array) or [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns the dot product of the two vectors. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        """
        return Function("dotProduct", *to_args(locals()))
    
    @staticmethod
    def dumpColumnStructure(x: Any) -> Function:
        """
        dumpColumnStructure(x)

        Args:
        - `x` — Value for which to get the description of. [`Any`](/sql-reference/data-types)

        Returns a description of the column structure used for representing the value. [`String`](/sql-reference/data-types/string)
        """
        return Function("dumpColumnStructure", *to_args(locals()))
    
    @staticmethod
    def dynamicElement(dynamic: Any, type_name: Any) -> Function:
        """
        dynamicElement(dynamic, type_name)

        Args:
        - `dynamic` — Dynamic column to extract from. [`Dynamic`](/sql-reference/data-types/dynamic)
        - `type_name` — The name of the variant type to extract (e.g., 'String', 'Int64', 'Array(Int64)'). 
        Returns values of the specified type from the Dynamic column. Returns NULL for non-matching types (or empty array for array types). [`Any`](/sql-reference/data-types)
        """
        return Function("dynamicElement", *to_args(locals()))
    
    @staticmethod
    def dynamicType(dynamic: Any) -> Function:
        """
        dynamicType(dynamic)

        Args:
        - `dynamic` — Dynamic column to inspect. [`Dynamic`](/sql-reference/data-types/dynamic)

        Returns the type name of the value stored in each row, or 'None' for NULL values. [`String`](/sql-reference/data-types/string)
        """
        return Function("dynamicType", *to_args(locals()))
    
    @staticmethod
    def e() -> Function:
        """
        e()

        
        Returns Euler's constant [`Float64`](/sql-reference/data-types/float)
        """
        return Function("e", *to_args(locals()))
    
    @staticmethod
    def editDistance(s1: Any, s2: Any) -> Function:
        """
        editDistance(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the edit distance between the two strings. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("editDistance", *to_args(locals()))
    
    @staticmethod
    def editDistanceUTF8(s1: Any, s2: Any) -> Function:
        """
        editDistanceUTF8(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the edit distance between the two UTF8 strings. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("editDistanceUTF8", *to_args(locals()))
    
    @staticmethod
    def empty(arr: Any) -> Function:
        """
        empty(arr)

        Args:
        - `arr` — Input array. [`Array(T)`](/sql-reference/data-types/array)

        Returns `1` for an empty array or `0` for a non-empty array [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("empty", *to_args(locals()))
    
    @staticmethod
    def emptyArrayDate() -> Function:
        """
        emptyArrayDate()

        
        An empty Date array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayDate", *to_args(locals()))
    
    @staticmethod
    def emptyArrayDateTime() -> Function:
        """
        emptyArrayDateTime()

        
        An empty DateTime array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayDateTime", *to_args(locals()))
    
    @staticmethod
    def emptyArrayFloat32() -> Function:
        """
        emptyArrayFloat32()

        
        An empty Float32 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayFloat32", *to_args(locals()))
    
    @staticmethod
    def emptyArrayFloat64() -> Function:
        """
        emptyArrayFloat64()

        
        An empty Float64 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayFloat64", *to_args(locals()))
    
    @staticmethod
    def emptyArrayInt16() -> Function:
        """
        emptyArrayInt16()

        
        An empty Int16 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayInt16", *to_args(locals()))
    
    @staticmethod
    def emptyArrayInt32() -> Function:
        """
        emptyArrayInt32()

        
        An empty Int32 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayInt32", *to_args(locals()))
    
    @staticmethod
    def emptyArrayInt64() -> Function:
        """
        emptyArrayInt64()

        
        An empty Int64 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayInt64", *to_args(locals()))
    
    @staticmethod
    def emptyArrayInt8() -> Function:
        """
        emptyArrayInt8()

        
        An empty Int8 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayInt8", *to_args(locals()))
    
    @staticmethod
    def emptyArrayString() -> Function:
        """
        emptyArrayString()

        
        An empty String array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayString", *to_args(locals()))
    
    @staticmethod
    def emptyArrayToSingle(arr: Any) -> Function:
        """
        emptyArrayToSingle(arr)

        Args:
        - `arr` — An empty array. [`Array(T)`](/sql-reference/data-types/array)

        An array with a single value of the Array's default type. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayToSingle", *to_args(locals()))
    
    @staticmethod
    def emptyArrayUInt16() -> Function:
        """
        emptyArrayUInt16()

        
        An empty UInt16 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayUInt16", *to_args(locals()))
    
    @staticmethod
    def emptyArrayUInt32() -> Function:
        """
        emptyArrayUInt32()

        
        An empty UInt32 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayUInt32", *to_args(locals()))
    
    @staticmethod
    def emptyArrayUInt64() -> Function:
        """
        emptyArrayUInt64()

        
        An empty UInt64 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayUInt64", *to_args(locals()))
    
    @staticmethod
    def emptyArrayUInt8() -> Function:
        """
        emptyArrayUInt8()

        
        An empty UInt8 array. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("emptyArrayUInt8", *to_args(locals()))
    
    @staticmethod
    def enabledProfiles() -> Function:
        """
        enabledProfiles()

        
        Returns an array of setting profile names which are enabled for the current user. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("enabledProfiles", *to_args(locals()))
    
    @staticmethod
    def enabledRoles() -> Function:
        """
        enabledRoles()

        
        Returns an array of role names which are enabled for the current user. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("enabledRoles", *to_args(locals()))
    
    @staticmethod
    def encodeURLComponent(url: Any) -> Function:
        """
        encodeURLComponent(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the encoded URL. [`String`](/sql-reference/data-types/string)
        """
        return Function("encodeURLComponent", *to_args(locals()))
    
    @staticmethod
    def encodeURLFormComponent(url: Any) -> Function:
        """
        encodeURLFormComponent(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the encoded URL. [`String`](/sql-reference/data-types/string)
        """
        return Function("encodeURLFormComponent", *to_args(locals()))
    
    @staticmethod
    def encodeXMLComponent(s: Any) -> Function:
        """
        encodeXMLComponent(s)

        Args:
        - `s` — String to escape. [`String`](/sql-reference/data-types/string)

        Returns the escaped string. [`String`](/sql-reference/data-types/string)
        """
        return Function("encodeXMLComponent", *to_args(locals()))
    
    @staticmethod
    def encrypt(mode: Any, plaintext: Any, key: Any, iv: Any | None = None, aad: Any | None = None) -> Function:
        """
        encrypt(mode, plaintext, key[, iv, aad])

        Args:
        - `mode` — Encryption mode. [`String`](/sql-reference/data-types/string)
        - `plaintext` — Text that should be encrypted. [`String`](/sql-reference/data-types/string)
        - `key` — Encryption key. [`String`](/sql-reference/data-types/string)
        - `iv` — Initialization vector. Required for `-gcm` modes, optional for others. [`String`](/sql-reference/data-types/string)
        - `aad` — Additional authenticated data. It isn't encrypted, but it affects decryption. Works only in `-gcm` modes, for others it throws an exception. [`String`](/sql-reference/data-types/string)

        Returns binary string ciphertext. [`String`](/sql-reference/data-types/string)
        """
        return Function("encrypt", *to_args(locals()))
    
    @staticmethod
    def endsWith(s: Any, suffix: Any) -> Function:
        """
        endsWith(s, suffix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `suffix` — Suffix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` ends with `suffix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("endsWith", *to_args(locals()))
    
    @staticmethod
    def endsWithCaseInsensitive(s: Any, suffix: Any) -> Function:
        """
        endsWithCaseInsensitive(s, suffix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `suffix` — Case-insensitive suffix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` ends with case-insensitive `suffix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("endsWithCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def endsWithCaseInsensitiveUTF8(s: Any, suffix: Any) -> Function:
        """
        endsWithCaseInsensitiveUTF8(s, suffix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `suffix` — Case-insensitive suffix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` ends with case-insensitive `suffix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("endsWithCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def endsWithUTF8(s: Any, suffix: Any) -> Function:
        """
        endsWithUTF8(s, suffix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `suffix` — Suffix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` ends with `suffix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("endsWithUTF8", *to_args(locals()))
    
    @staticmethod
    def entropy(val: Any) -> Function:
        """
        entropy(val)

        Args:
        - `val` — Column of values of any type. [`Any`](/sql-reference/data-types)

        Returns Shannon entropy. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("entropy", *to_args(locals()))
    
    @staticmethod
    def equals(a: Any, b: Any) -> Function:
        """
        equals(a, b)
                -- a = b
                -- a == b

        Args:
        - `a` — First value.<sup>[*](#comparison-rules)</sup> - `b` — Second value.<sup>[*](#comparison-rules)</sup> 
        Returns `1` if `a` is equal to `b`, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("equals", *to_args(locals()))
    
    @staticmethod
    def erf(x: Any) -> Function:
        """
        erf(x)

        Args:
        - `x` — The value for which to compute the error function value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the error function value [`Float*`](/sql-reference/data-types/float)
        """
        return Function("erf", *to_args(locals()))
    
    @staticmethod
    def erfc(x: Any) -> Function:
        """
        erfc(x)

        Args:
        - `x` — The value for which to find the error function value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the complementary error function value [`Float*`](/sql-reference/data-types/float)
        """
        return Function("erfc", *to_args(locals()))
    
    @staticmethod
    def errorCodeToName(error_code: Any) -> Function:
        """
        errorCodeToName(error_code)

        Args:
        - `error_code` — ClickHouse error code. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the textual name of `error_code`. [`String`](/sql-reference/data-types/string)
        """
        return Function("errorCodeToName", *to_args(locals()))
    
    @staticmethod
    def estimateCompressionRatio(codec: Any | None = None, block_size_bytes: Any | None = None) -> Function:
        """
        estimateCompressionRatio([codec, block_size_bytes])(column)

        Args:
        - `column` — Column of any type. [`Any`](/sql-reference/data-types)

        Returns an estimate compression ratio for the given column. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("estimateCompressionRatio", *to_args(locals()))
    
    @staticmethod
    def evalMLMethod(model: Any, x1: Any, x2: Any | None = None) -> Function:
        """
        evalMLMethod(model, x1[, x2, ...])

        Args:
        - `model` — The trained machine learning model. [`AggregateFunctionState`](/sql-reference/data-types/aggregatefunction)
        - `x1, x2, ...` — Feature values for prediction. [`Float*`](/sql-reference/data-types/float) or [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the predicted value based on the trained model. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("evalMLMethod", *to_args(locals()))
    
    @staticmethod
    def exp(x: Any) -> Function:
        """
        exp(x)

        Args:
        - `x` — The exponent. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns `e^x` [`Float*`](/sql-reference/data-types/float)
        """
        return Function("exp", *to_args(locals()))
    
    @staticmethod
    def exp10(x: Any) -> Function:
        """
        exp10(x)

        Args:
        - `x` — The exponent. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns 10^x [`Float*`](/sql-reference/data-types/float)
        """
        return Function("exp10", *to_args(locals()))
    
    @staticmethod
    def exp2(x: Any) -> Function:
        """
        exp2(x)

        Args:
        - `x` — The exponent. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns 2^x [`Float*`](/sql-reference/data-types/float)
        """
        return Function("exp2", *to_args(locals()))
    
    @staticmethod
    def exponentialMovingAverage(x: Any) -> Function:
        """
        exponentialMovingAverage(x)(value, timeunit)

        Args:
        - `value` — Value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `timeunit` — Timeunit. Timeunit is not timestamp (seconds), it's an index of the time interval. Can be calculated using `intDiv`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns an exponentially smoothed moving average of the values for the past `x` time at the latest point of time. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("exponentialMovingAverage", *to_args(locals()))
    
    @staticmethod
    def exponentialTimeDecayedAvg(x: Any) -> Function:
        """
        exponentialTimeDecayedAvg(x)(v, t)

        Args:
        - `v` — Value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `t` — Time. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns an exponentially smoothed weighted moving average at index `t` in time. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("exponentialTimeDecayedAvg", *to_args(locals()))
    
    @staticmethod
    def exponentialTimeDecayedCount(x: Any) -> Function:
        """
        exponentialTimeDecayedCount(x)(t)

        Args:
        - `t` — Time. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the cumulative exponential decay at the given point in time. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("exponentialTimeDecayedCount", *to_args(locals()))
    
    @staticmethod
    def exponentialTimeDecayedMax(x: Any) -> Function:
        """
        exponentialTimeDecayedMax(x)(value, timeunit)

        Args:
        - `value` — Value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `timeunit` — Timeunit. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the maximum of the exponentially smoothed weighted moving average at `t` and `t-1`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("exponentialTimeDecayedMax", *to_args(locals()))
    
    @staticmethod
    def exponentialTimeDecayedSum(x: Any) -> Function:
        """
        exponentialTimeDecayedSum(x)(v, t)

        Args:
        - `v` — Value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `t` — Time. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the sum of exponentially smoothed moving average values at the given point in time. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("exponentialTimeDecayedSum", *to_args(locals()))
    
    @staticmethod
    def extract(haystack: Any, pattern: Any) -> Function:
        """
        extract(haystack, pattern)

        Args:
        - `haystack` — String from which to extract. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expression, typically containing a capturing group. [`const String`](/sql-reference/data-types/string)

        Returns extracted fragment as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("extract", *to_args(locals()))
    
    @staticmethod
    def extractAll(haystack: Any, pattern: Any) -> Function:
        """
        extractAll(haystack, pattern)

        Args:
        - `haystack` — String from which to extract fragments. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expression, optionally containing capturing groups. [`const String`](/sql-reference/data-types/string)

        Returns array of extracted fragments. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("extractAll", *to_args(locals()))
    
    @staticmethod
    def extractAllGroupsHorizontal(s: Any, regexp: Any) -> Function:
        """
        extractAllGroupsHorizontal(s, regexp)

        Args:
        - `s` — Input string to extract from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `regexp` — Regular expression to match by. [`const String`](/sql-reference/data-types/string) or [`const FixedString`](/sql-reference/data-types/fixedstring)

        Returns an array of arrays, where each inner array contains all captures from one capturing group across all matches. The first inner array contains all captures from group 1, the second from group 2, etc. If no matches are found, returns an empty array. [`Array(Array(String))`](/sql-reference/data-types/array)
        """
        return Function("extractAllGroupsHorizontal", *to_args(locals()))
    
    @staticmethod
    def extractAllGroupsVertical(s: Any, regexp: Any) -> Function:
        """
        extractAllGroupsVertical(s, regexp)

        Args:
        - `s` — Input string to extract from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `regexp` — Regular expression to match by. [`const String`](/sql-reference/data-types/string) or [`const FixedString`](/sql-reference/data-types/fixedstring)

        Returns an array of arrays, where each inner array contains the captured groups from one match. Each match produces an array with elements corresponding to the capturing groups in the regular expression (group 1, group 2, etc.). If no matches are found, returns an empty array. [`Array(Array(String))`](/sql-reference/data-types/array)
        """
        return Function("extractAllGroupsVertical", *to_args(locals()))
    
    @staticmethod
    def extractGroups(s: Any, regexp: Any) -> Function:
        """
        extractGroups(s, regexp)

        Args:
        - `s` — Input string to extract from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `regexp` — Regular expression. Constant. [`const String`](/sql-reference/data-types/string) or [`const FixedString`](/sql-reference/data-types/fixedstring)

        If the function finds at least one matching group, it returns Array(Array(String)) column, clustered by group_id (`1` to `N`, where `N` is number of capturing groups in regexp). If there is no matching group, it returns an empty array. [`Array(Array(String))`](/sql-reference/data-types/array)
        """
        return Function("extractGroups", *to_args(locals()))
    
    @staticmethod
    def extractKeyValuePairs(input: Any) -> Function:
        """
        extractKeyValuePairs(input)

        
        
        """
        return Function("extractKeyValuePairs", *to_args(locals()))
    
    @staticmethod
    def extractKeyValuePairsWithEscaping(input: Any) -> Function:
        """
        extractKeyValuePairsWithEscaping(input)

        
        
        """
        return Function("extractKeyValuePairsWithEscaping", *to_args(locals()))
    
    @staticmethod
    def extractTextFromHTML(html: Any) -> Function:
        """
        extractTextFromHTML(html)

        Args:
        - `html` — String containing HTML content to extract text from. [`String`](/sql-reference/data-types/string)

        Returns the extracted text content with normalized whitespace. [`String`](/sql-reference/data-types/string)
        """
        return Function("extractTextFromHTML", *to_args(locals()))
    
    @staticmethod
    def extractURLParameter(url: Any, name: Any) -> Function:
        """
        extractURLParameter(url, name)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)
        - `name` — Parameter name. [`String`](/sql-reference/data-types/string)

        Returns the value of the URL parameter with the specified name. [`String`](/sql-reference/data-types/string)
        """
        return Function("extractURLParameter", *to_args(locals()))
    
    @staticmethod
    def extractURLParameterNames(url: Any) -> Function:
        """
        extractURLParameterNames(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns an array of name strings corresponding to the names of URL parameters. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("extractURLParameterNames", *to_args(locals()))
    
    @staticmethod
    def extractURLParameters(url: Any) -> Function:
        """
        extractURLParameters(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns an array of `name=value` strings corresponding to the URL parameters. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("extractURLParameters", *to_args(locals()))
    
    @staticmethod
    def factorial(n: Any) -> Function:
        """
        factorial(n)

        Args:
        - `n` — Integer value for which to calculate the factorial. Maximum value is 20. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the factorial of the input as UInt64. Returns 1 for input 0 or any negative value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("factorial", *to_args(locals()))
    
    @staticmethod
    def farmFingerprint64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        farmFingerprint64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash value of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("farmFingerprint64", *to_args(locals()))
    
    @staticmethod
    def farmHash64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        farmHash64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash value of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("farmHash64", *to_args(locals()))
    
    @staticmethod
    def file(path: Any, default: Any | None = None) -> Function:
        """
        file(path[, default])

        Args:
        - `path` — The path of the file relative to the `user_files_path`. Supports wildcards `*`, `**`, `?`, `{abc,def}` and `{N..M}` where `N`, `M` are numbers and `'abc', 'def'` are strings. [`String`](/sql-reference/data-types/string)
        - `default` — The value returned if the file does not exist or cannot be accessed. [`String`](/sql-reference/data-types/string) or [`NULL`](/sql-reference/syntax#null)

        Returns the file content as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("file", *to_args(locals()))
    
    @staticmethod
    def filesystemAvailable(disk_name: Any | None = None) -> Function:
        """
        filesystemAvailable([disk_name])

        Args:
        - `disk_name` — Optional. The disk name to find the amount of free space for. If omitted, uses the default disk. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the amount of remaining space available in bytes. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("filesystemAvailable", *to_args(locals()))
    
    @staticmethod
    def filesystemCapacity(disk_name: Any | None = None) -> Function:
        """
        filesystemCapacity([disk_name])

        Args:
        - `disk_name` — Optional. The disk name to get the capacity for. If omitted, uses the default disk. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the capacity of the filesystem in bytes. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("filesystemCapacity", *to_args(locals()))
    
    @staticmethod
    def filesystemUnreserved(disk_name: Any | None = None) -> Function:
        """
        filesystemUnreserved([disk_name])

        Args:
        - `disk_name` — Optional. The disk name for which to find the total amount of free space. If omitted, uses the default disk. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the amount of free space in bytes. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("filesystemUnreserved", *to_args(locals()))
    
    @staticmethod
    def finalizeAggregation(state: Any) -> Function:
        """
        finalizeAggregation(state)

        Args:
        - `state` — State of aggregation. [`AggregateFunction`](/sql-reference/data-types/aggregatefunction)

        Returns the finalized result of aggregation. [`Any`](/sql-reference/data-types)
        """
        return Function("finalizeAggregation", *to_args(locals()))
    
    @staticmethod
    def financialInternalRateOfReturn(cashflows: Any, guess: Any | None = None) -> Function:
        """
        financialInternalRateOfReturn(cashflows[, guess])

        Args:
        - `cashflows` — Array of cash flows. Each value represents a payment (negative value) or income (positive value). [`Array(Int8/16/32/64)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `[, guess]` — Optional initial guess (constant value) for the internal rate of return (default 0.1). [`Float*`](/sql-reference/data-types/float)

        Returns the internal rate of return or `NaN` if the calculation cannot converge, input array is empty or has only one element, all cash flows are zero, or other calculation errors occur. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("financialInternalRateOfReturn", *to_args(locals()))
    
    @staticmethod
    def financialInternalRateOfReturnExtended(cashflow: Any, date: Any, guess: Any | None = None, daycount: Any | None = None) -> Function:
        """
        financialInternalRateOfReturnExtended(cashflow, date [, guess, daycount])

        Args:
        - `cashflow` — An array of cash flows corresponding to the dates in second param. [`Array(Int8/16/32/64)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `date` — A sorted array of unique dates corresponding to the cash flows. [`Array(Date)`](/sql-reference/data-types/array) or [`Array(Date32)`](/sql-reference/data-types/array)
        - `[, guess]` — Optional. Initial guess (constant value) for the XIRR calculation. [`Float*`](/sql-reference/data-types/float)
        - `[, daycount]` — 
        Optional day count convention (default 'ACT_365F'). Supported values:
        - 'ACT_365F' - Actual/365 Fixed: Uses actual number of days between dates divided by 365
        - 'ACT_365_25' - Actual/365.25: Uses actual number of days between dates divided by 365.25
                     [`String`](/sql-reference/data-types/string)

        Returns the XIRR value. If the calculation cannot be performed, it returns NaN. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("financialInternalRateOfReturnExtended", *to_args(locals()))
    
    @staticmethod
    def financialNetPresentValue(rate: Any, cashflows: Any, start_from_zero: Any | None = None) -> Function:
        """
        financialNetPresentValue(rate, cashflows[, start_from_zero])

        Args:
        - `rate` — The discount rate to apply. [`Float*`](/sql-reference/data-types/float)
        - `cashflows` — Array of cash flows. Each value represents a payment (negative value) or income (positive value). [`Array(Int8/16/32/64)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `[, start_from_zero]` — Optional boolean parameter indicating whether to start the NPV calculation from period `0` (true) or period `1` (false, Excel-compatible). Default: true. [`Bool`](/sql-reference/data-types/boolean)

        Returns the net present value as a Float64 value. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("financialNetPresentValue", *to_args(locals()))
    
    @staticmethod
    def financialNetPresentValueExtended(rate: Any, cashflows: Any, dates: Any, daycount: Any | None = None) -> Function:
        """
        financialNetPresentValueExtended(rate, cashflows, dates[, daycount])

        Args:
        - `rate` — The discount rate to apply. [`Float*`](/sql-reference/data-types/float)
        - `cashflows` — Array of cash flows. Each value represents a payment (negative value) or income (positive value). Must contain at least one positive and one negative value. [`Array(Int8/16/32/64)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `dates` — Array of dates corresponding to each cash flow. Must have the same size as cashflows array. [`Array(Date)`](/sql-reference/data-types/array) or [`Array(Date32)`](/sql-reference/data-types/array)
        - `[, daycount]` — Optional day count convention. Supported values: `'ACT_365F'` (default) — Actual/365 Fixed, `'ACT_365_25'` — Actual/365.25. [`String`](/sql-reference/data-types/string)

        Returns the net present value as a Float64 value. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("financialNetPresentValueExtended", *to_args(locals()))
    
    @staticmethod
    def firstLine(s: Any) -> Function:
        """
        firstLine(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns the first line of the input string or the whole string if there are no line separators. [`String`](/sql-reference/data-types/string)
        """
        return Function("firstLine", *to_args(locals()))
    
    @staticmethod
    def firstNonDefault(arg1: Any, arg2: Any | None = None) -> Function:
        """
        firstNonDefault(arg1[, arg2[ ...]])

        Args:
        - `arg1` — The first argument to check - `arg2` — The second argument to check - `...` — Additional arguments to check 
        Result type is the supertype of all arguments
        """
        return Function("firstNonDefault", *to_args(locals()))
    
    @staticmethod
    def firstSignificantSubdomain(url: Any) -> Function:
        """
        firstSignificantSubdomain(url)

        
        
        """
        return Function("firstSignificantSubdomain", *to_args(locals()))
    
    @staticmethod
    def firstSignificantSubdomainCustom(url: Any, tld_list_name: Any) -> Function:
        """
        firstSignificantSubdomainCustom(url, tld_list_name)

        Args:
        - `url` — The URL to extract the subdomain from. [`String`](/sql-reference/data-types/string)
        - `tld_list_name` — Name of the custom TLD list from the configuration. [`String`](/sql-reference/data-types/string)

        Returns the first significant subdomain. [`String`](/sql-reference/data-types/string)
        """
        return Function("firstSignificantSubdomainCustom", *to_args(locals()))
    
    @staticmethod
    def firstSignificantSubdomainCustomRFC(url: Any, tld_list_name: Any) -> Function:
        """
        firstSignificantSubdomainCustomRFC(url, tld_list_name)

        Args:
        - `url` — The URL to extract the subdomain from. [`String`](/sql-reference/data-types/string)
        - `tld_list_name` — Name of the custom TLD list from the configuration. [`String`](/sql-reference/data-types/string)

        Returns the first significant subdomain. [`String`](/sql-reference/data-types/string)
        """
        return Function("firstSignificantSubdomainCustomRFC", *to_args(locals()))
    
    @staticmethod
    def firstSignificantSubdomainRFC(url: Any) -> Function:
        """
        firstSignificantSubdomainRFC(url)

        
        
        """
        return Function("firstSignificantSubdomainRFC", *to_args(locals()))
    
    @staticmethod
    def flameGraph(traces: Any, size: Any | None = None, ptr: Any | None = None) -> Function:
        """
        flameGraph(traces[, size[, ptr]])

        Args:
        - `traces` — A stacktrace. [`Array(UInt64)`](/sql-reference/data-types/array)
        - `size` — Optional. An allocation size for memory profiling (default 1). [`UInt64`](/sql-reference/data-types/int-uint)
        - `ptr` — Optional. An allocation address (default 0). [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of strings for use with flamegraph.pl utility. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("flameGraph", *to_args(locals()))
    
    @staticmethod
    def flattenTuple(input: Any) -> Function:
        """
        flattenTuple(input)

        Args:
        - `input` — Named and nested tuple to flatten. [`Tuple(n1 T1[, n2 T2, ... ])`](/sql-reference/data-types/tuple)

        Returns an output tuple whose elements are paths from the original input. [`Tuple(T)`](/sql-reference/data-types/tuple)
        """
        return Function("flattenTuple", *to_args(locals()))
    
    @staticmethod
    def flipCoordinates(geometry: Any) -> Function:
        """
        flipCoordinates(geometry)

        Args:
        - `geometry` — The geometry to transform. Supported types: Point (Tuple(Float64, Float64)), Ring (Array(Point)), Polygon (Array(Ring)), MultiPolygon (Array(Polygon)), LineString (Array(Point)), MultiLineString (Array(LineString)), or Geometry (a variant containing any of these types). 
        The geometry with flipped coordinates. The return type matches the input type. [`Point`](/sql-reference/data-types/geo#point) or [`Ring`](/sql-reference/data-types/geo#ring) or [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon) or [`LineString`](/sql-reference/data-types/geo#linestring) or [`MultiLineString`](/sql-reference/data-types/geo#multilinestring) or [`Geometry`](/sql-reference/data-types/geo)
        """
        return Function("flipCoordinates", *to_args(locals()))
    
    @staticmethod
    def floor(x: Any, N: Any | None = None) -> Function:
        """
        floor(x[, N])

        Args:
        - `x` — The value to round. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `N` — Optional. The number of decimal places to round to. Defaults to zero, which means rounding to an integer. Can be negative. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a rounded number of the same type as `x`. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("floor", *to_args(locals()))
    
    @staticmethod
    def format(pattern: Any, s0: Any, s1: Any | None = None) -> Function:
        """
        format(pattern, s0[, s1, ...])

        Args:
        - `pattern` — The format string containing placeholders. [`String`](/sql-reference/data-types/string)
        - `s0[, s1, ...]` — One or more values to substitute into the pattern. [`Any`](/sql-reference/data-types)

        Returns a formatted string. [`String`](/sql-reference/data-types/string)
        """
        return Function("format", *to_args(locals()))
    
    @staticmethod
    def formatDateTime(datetime: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        formatDateTime(datetime, format[, timezone])

        Args:
        - `datetime` — A date or date time to format. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `format` — Format string with replacement fields. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone name for the formatted time. [`String`](/sql-reference/data-types/string)

        Returns time and date values according to the determined format. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatDateTime", *to_args(locals()))
    
    @staticmethod
    def formatDateTimeInJodaSyntax(datetime: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        formatDateTimeInJodaSyntax(datetime, format[, timezone])

        Args:
        - `datetime` — A date or date time to format. [`DateTime`](/sql-reference/data-types/datetime) or [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `format` — Format string with Joda-style replacement fields. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone name for the formatted time. [`String`](/sql-reference/data-types/string)

        Returns time and date values according to the determined format. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatDateTimeInJodaSyntax", *to_args(locals()))
    
    @staticmethod
    def formatQuery(query: Any) -> Function:
        """
        formatQuery(query)

        Args:
        - `query` — The SQL query to be formatted. [String](../../sql-reference/data-types/string.md) 
        The formatted query [`String`](/sql-reference/data-types/string)
        """
        return Function("formatQuery", *to_args(locals()))
    
    @staticmethod
    def formatQueryOrNull(query: Any) -> Function:
        """
        formatQueryOrNull(query)

        Args:
        - `query` — The SQL query to be formatted. [String](../../sql-reference/data-types/string.md) 
        The formatted query [`String`](/sql-reference/data-types/string)
        """
        return Function("formatQueryOrNull", *to_args(locals()))
    
    @staticmethod
    def formatQuerySingleLine(query: Any) -> Function:
        """
        formatQuerySingleLine(query)

        Args:
        - `query` — The SQL query to be formatted. [String](../../sql-reference/data-types/string.md) 
        The formatted query [`String`](/sql-reference/data-types/string)
        """
        return Function("formatQuerySingleLine", *to_args(locals()))
    
    @staticmethod
    def formatQuerySingleLineOrNull(query: Any) -> Function:
        """
        formatQuerySingleLineOrNull(query)

        Args:
        - `query` — The SQL query to be formatted. [`String`](/sql-reference/data-types/string)

        The formatted query [`String`](/sql-reference/data-types/string)
        """
        return Function("formatQuerySingleLineOrNull", *to_args(locals()))
    
    @staticmethod
    def formatReadableDecimalSize(x: Any) -> Function:
        """
        formatReadableDecimalSize(x)

        Args:
        - `x` — Size in bytes. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a readable, rounded size with suffix as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatReadableDecimalSize", *to_args(locals()))
    
    @staticmethod
    def formatReadableQuantity(x: Any) -> Function:
        """
        formatReadableQuantity(x)

        Args:
        - `x` — A number to format. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a rounded number with suffix as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatReadableQuantity", *to_args(locals()))
    
    @staticmethod
    def formatReadableSize(x: Any) -> Function:
        """
        formatReadableSize(x)

        Args:
        - `x` — Size in bytes. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a readable, rounded size with suffix as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatReadableSize", *to_args(locals()))
    
    @staticmethod
    def formatReadableTimeDelta(column: Any, maximum_unit: Any | None = None, minimum_unit: Any | None = None) -> Function:
        """
        formatReadableTimeDelta(column[, maximum_unit, minimum_unit])

        Args:
        - `column` — A column with a numeric time delta. [`Float64`](/sql-reference/data-types/float)
        - `maximum_unit` — Optional. Maximum unit to show. Acceptable values: `nanoseconds`, `microseconds`, `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `months`, `years`. Default value: `years`. [`const String`](/sql-reference/data-types/string)
        - `minimum_unit` — Optional. Minimum unit to show. All smaller units are truncated. Acceptable values: `nanoseconds`, `microseconds`, `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `months`, `years`. If explicitly specified value is bigger than `maximum_unit`, an exception will be thrown. Default value: `seconds` if `maximum_unit` is `seconds` or bigger, `nanoseconds` otherwise. [`const String`](/sql-reference/data-types/string)

        Returns a time delta as a string. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatReadableTimeDelta", *to_args(locals()))
    
    @staticmethod
    def formatRow(format: Any, x: Any, y: Any) -> Function:
        """
        formatRow(format, x, y, ...)

        Args:
        - `format` — Text format. For example, CSV, TSV. [`String`](/sql-reference/data-types/string)
        - `x, y, ...` — Expressions. [`Any`](/sql-reference/data-types)

        A formatted string. (for text formats it's usually terminated with the new line character). [`String`](/sql-reference/data-types/string)
        """
        return Function("formatRow", *to_args(locals()))
    
    @staticmethod
    def formatRowNoNewline(format: Any, x: Any, y: Any) -> Function:
        """
        formatRowNoNewline(format, x, y, ...)

        Args:
        - `format` — Text format. For example, CSV, TSV. [`String`](/sql-reference/data-types/string)
        - `x, y, ...` — Expressions. [`Any`](/sql-reference/data-types)

        Returns a formatted string with newlines removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("formatRowNoNewline", *to_args(locals()))
    
    @staticmethod
    def fragment(url: Any) -> Function:
        """
        fragment(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the fragment identifier without the initial hash symbol. [`String`](/sql-reference/data-types/string)
        """
        return Function("fragment", *to_args(locals()))
    
    @staticmethod
    def fromDaysSinceYearZero(days: Any) -> Function:
        """
        fromDaysSinceYearZero(days)

        Args:
        - `days` — The number of days passed since year zero. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns the date corresponding to the number of days passed since year zero. [`Date`](/sql-reference/data-types/date)
        """
        return Function("fromDaysSinceYearZero", *to_args(locals()))
    
    @staticmethod
    def fromDaysSinceYearZero32(days: Any) -> Function:
        """
        fromDaysSinceYearZero32(days)

        Args:
        - `days` — The number of days passed since year zero. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns the date corresponding to the number of days passed since year zero. [`Date32`](/sql-reference/data-types/date32)
        """
        return Function("fromDaysSinceYearZero32", *to_args(locals()))
    
    @staticmethod
    def fromModifiedJulianDay(day: Any) -> Function:
        """
        fromModifiedJulianDay(day)

        Args:
        - `day` — Modified Julian Day number. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns date in text form. [`String`](/sql-reference/data-types/string)
        """
        return Function("fromModifiedJulianDay", *to_args(locals()))
    
    @staticmethod
    def fromModifiedJulianDayOrNull(day: Any) -> Function:
        """
        fromModifiedJulianDayOrNull(day)

        Args:
        - `day` — Modified Julian Day number. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns date in text form for valid `day` argument, otherwise `null`. [`Nullable(String)`](/sql-reference/data-types/nullable)
        """
        return Function("fromModifiedJulianDayOrNull", *to_args(locals()))
    
    @staticmethod
    def fromUTCTimestamp(datetime: Any, time_zone: Any) -> Function:
        """
        fromUTCTimestamp(datetime, time_zone)

        Args:
        - `datetime` — A date or date with time const value or an expression. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `time_zone` — A String type const value or an expression representing the time zone. [`String`](/sql-reference/data-types/string)

        Returns DateTime/DateTime64 in the specified timezone. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("fromUTCTimestamp", *to_args(locals()))
    
    @staticmethod
    def fromUnixTimestamp(timestamp: Any) -> Function:
        """
        fromUnixTimestamp(timestamp)
        fromUnixTimestamp(timestamp[, format[, timezone]])

        Args:
        - `timestamp` — Unix timestamp or date/date with time value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `format` — Optional. Constant format string for output formatting. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Constant time zone string. [`String`](/sql-reference/data-types/string)

        Returns `DateTime` of the timestamp when called with one argument, or a String  when called with two or three arguments. [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string)
        """
        return Function("fromUnixTimestamp", *to_args(locals()))
    
    @staticmethod
    def fromUnixTimestamp64Micro(value: Any, timezone: Any | None = None) -> Function:
        """
        fromUnixTimestamp64Micro(value[, timezone])

        Args:
        - `value` — Unix timestamp in microseconds. [`Int64`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone for the returned value. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime64` value with microsecond precision. [`DateTime64(6)`](/sql-reference/data-types/datetime64)
        """
        return Function("fromUnixTimestamp64Micro", *to_args(locals()))
    
    @staticmethod
    def fromUnixTimestamp64Milli(value: Any, timezone: Any | None = None) -> Function:
        """
        fromUnixTimestamp64Milli(value[, timezone])

        Args:
        - `value` — Unix timestamp in milliseconds. [`Int64`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone for the returned value. [`String`](/sql-reference/data-types/string)

        A `DateTime64` value with millisecond precision. [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("fromUnixTimestamp64Milli", *to_args(locals()))
    
    @staticmethod
    def fromUnixTimestamp64Nano(value: Any, timezone: Any | None = None) -> Function:
        """
        fromUnixTimestamp64Nano(value[, timezone])

        Args:
        - `value` — Unix timestamp in nanoseconds. [`Int64`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone for the returned value. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime64` value with nanosecond precision. [`DateTime64(9)`](/sql-reference/data-types/datetime64)
        """
        return Function("fromUnixTimestamp64Nano", *to_args(locals()))
    
    @staticmethod
    def fromUnixTimestamp64Second(value: Any, timezone: Any | None = None) -> Function:
        """
        fromUnixTimestamp64Second(value[, timezone])

        Args:
        - `value` — Unix timestamp in seconds. [`Int64`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone for the returned value. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime64` value with second precision. [`DateTime64(0)`](/sql-reference/data-types/datetime64)
        """
        return Function("fromUnixTimestamp64Second", *to_args(locals()))
    
    @staticmethod
    def fromUnixTimestampInJodaSyntax(timestamp: Any) -> Function:
        """
        fromUnixTimestampInJodaSyntax(timestamp)
        fromUnixTimestampInJodaSyntax(timestamp, format[, timezone])

        Args:
        - `timestamp` — Unix timestamp or date/time value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `format` — Optional. Constant format string using Joda syntax for output formatting. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Constant time zone string. [`String`](/sql-reference/data-types/string)

        Returns a date with time when called with one argument, or a String when called with two or three arguments.} [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string)
        """
        return Function("fromUnixTimestampInJodaSyntax", *to_args(locals()))
    
    @staticmethod
    def fuzzBits(s: Any, p: Any) -> Function:
        """
        fuzzBits(s, p)

        Args:
        - `s` — String or FixedString to perform bit fuzzing on [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `p` — Probability of flipping each bit as a number between `0.0` and `1.0` [`Float*`](/sql-reference/data-types/float)

        Returns a Fuzzed string with same type as `s`. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        """
        return Function("fuzzBits", *to_args(locals()))
    
    @staticmethod
    def fuzzQuery(query: Any) -> Function:
        """
        fuzzQuery(query)

        Args:
        - `query` — The SQL query to be fuzzed. [String](../../sql-reference/data-types/string.md) 
        The fuzzed query string [`String`](/sql-reference/data-types/string)
        """
        return Function("fuzzQuery", *to_args(locals()))
    
    @staticmethod
    def gccMurmurHash(arg1: Any, arg2: Any | None = None) -> Function:
        """
        gccMurmurHash(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the calculated hash value of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("gccMurmurHash", *to_args(locals()))
    
    @staticmethod
    def gcd(x: Any, y: Any) -> Function:
        """
        gcd(x, y)

        Args:
        - `x` — First integer - `y` — Second integer 
        The greatest common divisor of `x` and `y`.
        """
        return Function("gcd", *to_args(locals()))
    
    @staticmethod
    def generateRandomStructure(number_of_columns: Any | None = None, seed: Any | None = None) -> Function:
        """
        generateRandomStructure([number_of_columns, seed])

        Args:
        - `number_of_columns` — The desired number of columns in the resultant table structure. If set to 0 or `Null`, the number of columns will be random from 1 to 128. Default value: `Null`. [`UInt64`](/sql-reference/data-types/int-uint)
        - `seed` — Random seed to produce stable results. If seed is not specified or set to `Null`, it is randomly generated. [`UInt64`](/sql-reference/data-types/int-uint)

        Randomly generated table structure. [`String`](/sql-reference/data-types/string)
        """
        return Function("generateRandomStructure", *to_args(locals()))
    
    @staticmethod
    def generateSerialID(series_identifier: Any, start_value: Any | None = None) -> Function:
        """
        generateSerialID(series_identifier[, start_value])

        Args:
        - `series_identifier` — Series identifier [`const String`](/sql-reference/data-types/string)
        - `start_value` — Optional. Starting value for the counter. Defaults to 0. Note: this value is only used when creating a new series and is ignored if the series already exists [`UInt*`](/sql-reference/data-types/int-uint)

        Returns sequential numbers starting from the previous counter value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("generateSerialID", *to_args(locals()))
    
    @staticmethod
    def generateSnowflakeID(expr: Any | None = None, machine_id: Any | None = None) -> Function:
        """
        generateSnowflakeID([expr, [machine_id]])

        Args:
        - `expr` — An arbitrary [expression](/sql-reference/syntax#expressions) used to bypass [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) if the function is called multiple times in a query. The value of the expression has no effect on the returned Snowflake ID. Optional. - `machine_id` — A machine ID, the lowest 10 bits are used. [Int64](../data-types/int-uint.md). Optional. 
        Returns the Snowflake ID. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("generateSnowflakeID", *to_args(locals()))
    
    @staticmethod
    def generateULID(x: Any | None = None) -> Function:
        """
        generateULID([x])

        Args:
        - `x` — Optional. An expression resulting in any of the supported data types. The resulting value is discarded, but the expression itself if used for bypassing [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) if the function is called multiple times in one query. [`Any`](/sql-reference/data-types)

        Returns a ULID. [`FixedString(26)`](/sql-reference/data-types/fixedstring)
        """
        return Function("generateULID", *to_args(locals()))
    
    @staticmethod
    def generateUUIDv4(expr: Any | None = None) -> Function:
        """
        generateUUIDv4([expr])

        Args:
        - `expr` — Optional. An arbitrary expression used to bypass [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) if the function is called multiple times in a query. The value of the expression has no effect on the returned UUID. 
        Returns a UUIDv4. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("generateUUIDv4", *to_args(locals()))
    
    @staticmethod
    def generateUUIDv7(expr: Any | None = None) -> Function:
        """
        generateUUIDv7([expr])

        Args:
        - `expr` — Optional. An arbitrary expression used to bypass [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) if the function is called multiple times in a query. The value of the expression has no effect on the returned UUID. [`Any`](/sql-reference/data-types)

        Returns a UUIDv7. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("generateUUIDv7", *to_args(locals()))
    
    @staticmethod
    def geoDistance(lon1Deg: Any, lat1Deg: Any, lon2Deg: Any, lat2Deg: Any) -> Function:
        """
        geoDistance(lon1Deg, lat1Deg, lon2Deg, lat2Deg)

        Args:
        - `lon1Deg` — Longitude of the first point in degrees. Range: `[-180°, 180°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lat1Deg` — Latitude of the first point in degrees. Range: `[-90°, 90°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lon2Deg` — Longitude of the second point in degrees. Range: `[-180°, 180°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lat2Deg` — Latitude of the second point in degrees. Range: `[-90°, 90°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the distance between two points on the Earth's surface, in meters [`Float64`](/sql-reference/data-types/float)
        """
        return Function("geoDistance", *to_args(locals()))
    
    @staticmethod
    def geoToH3(lat: Any, lon: Any, resolution: Any) -> Function:
        """
        geoToH3(lat, lon, resolution)

        Args:
        - `lat` — Latitude in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon` — Longitude in degrees. [`Float64`](/sql-reference/data-types/float)
        - `resolution` — Index resolution with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the H3 index number, or `0` in case of error. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("geoToH3", *to_args(locals()))
    
    @staticmethod
    def geoToS2(lon: Any, lat: Any) -> Function:
        """
        geoToS2(lon, lat)

        Args:
        - `lon` — Longitude. [`Float64`](/sql-reference/data-types/float)
        - `lat` — Latitude. [`Float64`](/sql-reference/data-types/float)

        Returns the S2 cell identifier. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("geoToS2", *to_args(locals()))
    
    @staticmethod
    def geohashDecode(hash_str: Any) -> Function:
        """
        geohashDecode(hash_str)

        Args:
        - `hash_str` — Geohash-encoded string to decode. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns a tuple of `(longitude, latitude)` with `Float64` precision. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("geohashDecode", *to_args(locals()))
    
    @staticmethod
    def geohashEncode(longitude: Any, latitude: Any, precision: Any | None = None) -> Function:
        """
        geohashEncode(longitude, latitude, [precision])

        Args:
        - `longitude` — Longitude part of the coordinate to encode. Range: `[-180°, 180°]`. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `latitude` — Latitude part of the coordinate to encode. Range: `[-90°, 90°]`. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `precision` — Optional. Length of the resulting encoded string. Default: 12. Range: `[1, 12]`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an alphanumeric string of the encoded coordinate (modified version of the base32-encoding alphabet is used) [`String`](/sql-reference/data-types/string)
        """
        return Function("geohashEncode", *to_args(locals()))
    
    @staticmethod
    def geohashesInBox(longitude_min: Any, latitude_min: Any, longitude_max: Any, latitude_max: Any, precision: Any) -> Function:
        """
        geohashesInBox(longitude_min, latitude_min, longitude_max, latitude_max, precision)

        Args:
        - `longitude_min` — Minimum longitude. Range: `[-180°, 180°]`. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `latitude_min` — Minimum latitude. Range: `[-90°, 90°]`. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `longitude_max` — Maximum longitude. Range: `[-180°, 180°]`. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `latitude_max` — Maximum latitude. Range: `[-90°, 90°]`. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `precision` — Geohash precision. Range: `[1, 12]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns an array of precision-long strings of geohash-boxes covering the provided area, or an empty array if the minimum longitude and latitude values aren't less than the corresponding maximum values. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("geohashesInBox", *to_args(locals()))
    
    @staticmethod
    def getClientHTTPHeader(name: Any) -> Function:
        """
        getClientHTTPHeader(name)

        Args:
        - `name` — The HTTP header name. [`String`](/sql-reference/data-types/string)

        Returns the value of the header. [`String`](/sql-reference/data-types/string)
        """
        return Function("getClientHTTPHeader", *to_args(locals()))
    
    @staticmethod
    def getMacro(name: Any) -> Function:
        """
        getMacro(name)

        Args:
        - `name` — The name of the macro to retrieve. [`const String`](/sql-reference/data-types/string)

        Returns the value of the specified macro. [`String`](/sql-reference/data-types/string)
        """
        return Function("getMacro", *to_args(locals()))
    
    @staticmethod
    def getMaxTableNameLengthForDatabase(database_name: Any) -> Function:
        """
        getMaxTableNameLengthForDatabase(database_name)

        Args:
        - `database_name` — The name of the specified database. [`String`](/sql-reference/data-types/string)

        Returns the length of the maximum table name, an Integer
        """
        return Function("getMaxTableNameLengthForDatabase", *to_args(locals()))
    
    @staticmethod
    def getMergeTreeSetting(setting_name: Any) -> Function:
        """
        getMergeTreeSetting(setting_name)

        Args:
        - `setting_name` — The setting name. [`String`](/sql-reference/data-types/string)

        Returns the merge tree setting's current value.
        """
        return Function("getMergeTreeSetting", *to_args(locals()))
    
    @staticmethod
    def getOSKernelVersion() -> Function:
        """
        getOSKernelVersion()

        
        Returns the current OS kernel version. [`String`](/sql-reference/data-types/string)
        """
        return Function("getOSKernelVersion", *to_args(locals()))
    
    @staticmethod
    def getServerPort(port_name: Any) -> Function:
        """
        getServerPort(port_name)

        Args:
        - `port_name` — The name of the port. [`String`](/sql-reference/data-types/string)

        Returns the server port number. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("getServerPort", *to_args(locals()))
    
    @staticmethod
    def getServerSetting(setting_name: Any) -> Function:
        """
        getServerSetting(setting_name')

        Args:
        - `setting_name` — The server setting name. [`String`](/sql-reference/data-types/string)

        Returns the server setting's current value. [`Any`](/sql-reference/data-types)
        """
        return Function("getServerSetting", *to_args(locals()))
    
    @staticmethod
    def getSetting(setting_name: Any) -> Function:
        """
        getSetting(setting_name)

        Args:
        - `setting_Name` — The setting name. [`const String`](/sql-reference/data-types/string)

        Returns the setting's current value. [`Any`](/sql-reference/data-types)
        """
        return Function("getSetting", *to_args(locals()))
    
    @staticmethod
    def getSettingOrDefault(setting_name: Any, default_value: Any) -> Function:
        """
        getSettingOrDefault(setting_name, default_value)

        Args:
        - `setting_name` — The setting name. [`String`](/sql-reference/data-types/string)
        - `default_value` — Value to return if custom_setting is not set. Value may be of any data type or Null. 
        Returns the current value of the specified setting or `default_value` if the setting is not set.
        """
        return Function("getSettingOrDefault", *to_args(locals()))
    
    @staticmethod
    def getSizeOfEnumType(x: Any) -> Function:
        """
        getSizeOfEnumType(x)

        Args:
        - `x` — Value of type `Enum`. [`Enum`](/sql-reference/data-types/enum)

        Returns the number of fields with `Enum` input values. [`UInt8/16`](/sql-reference/data-types/int-uint)
        """
        return Function("getSizeOfEnumType", *to_args(locals()))
    
    @staticmethod
    def getSubcolumn(nested_value: Any, subcolumn_name: Any) -> Function:
        """
        getSubcolumn(nested_value, subcolumn_name)

        
        
        """
        return Function("getSubcolumn", *to_args(locals()))
    
    @staticmethod
    def getTypeSerializationStreams(col: Any) -> Function:
        """
        getTypeSerializationStreams(col)

        Args:
        - `col` — Column or string representation of a data-type from which the data type will be detected. [`Any`](/sql-reference/data-types)

        Returns an array with all the serialization sub-stream paths. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("getTypeSerializationStreams", *to_args(locals()))
    
    @staticmethod
    def globalIn(x: Any, set: Any) -> Function:
        """
        globalIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalIn", *to_args(locals()))
    
    @staticmethod
    def globalInIgnoreSet(x: Any, set: Any) -> Function:
        """
        globalIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def globalNotIn(x: Any, set: Any) -> Function:
        """
        globalNotIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalNotIn", *to_args(locals()))
    
    @staticmethod
    def globalNotInIgnoreSet(x: Any, set: Any) -> Function:
        """
        globalNotIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalNotInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def globalNotNullIn(x: Any, set: Any) -> Function:
        """
        globalNotNullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalNotNullIn", *to_args(locals()))
    
    @staticmethod
    def globalNotNullInIgnoreSet(x: Any, set: Any) -> Function:
        """
        globalNotNullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalNotNullInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def globalNullIn(x: Any, set: Any) -> Function:
        """
        globalNullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalNullIn", *to_args(locals()))
    
    @staticmethod
    def globalNullInIgnoreSet(x: Any, set: Any) -> Function:
        """
        globalNullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("globalNullInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def globalVariable(name: Any) -> Function:
        """
        globalVariable(name)

        Args:
        - `name` — Global variable name. [`String`](/sql-reference/data-types/string)

        Returns the value of variable `name`. [`Any`](/sql-reference/data-types)
        """
        return Function("globalVariable", *to_args(locals()))
    
    @staticmethod
    def greatCircleAngle(lon1Deg: Any, lat1Deg: Any, lon2Deg: Any, lat2Deg: Any) -> Function:
        """
        greatCircleAngle(lon1Deg, lat1Deg, lon2Deg, lat2Deg)

        Args:
        - `lon1Deg` — Longitude of the first point in degrees. Range: `[-180°, 180°]` [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lat1Deg` — Latitude of the first point in degrees. Range: `[-90°, 90°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lon2Deg` — Longitude of the second point in degrees. Range: `[-180°, 180°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lat2Deg` — Latitude of the second point in degrees. Range: `[-90°, 90°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the central angle between the two points in degrees [`Float64`](/sql-reference/data-types/float)
        """
        return Function("greatCircleAngle", *to_args(locals()))
    
    @staticmethod
    def greatCircleDistance(lon1Deg: Any, lat1Deg: Any, lon2Deg: Any, lat2Deg: Any) -> Function:
        """
        greatCircleDistance(lon1Deg, lat1Deg, lon2Deg, lat2Deg)

        Args:
        - `lon1Deg` — Longitude of the first point in degrees. Range: `[-180°, 180°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lat1Deg` — Latitude of the first point in degrees. Range: `[-90°, 90°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lon2Deg` — Longitude of the second point in degrees. Range: `[-180°, 180°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `lat2Deg` — Latitude of the second point in degrees. Range: `[-90°, 90°]`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the distance between two points on the Earth's surface, in meters [`Float64`](/sql-reference/data-types/float)
        """
        return Function("greatCircleDistance", *to_args(locals()))
    
    @staticmethod
    def greater(a: Any, b: Any) -> Function:
        """
        greater(a, b)
            -- a > b

        Args:
        - `a` — First value.<sup>[*](#comparison-rules)</sup> - `b` — Second value.<sup>[*](#comparison-rules)</sup> 
        Returns `1` if `a` is greater than `b`, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("greater", *to_args(locals()))
    
    @staticmethod
    def greaterOrEquals(a: Any, b: Any) -> Function:
        """
        greaterOrEquals(a, b)
            -- a >= b

        Args:
        - `a` — First value.<sup>[*](#comparison-rules)</sup> - `b` — Second value.<sup>[*](#comparison-rules)</sup> 
        Returns `1` if `a` is greater than or equal to `b`, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("greaterOrEquals", *to_args(locals()))
    
    @staticmethod
    def greatest(x1: Any, x2: Any | None = None) -> Function:
        """
        greatest(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — One or multiple values to compare. All arguments must be of comparable types. [`Any`](/sql-reference/data-types)

        Returns the greatest value among the arguments, promoted to the largest compatible type. [`Any`](/sql-reference/data-types)
        """
        return Function("greatest", *to_args(locals()))
    
    @staticmethod
    def groupArray(x: Any) -> Function:
        """
        groupArray(x)
        groupArray(max_size)(x)

        Args:
        - `x` — Argument values to collect into an array. [`Any`](/sql-reference/data-types)

        Returns an array of argument values. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupArray", *to_args(locals()))
    
    @staticmethod
    def groupArrayInsertAt(default_x: Any, size: Any) -> Function:
        """
        groupArrayInsertAt(default_x, size)([x, pos])

        Args:
        - `x` — Value to be inserted. [`Any`](/sql-reference/data-types)
        - `pos` — Position at which the specified element `x` is to be inserted. Index numbering in the array starts from zero. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns an array with inserted values. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupArrayInsertAt", *to_args(locals()))
    
    @staticmethod
    def groupArrayIntersect(x: Any) -> Function:
        """
        groupArrayIntersect(x)

        Args:
        - `x` — Argument (column name or expression). [`Any`](/sql-reference/data-types)

        Returns an array that contains elements that are in all arrays. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupArrayIntersect", *to_args(locals()))
    
    @staticmethod
    def groupArrayLast(max_size: Any) -> Function:
        """
        groupArrayLast(max_size)(x)

        Args:
        - `max_size` — Maximum size of the resulting array. [`UInt64`](/sql-reference/data-types/int-uint)
        - `x` — Argument (column name or expression). [`Any`](/sql-reference/data-types)

        Returns an array of the last argument values. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("groupArrayLast", *to_args(locals()))
    
    @staticmethod
    def groupArrayMovingAvg(numbers_for_summing: Any) -> Function:
        """
        groupArrayMovingAvg(numbers_for_summing)
        groupArrayMovingAvg(window_size)(numbers_for_summing)

        Args:
        - `numbers_for_summing` — Expression resulting in a numeric data type value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns an array of the same size and type as the input data. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupArrayMovingAvg", *to_args(locals()))
    
    @staticmethod
    def groupArrayMovingSum(numbers_for_summing: Any) -> Function:
        """
        groupArrayMovingSum(numbers_for_summing)
        groupArrayMovingSum(window_size)(numbers_for_summing)

        Args:
        - `numbers_for_summing` — Expression resulting in a numeric data type value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns an array of the same size and type as the input data. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupArrayMovingSum", *to_args(locals()))
    
    @staticmethod
    def groupArraySample(max_size: Any, seed: Any | None = None) -> Function:
        """
        groupArraySample(max_size[, seed])(x)

        Args:
        - `array_column` — Column containing arrays to be aggregated. [`Array`](/sql-reference/data-types/array)

        Array of randomly selected x arguments. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("groupArraySample", *to_args(locals()))
    
    @staticmethod
    def groupArraySorted(N: Any) -> Function:
        """
        groupArraySorted(N)(column)

        Args:
        - `column` — Column for which to group into an array. [`Any`](/sql-reference/data-types)

        Returns an array with the first N items in ascending order. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupArraySorted", *to_args(locals()))
    
    @staticmethod
    def groupBitAnd(expr: Any) -> Function:
        """
        groupBitAnd(expr)

        Args:
        - `expr` — Expression of `(U)Int*` type. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of `(U)Int*` type. [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitAnd", *to_args(locals()))
    
    @staticmethod
    def groupBitOr(expr: Any) -> Function:
        """
        groupBitOr(expr)

        Args:
        - `expr` — Expression of `(U)Int*` type. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of `(U)Int*` type. [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitOr", *to_args(locals()))
    
    @staticmethod
    def groupBitXor(expr: Any) -> Function:
        """
        groupBitXor(expr)

        Args:
        - `expr` — Expression of `(U)Int*` type. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value of `(U)Int*` type. [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitXor", *to_args(locals()))
    
    @staticmethod
    def groupBitmap(expr: Any) -> Function:
        """
        groupBitmap(expr)
        groupBitmapState(expr)

        Args:
        - `expr` — Expression that results in a `UInt*` type. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns the count of type UInt64 type, or a bitmap object when using `-State`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitmap", *to_args(locals()))
    
    @staticmethod
    def groupBitmapAnd(expr: Any) -> Function:
        """
        groupBitmapAnd(expr)
        groupBitmapAndState(expr)

        Args:
        - `expr` — Expression that results in an `AggregateFunction(groupBitmap, UInt*)` type. [`AggregateFunction(groupBitmap, UInt*)`](/sql-reference/data-types/aggregatefunction)

        Returns a count of type `UInt64`, or a bitmap object when using `-State`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitmapAnd", *to_args(locals()))
    
    @staticmethod
    def groupBitmapOr(expr: Any) -> Function:
        """
        groupBitmapOr(expr)
        groupBitmapOrState(expr)

        Args:
        - `expr` — Expression that results in an `AggregateFunction(groupBitmap, UInt*)` type. [`AggregateFunction(groupBitmap, UInt*)`](/sql-reference/data-types/aggregatefunction)

        Returns a count of type `UInt64`, or a bitmap object when using `-State`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitmapOr", *to_args(locals()))
    
    @staticmethod
    def groupBitmapXor(expr: Any) -> Function:
        """
        groupBitmapXor(expr)
        groupBitmapXorState(expr)

        Args:
        - `expr` — Expression that results in an `AggregateFunction(groupBitmap, UInt*)` type. [`AggregateFunction(groupBitmap, UInt*)`](/sql-reference/data-types/aggregatefunction)

        Returns a count of type `UInt64`, or a bitmap object when using `-State`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("groupBitmapXor", *to_args(locals()))
    
    @staticmethod
    def groupConcat(delimiter: Any, limit: Any | None = None) -> Function:
        """
        groupConcat[(delimiter [, limit])](expression)

        Args:
        - `expression` — The expression or column name that outputs strings to be concatenated. [`String`](/sql-reference/data-types/string)
        - `delimiter` — A string that will be used to separate concatenated values. This parameter is optional and defaults to an empty string or delimiter from parameters if not specified. [`String`](/sql-reference/data-types/string)

        Returns a string consisting of the concatenated values of the column or expression. If the group has no elements or only null elements, and the function does not specify a handling for only null values, the result is a nullable string with a null value. [`String`](/sql-reference/data-types/string)
        """
        return Function("groupConcat", *to_args(locals()))
    
    @staticmethod
    def groupNumericIndexedVector(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("groupNumericIndexedVector", *to_args(locals()))
    
    @staticmethod
    def groupUniqArray(x: Any) -> Function:
        """
        groupUniqArray(x)
        groupUniqArray(max_size)(x)

        Args:
        - `x` — Expression. [`Any`](/sql-reference/data-types)

        Returns an array of unique values. [`Array`](/sql-reference/data-types/array)
        """
        return Function("groupUniqArray", *to_args(locals()))
    
    @staticmethod
    def h3CellAreaM2(index: Any) -> Function:
        """
        h3CellAreaM2(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the exact area of the H3 cell in square meters. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3CellAreaM2", *to_args(locals()))
    
    @staticmethod
    def h3CellAreaRads2(index: Any) -> Function:
        """
        h3CellAreaRads2(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the exact area of the H3 cell in square radians. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3CellAreaRads2", *to_args(locals()))
    
    @staticmethod
    def h3Distance(start: Any, end: Any) -> Function:
        """
        h3Distance(start, end)

        Args:
        - `start` — Hexagon index number that represents the starting point. [`UInt64`](/sql-reference/data-types/int-uint)
        - `end` — Hexagon index number that represents the ending point. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the number of grid cells between the start and end indices. Returns a negative number if the distance cannot be computed. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3Distance", *to_args(locals()))
    
    @staticmethod
    def h3EdgeAngle(resolution: Any) -> Function:
        """
        h3EdgeAngle(resolution)

        Args:
        - `resolution` — Index resolution. Range: `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the average length of an [H3](#h3-index) hexagon edge in grades. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3EdgeAngle", *to_args(locals()))
    
    @staticmethod
    def h3EdgeLengthKm(resolution: Any) -> Function:
        """
        h3EdgeLengthKm(resolution)

        Args:
        - `resolution` — Index resolution with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the average length of an [H3](#h3-index) hexagon edge in kilometers. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3EdgeLengthKm", *to_args(locals()))
    
    @staticmethod
    def h3EdgeLengthM(resolution: Any) -> Function:
        """
        h3EdgeLengthM(resolution)

        Args:
        - `resolution` — Index resolution. Range: `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the average edge length of an [H3](#h3-index) hexagon in meters. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3EdgeLengthM", *to_args(locals()))
    
    @staticmethod
    def h3ExactEdgeLengthKm(index: Any) -> Function:
        """
        h3ExactEdgeLengthKm(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the exact length of the H3 edge in kilometers. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3ExactEdgeLengthKm", *to_args(locals()))
    
    @staticmethod
    def h3ExactEdgeLengthM(index: Any) -> Function:
        """
        h3ExactEdgeLengthM(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the exact length of the H3 edge in meters. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3ExactEdgeLengthM", *to_args(locals()))
    
    @staticmethod
    def h3ExactEdgeLengthRads(index: Any) -> Function:
        """
        h3ExactEdgeLengthRads(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the exact length of the H3 edge in radians. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3ExactEdgeLengthRads", *to_args(locals()))
    
    @staticmethod
    def h3GetBaseCell(index: Any) -> Function:
        """
        h3GetBaseCell(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the hexagon base cell number. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3GetBaseCell", *to_args(locals()))
    
    @staticmethod
    def h3GetDestinationIndexFromUnidirectionalEdge(edge: Any) -> Function:
        """
        h3GetDestinationIndexFromUnidirectionalEdge(edge)

        Args:
        - `edge` — Hexagon index number that represents a unidirectional edge. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the destination hexagon index from the unidirectional edge. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3GetDestinationIndexFromUnidirectionalEdge", *to_args(locals()))
    
    @staticmethod
    def h3GetFaces(index: Any) -> Function:
        """
        h3GetFaces(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array containing the indices (0-19) of the icosahedron faces that the H3 index intersects with. [`Array(UInt8)`](/sql-reference/data-types/array)
        """
        return Function("h3GetFaces", *to_args(locals()))
    
    @staticmethod
    def h3GetIndexesFromUnidirectionalEdge(edge: Any) -> Function:
        """
        h3GetIndexesFromUnidirectionalEdge(edge)

        Args:
        - `edge` — Hexagon index number that represents a unidirectional edge. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple containing the origin and destination hexagon indices from the unidirectional edge, or `(0,0)` if the input is not valid. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("h3GetIndexesFromUnidirectionalEdge", *to_args(locals()))
    
    @staticmethod
    def h3GetOriginIndexFromUnidirectionalEdge(edge: Any) -> Function:
        """
        h3GetOriginIndexFromUnidirectionalEdge(edge)

        Args:
        - `edge` — Hexagon index number that represents a unidirectional edge. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the origin hexagon index from the unidirectional edge. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3GetOriginIndexFromUnidirectionalEdge", *to_args(locals()))
    
    @staticmethod
    def h3GetPentagonIndexes(resolution: Any) -> Function:
        """
        h3GetPentagonIndexes(resolution)

        Args:
        - `resolution` — Index resolution with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns an array of all pentagon H3 indices at the specified resolution. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3GetPentagonIndexes", *to_args(locals()))
    
    @staticmethod
    def h3GetRes0Indexes() -> Function:
        """
        h3GetRes0Indexes()

        
        Returns an array of all resolution 0 H3 indices. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3GetRes0Indexes", *to_args(locals()))
    
    @staticmethod
    def h3GetResolution(index: Any) -> Function:
        """
        h3GetResolution(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the resolution of the H3 index with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3GetResolution", *to_args(locals()))
    
    @staticmethod
    def h3GetUnidirectionalEdge(origin: Any, destination: Any) -> Function:
        """
        h3GetUnidirectionalEdge(origin, destination)

        Args:
        - `origin` — The origin H3 cell index. [`UInt64`](/sql-reference/data-types/int-uint)
        - `destination` — The destination H3 cell index. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the H3 unidirectional edge index. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3GetUnidirectionalEdge", *to_args(locals()))
    
    @staticmethod
    def h3GetUnidirectionalEdgeBoundary(index: Any) -> Function:
        """
        h3GetUnidirectionalEdgeBoundary(index)

        Args:
        - `index` — Hexagon index number that represents a unidirectional edge. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of (longitude, latitude) pairs defining a unidirectional edge. [`Array(Float64, Float64)`](/sql-reference/data-types/array)
        """
        return Function("h3GetUnidirectionalEdgeBoundary", *to_args(locals()))
    
    @staticmethod
    def h3GetUnidirectionalEdgesFromHexagon(index: Any) -> Function:
        """
        h3GetUnidirectionalEdgesFromHexagon(index)

        Args:
        - `index` — Hexagon index number that represents a cell. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of H3 indexes representing each unidirectional edge. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3GetUnidirectionalEdgesFromHexagon", *to_args(locals()))
    
    @staticmethod
    def h3HexAreaKm2(resolution: Any) -> Function:
        """
        h3HexAreaKm2(resolution)

        Args:
        - `resolution` — Index resolution with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the average area of an H3 hexagon in square kilometers for the given resolution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3HexAreaKm2", *to_args(locals()))
    
    @staticmethod
    def h3HexAreaM2(resolution: Any) -> Function:
        """
        h3HexAreaM2(resolution)

        Args:
        - `resolution` — Index resolution with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the average area of an H3 hexagon in square meters for the given resolution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3HexAreaM2", *to_args(locals()))
    
    @staticmethod
    def h3HexRing(index: Any, k: Any) -> Function:
        """
        h3HexRing(index, k)

        Args:
        - `index` — Hexagon index number that represents the origin. [`UInt64`](/sql-reference/data-types/int-uint)
        - `k` — Distance from the origin (ring size). [`UInt16`](/sql-reference/data-types/int-uint)

        Returns an array of H3 indices forming a hexagonal ring around the origin, or `0` if a pentagonal distortion is encountered. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3HexRing", *to_args(locals()))
    
    @staticmethod
    def h3IndexesAreNeighbors(index1: Any, index2: Any) -> Function:
        """
        h3IndexesAreNeighbors(index1, index2)

        Args:
        - `index1` — First H3 index. [`UInt64`](/sql-reference/data-types/int-uint)
        - `index2` — Second H3 index. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns `1` if the indexes are neighbors (sharing an edge), `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3IndexesAreNeighbors", *to_args(locals()))
    
    @staticmethod
    def h3IsPentagon(index: Any) -> Function:
        """
        h3IsPentagon(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns `1` if the index represents a pentagonal cell, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3IsPentagon", *to_args(locals()))
    
    @staticmethod
    def h3IsResClassIII(index: Any) -> Function:
        """
        h3IsResClassIII(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns `1` if the index has a Class III resolution (odd-numbered), `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3IsResClassIII", *to_args(locals()))
    
    @staticmethod
    def h3IsValid(h3index: Any) -> Function:
        """
        h3IsValid(h3index)

        Args:
        - `h3index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns `1` if the number is a valid H3 index, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3IsValid", *to_args(locals()))
    
    @staticmethod
    def h3Line(start: Any, end: Any) -> Function:
        """
        h3Line(start, end)

        Args:
        - `start` — Hexagon index number that represents the starting point. [`UInt64`](/sql-reference/data-types/int-uint)
        - `end` — Hexagon index number that represents the ending point. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of H3 indices representing the line between the start and end indices. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3Line", *to_args(locals()))
    
    @staticmethod
    def h3NumHexagons(resolution: Any) -> Function:
        """
        h3NumHexagons(resolution)

        Args:
        - `resolution` — Index resolution with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the number of unique H3 indices at the specified resolution. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3NumHexagons", *to_args(locals()))
    
    @staticmethod
    def h3PointDistKm(lat1: Any, lon1: Any, lat2: Any, lon2: Any) -> Function:
        """
        h3PointDistKm(lat1, lon1, lat2, lon2)

        Args:
        - `lat1` — Latitude of point1 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon1` — Longitude of point1 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lat2` — Latitude of point2 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon2` — Longitude of point2 in degrees. [`Float64`](/sql-reference/data-types/float)

        Returns the haversine or great circle distance in kilometers. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3PointDistKm", *to_args(locals()))
    
    @staticmethod
    def h3PointDistM(lat1: Any, lon1: Any, lat2: Any, lon2: Any) -> Function:
        """
        h3PointDistM(lat1, lon1, lat2, lon2)

        Args:
        - `lat1` — Latitude of point1 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon1` — Longitude of point1 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lat2` — Latitude of point2 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon2` — Longitude of point2 in degrees. [`Float64`](/sql-reference/data-types/float)

        Returns the haversine or great circle distance in meters. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3PointDistM", *to_args(locals()))
    
    @staticmethod
    def h3PointDistRads(lat1: Any, lon1: Any, lat2: Any, lon2: Any) -> Function:
        """
        h3PointDistRads(lat1, lon1, lat2, lon2)

        Args:
        - `lat1` — Latitude of point1 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon1` — Longitude of point1 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lat2` — Latitude of point2 in degrees. [`Float64`](/sql-reference/data-types/float)
        - `lon2` — Longitude of point2 in degrees. [`Float64`](/sql-reference/data-types/float)

        Returns the haversine or great circle distance in radians. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("h3PointDistRads", *to_args(locals()))
    
    @staticmethod
    def h3PolygonToCells(geometry: Any, resolution: Any) -> Function:
        """
        h3PolygonToCells(geometry, resolution)

        
        
        """
        return Function("h3PolygonToCells", *to_args(locals()))
    
    @staticmethod
    def h3ToCenterChild(index: Any, resolution: Any) -> Function:
        """
        h3ToCenterChild(index, resolution)

        Args:
        - `index` — Parent H3 index. [`UInt64`](/sql-reference/data-types/int-uint)
        - `resolution` — Resolution of the center child with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the H3 index of the center child at the specified resolution. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3ToCenterChild", *to_args(locals()))
    
    @staticmethod
    def h3ToChildren(index: Any, resolution: Any) -> Function:
        """
        h3ToChildren(index, resolution)

        Args:
        - `index` — Parent H3 index. [`UInt64`](/sql-reference/data-types/int-uint)
        - `resolution` — Resolution of the child indexes with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns an array of child H3 indexes at the specified resolution. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3ToChildren", *to_args(locals()))
    
    @staticmethod
    def h3ToGeo(h3Index: Any) -> Function:
        """
        h3ToGeo(h3Index)

        Args:
        - `h3Index` — H3 index. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple consisting of two values `(lat, lon)` where `lat` is latitude and `lon` is longitude. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("h3ToGeo", *to_args(locals()))
    
    @staticmethod
    def h3ToGeoBoundary(h3Index: Any) -> Function:
        """
        h3ToGeoBoundary(h3Index)

        Args:
        - `h3Index` — H3 index. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of coordinate pairs `(lat, lon)` that define the boundary of the H3 hexagon. [`Array(Tuple(Float64, Float64))`](/sql-reference/data-types/array)
        """
        return Function("h3ToGeoBoundary", *to_args(locals()))
    
    @staticmethod
    def h3ToParent(index: Any, resolution: Any) -> Function:
        """
        h3ToParent(index, resolution)

        Args:
        - `index` — Child H3 index. [`UInt64`](/sql-reference/data-types/int-uint)
        - `resolution` — Resolution of the parent index with range `[0, 15]`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the parent H3 index at the specified resolution. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("h3ToParent", *to_args(locals()))
    
    @staticmethod
    def h3ToString(index: Any) -> Function:
        """
        h3ToString(index)

        Args:
        - `index` — H3 index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the string representation of the H3 index. [`String`](/sql-reference/data-types/string)
        """
        return Function("h3ToString", *to_args(locals()))
    
    @staticmethod
    def h3UnidirectionalEdgeIsValid(index: Any) -> Function:
        """
        h3UnidirectionalEdgeIsValid(index)

        Args:
        - `index` — Hexagon index number. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns `1` if the H3 index is a valid unidirectional edge, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("h3UnidirectionalEdgeIsValid", *to_args(locals()))
    
    @staticmethod
    def h3kRing(h3index: Any, k: Any) -> Function:
        """
        h3kRing(h3index, k)

        Args:
        - `h3index` — H3 index of the origin hexagon. [`UInt64`](/sql-reference/data-types/int-uint)
        - `k` — Radius [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an array of H3 indexes that are within `k` rings of the origin hexagon. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("h3kRing", *to_args(locals()))
    
    @staticmethod
    def halfMD5(arg1: Any, arg2: Any | None = None, argN: Any | None = None) -> Function:
        """
        halfMD5(arg1[, arg2, ..., argN])

        Args:
        - `arg1[, arg2, ..., argN]` — Variable number of arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed half MD5 hash of the given input params returned as a `UInt64` in big-endian byte order. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("halfMD5", *to_args(locals()))
    
    @staticmethod
    def has(haystack: Any, needle: Any) -> Function:
        """
        has(haystack, needle)

        Args:
        - `haystack` — The source array, map, or JSON. [`Array`](/sql-reference/data-types/array) or [`Map`](/sql-reference/data-types/map) or [`JSON`](/sql-reference/data-types/newjson)
        - `needle` — The value to search for (element in array, key in map, or path string in JSON). 
        Returns `1` if the haystack contains the specified needle, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("has", *to_args(locals()))
    
    @staticmethod
    def hasAll(set: Any, subset: Any) -> Function:
        """
        hasAll(set, subset)

        Args:
        - `set` — Array of any type with a set of elements. [`Array(T)`](/sql-reference/data-types/array)
        - `subset` — Array of any type that shares a common supertype with `set` containing elements that should be tested to be a subset of `set`. [`Array(T)`](/sql-reference/data-types/array)

        - `1`, if `set` contains all of the elements from `subset`.
        - `0`, otherwise.

        Raises a `NO_COMMON_TYPE` exception if the set and subset elements do not share a common supertype.
        """
        return Function("hasAll", *to_args(locals()))
    
    @staticmethod
    def hasAllTokens(input: Any, needles: Any) -> Function:
        """
        hasAllTokens(input, needles)

        Args:
        - `input` — The input column. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Array(String)`](/sql-reference/data-types/array) or [`Array(FixedString)`](/sql-reference/data-types/array)
        - `needles` — Tokens to be searched. [`String`](/sql-reference/data-types/string) or [`Array(String)`](/sql-reference/data-types/array)
        - `tokenizer` — The tokenizer to use. Valid arguments are `splitByNonAlpha`, `ngrams`, `splitByString`, `array`, and `sparseGrams`. Optional, if not set explicitly, defaults to `splitByNonAlpha`. [`const String`](/sql-reference/data-types/string)

        Returns 1, if all needles match. 0, otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasAllTokens", *to_args(locals()))
    
    @staticmethod
    def hasAny(arr_x: Any, arr_y: Any) -> Function:
        """
        hasAny(arr_x, arr_y)

        Args:
        - `arr_x` — Array of any type with a set of elements. [`Array(T)`](/sql-reference/data-types/array)
        - `arr_y` — Array of any type that shares a common supertype with array `arr_x`. [`Array(T)`](/sql-reference/data-types/array)

        - `1`, if `arr_x` and `arr_y` have one similar element at least.
        - `0`, otherwise.

        Raises a `NO_COMMON_TYPE` exception if any of the elements of the two arrays do not share a common supertype.
        """
        return Function("hasAny", *to_args(locals()))
    
    @staticmethod
    def hasAnyTokens(input: Any, needles: Any) -> Function:
        """
        hasAnyTokens(input, needles)

        Args:
        - `input` — The input column. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Nullable(String)`](/sql-reference/data-types/nullable) or [`Nullable(FixedString)`](/sql-reference/data-types/nullable) or [`Array(String)`](/sql-reference/data-types/array) or [`Array(FixedString)`](/sql-reference/data-types/array) or [`Array(Nullable(String))`](/sql-reference/data-types/array) or [`Array(Nullable(FixedString))`](/sql-reference/data-types/array)
        - `needles` — Tokens to be searched. [`String`](/sql-reference/data-types/string) or [`Array(String)`](/sql-reference/data-types/array)
        - `tokenizer` — The tokenizer to use. Valid arguments are `splitByNonAlpha`, `ngrams`, `splitByString`, `array`, and `sparseGrams`. Optional, if not set explicitly, defaults to `splitByNonAlpha`. [`const String`](/sql-reference/data-types/string)

        Returns `1`, if there was at least one match. `0`, otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasAnyTokens", *to_args(locals()))
    
    @staticmethod
    def hasColumnInTable(hostname: Any | None = None, username: Any | None = None, password: Any | None = None, database: Any | None = None, table: Any | None = None, column: Any | None = None) -> Function:
        """
        hasColumnInTable([hostname[, username[, password]],]database, table, column)

        Args:
        - `database` — Name of the database. [`const String`](/sql-reference/data-types/string)
        - `table` — Name of the table. [`const String`](/sql-reference/data-types/string)
        - `column` — Name of the column. [`const String`](/sql-reference/data-types/string)
        - `hostname` — Optional. Remote server name to perform the check on. [`const String`](/sql-reference/data-types/string)
        - `username` — Optional. Username for remote server. [`const String`](/sql-reference/data-types/string)
        - `password` — Optional. Password for remote server. [`const String`](/sql-reference/data-types/string)

        Returns `1` if the given column exists, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasColumnInTable", *to_args(locals()))
    
    @staticmethod
    def hasSubsequence(haystack: Any, needle: Any) -> Function:
        """
        hasSubsequence(haystack, needle)

        Args:
        - `haystack` — String in which to search for the subsequence. [`String`](/sql-reference/data-types/string)
        - `needle` — Subsequence to be searched. [`String`](/sql-reference/data-types/string)

        Returns `1` if needle is a subsequence of haystack, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasSubsequence", *to_args(locals()))
    
    @staticmethod
    def hasSubsequenceCaseInsensitive(haystack: Any, needle: Any) -> Function:
        """
        hasSubsequenceCaseInsensitive(haystack, needle)

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Subsequence to be searched. [`String`](/sql-reference/data-types/string)

        Returns 1, if needle is a subsequence of haystack, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasSubsequenceCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def hasSubsequenceCaseInsensitiveUTF8(haystack: Any, needle: Any) -> Function:
        """
        hasSubsequenceCaseInsensitiveUTF8(haystack, needle)

        Args:
        - `haystack` — UTF8-encoded string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — UTF8-encoded subsequence string to be searched. [`String`](/sql-reference/data-types/string)

        Returns 1, if needle is a subsequence of haystack, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasSubsequenceCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def hasSubsequenceUTF8(haystack: Any, needle: Any) -> Function:
        """
        hasSubsequenceUTF8(haystack, needle)

        Args:
        - `haystack` — The string in which to search. [`String`](/sql-reference/data-types/string)
        - `needle` — The subsequence to search for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `needle` is a subsequence of `haystack`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasSubsequenceUTF8", *to_args(locals()))
    
    @staticmethod
    def hasSubstr(arr1: Any, arr2: Any) -> Function:
        """
        hasSubstr(arr1, arr2)

        Args:
        - `arr1` — Array of any type with a set of elements. [`Array(T)`](/sql-reference/data-types/array)
        - `arr2` — Array of any type with a set of elements. [`Array(T)`](/sql-reference/data-types/array)

        Returns `1` if array `arr1` contains array `arr2`. Otherwise, returns `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasSubstr", *to_args(locals()))
    
    @staticmethod
    def hasThreadFuzzer() -> Function:
        """
        hasThreadFuzzer()

        
        Returns whether Thread Fuzzer is effective. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasThreadFuzzer", *to_args(locals()))
    
    @staticmethod
    def hasToken(haystack: Any, token: Any) -> Function:
        """
        hasToken(haystack, token)

        Args:
        - `haystack` — String to be searched. [`String`](/sql-reference/data-types/string)
        - `token` — Token to search for. [`const String`](/sql-reference/data-types/string)

        Returns `1` if the token is found, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("hasToken", *to_args(locals()))
    
    @staticmethod
    def hasTokenCaseInsensitive(haystack: Any, needle: Any) -> Function:
        """
        hasTokenCaseInsensitive(haystack, needle)

        
        
        """
        return Function("hasTokenCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def hasTokenCaseInsensitiveOrNull(haystack: Any, needle: Any) -> Function:
        """
        hasTokenCaseInsensitiveOrNull(haystack, needle)

        
        
        """
        return Function("hasTokenCaseInsensitiveOrNull", *to_args(locals()))
    
    @staticmethod
    def hasTokenOrNull(haystack: Any, token: Any) -> Function:
        """
        hasTokenOrNull(haystack, token)

        Args:
        - `haystack` — String to be searched. Must be constant. [`String`](/sql-reference/data-types/string)
        - `token` — Token to search for. [`const String`](/sql-reference/data-types/string)

        Returns `1` if the token is found, `0` otherwise, null if token is ill-formed. [`Nullable(UInt8)`](/sql-reference/data-types/nullable)
        """
        return Function("hasTokenOrNull", *to_args(locals()))
    
    @staticmethod
    def hex(arg: Any) -> Function:
        """
        hex(arg)

        Args:
        - `arg` — A value to convert to hexadecimal. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns a string with the hexadecimal representation of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("hex", *to_args(locals()))
    
    @staticmethod
    def hilbertDecode(tuple_size: Any, code: Any) -> Function:
        """
        hilbertDecode(tuple_size, code)

        Args:
        - `tuple_size` — Integer value of no more than `2`. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint) or [`Tuple(UInt8/16/32/64)`](/sql-reference/data-types/tuple)
        - `code` — `UInt64` code. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple of the specified size. [`Tuple(UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("hilbertDecode", *to_args(locals()))
    
    @staticmethod
    def hilbertEncode(args: Any) -> Function:
        """
        -- Simplified mode
        hilbertEncode(args)

        -- Expanded mode
        hilbertEncode(range_mask, args)

        Args:
        - `args` — Up to two `UInt` values or columns of type `UInt`. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)
        - `range_mask` — For the expanded mode, up to two `UInt` values or columns of type `UInt`. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns a `UInt64` code. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("hilbertEncode", *to_args(locals()))
    
    @staticmethod
    def histogram(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("histogram", *to_args(locals()))
    
    @staticmethod
    def hiveHash(arg: Any) -> Function:
        """
        hiveHash(arg)

        Args:
        - `arg` — Input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the computed "hive hash" of the input string. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("hiveHash", *to_args(locals()))
    
    @staticmethod
    def hop(time_attr: Any, hop_interval: Any, window_interval: Any, timezone: Any | None = None) -> Function:
        """
        hop(time_attr, hop_interval, window_interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `hop_interval` — Positive Hop interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `window_interval` — Positive Window interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the inclusive lower and exclusive upper bound of the corresponding hopping window. [`Tuple(DateTime, DateTime)`](/sql-reference/data-types/tuple)
        """
        return Function("hop", *to_args(locals()))
    
    @staticmethod
    def hopEnd(time_attr: Any, hop_interval: Any, window_interval: Any, timezone: Any | None = None) -> Function:
        """
        hopEnd(time_attr, hop_interval, window_interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `hop_interval` — Positive Hop interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `window_interval` — Positive Window interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the exclusive upper bound of the corresponding hopping window. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("hopEnd", *to_args(locals()))
    
    @staticmethod
    def hopStart(time_attr: Any, hop_interval: Any, window_interval: Any, timezone: Any | None = None) -> Function:
        """
        hopStart(time_attr, hop_interval, window_interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `hop_interval` — Positive Hop interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `window_interval` — Positive Window interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the inclusive lower bound of the corresponding hopping window. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("hopStart", *to_args(locals()))
    
    @staticmethod
    def hostName() -> Function:
        """
        hostName()

        
        Returns the host name. [`String`](/sql-reference/data-types/string)
        """
        return Function("hostName", *to_args(locals()))
    
    @staticmethod
    def hypot(x: Any, y: Any) -> Function:
        """
        hypot(x, y)

        Args:
        - `x` — The first cathetus of a right-angle triangle. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        - `y` — The second cathetus of a right-angle triangle. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the length of the hypotenuse of a right-angle triangle. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("hypot", *to_args(locals()))
    
    @staticmethod
    def icebergBucket(N: Any, value: Any) -> Function:
        """
        icebergBucket(N, value)

        Args:
        - `N` — The number of buckets, modulo. [`const (U)Int*`](/sql-reference/data-types/int-uint)
        - `value` — The source value to transform. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Bool`](/sql-reference/data-types/boolean) or [`Decimal`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`UUID`](/sql-reference/data-types/uuid) or [`Date`](/sql-reference/data-types/date) or [`Time`](/sql-reference/data-types/time) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns a 32-bit hash of the source value. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("icebergBucket", *to_args(locals()))
    
    @staticmethod
    def icebergHash(value: Any) -> Function:
        """
        icebergHash(value)

        Args:
        - `value` — Source value to take the hash of [`Integer`](/sql-reference/data-types/int-uint) or [`Bool`](/sql-reference/data-types/boolean) or [`Decimal`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`UUID`](/sql-reference/data-types/uuid) or [`Date`](/sql-reference/data-types/date) or [`Time`](/sql-reference/data-types/time) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns a 32-bit Murmur3 hash, x86 variant, seeded with 0 [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("icebergHash", *to_args(locals()))
    
    @staticmethod
    def icebergTruncate(N: Any, value: Any) -> Function:
        """
        icebergTruncate(N, value)

        Args:
        - `value` — The value to transform. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal`](/sql-reference/data-types/decimal)

        The same type as the argument
        """
        return Function("icebergTruncate", *to_args(locals()))
    
    @staticmethod
    def identity(x: Any) -> Function:
        """
        identity(x)

        Args:
        - `x` — Input value. [`Any`](/sql-reference/data-types)

        Returns the input value unchanged. [`Any`](/sql-reference/data-types)
        """
        return Function("identity", *to_args(locals()))
    
    @staticmethod
    def idnaDecode(s: Any) -> Function:
        """
        idnaDecode(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns a Unicode (UTF-8) representation of the input string according to the IDNA mechanism of the input value. [`String`](/sql-reference/data-types/string)
        """
        return Function("idnaDecode", *to_args(locals()))
    
    @staticmethod
    def idnaEncode(s: Any) -> Function:
        """
        idnaEncode(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns an ASCII representation of the input string according to the IDNA mechanism of the input value. [`String`](/sql-reference/data-types/string)
        """
        return Function("idnaEncode", *to_args(locals()))
    
    @staticmethod
    def if_(cond: Any, then: Any, else_: Any) -> Function:
        """
        if(cond, then, else)

        Args:
        - `cond` — The evaluated condition. [`UInt8`](/sql-reference/data-types/int-uint) or [`Nullable(UInt8)`](/sql-reference/data-types/nullable) or [`NULL`](/sql-reference/syntax#null)
        - `then` — The expression returned if `cond` is true. - `else` — The expression returned if `cond` is false or `NULL`. 
        The result of either the `then` or `else` expressions, depending on condition `cond`.
        """
        return Function("if", *to_args(locals()))
    
    @staticmethod
    def ifNotFinite(x: Any, y: Any) -> Function:
        """
        ifNotFinite(x,y)

        Args:
        - `x` — Value to check if infinite. [`Float*`](/sql-reference/data-types/float)
        - `y` — Fallback value. [`Float*`](/sql-reference/data-types/float)

        - `x` if `x` is finite.
        - `y` if `x` is not finite.
        """
        return Function("ifNotFinite", *to_args(locals()))
    
    @staticmethod
    def ifNull(x: Any, alt: Any) -> Function:
        """
        ifNull(x, alt)

        Args:
        - `x` — The value to check for `NULL`. [`Any`](/sql-reference/data-types)
        - `alt` — The value that the function returns if `x` is `NULL`. [`Any`](/sql-reference/data-types)

        Returns the value of `x` if it is not `NULL`, otherwise `alt`. [`Any`](/sql-reference/data-types)
        """
        return Function("ifNull", *to_args(locals()))
    
    @staticmethod
    def ignore(x: Any) -> Function:
        """
        ignore(x)

        Args:
        - `x` — An input value which is unused and passed only so as to avoid a syntax error. [`Any`](/sql-reference/data-types)

        Always returns `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("ignore", *to_args(locals()))
    
    @staticmethod
    def ilike(haystack: Any, pattern: Any) -> Function:
        """
        ilike(haystack, pattern)
        -- haystack ILIKE pattern

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `pattern` — LIKE pattern to match against. [`String`](/sql-reference/data-types/string)

        Returns `1` if the string matches the LIKE pattern (case-insensitive), otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("ilike", *to_args(locals()))
    
    @staticmethod
    def in_(x: Any, set: Any) -> Function:
        """
        in(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("in", *to_args(locals()))
    
    @staticmethod
    def inIgnoreSet(x: Any, set: Any) -> Function:
        """
        in(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("inIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def indexHint(expression: Any) -> Function:
        """
        indexHint(expression)

        Args:
        - `expression` — Any expression for index range selection. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns `1` in all cases. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("indexHint", *to_args(locals()))
    
    @staticmethod
    def indexOf(arr: Any, x: Any) -> Function:
        """
        indexOf(arr, x)

        Args:
        - `arr` — An array to search in for `x`. [`Array(T)`](/sql-reference/data-types/array)
        - `x` — Value of the first matching element in `arr` for which to return an index. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the index (numbered from one) of the first `x` in `arr` if it exists. Otherwise, returns `0`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("indexOf", *to_args(locals()))
    
    @staticmethod
    def indexOfAssumeSorted(arr: Any, x: Any) -> Function:
        """
        indexOfAssumeSorted(arr, x)

        Args:
        - `arr` — A sorted array to search. [`Array(T)`](/sql-reference/data-types/array)
        - `x` — Value of the first matching element in sorted `arr` for which to return an index. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns the index (numbered from one) of the first `x` in `arr` if it exists. Otherwise, returns `0`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("indexOfAssumeSorted", *to_args(locals()))
    
    @staticmethod
    def initcap(s: Any) -> Function:
        """
        initcap(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns `s` with the first letter of each word converted to upper case. [`String`](/sql-reference/data-types/string)
        """
        return Function("initcap", *to_args(locals()))
    
    @staticmethod
    def initcapUTF8(s: Any) -> Function:
        """
        initcapUTF8(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns `s` with the first letter of each word converted to upper case. [`String`](/sql-reference/data-types/string)
        """
        return Function("initcapUTF8", *to_args(locals()))
    
    @staticmethod
    def initialQueryID() -> Function:
        """
        initialQueryID()

        
        Returns the ID of the initial current query. [`String`](/sql-reference/data-types/string)
        """
        return Function("initialQueryID", *to_args(locals()))
    
    @staticmethod
    def initialQueryStartTime() -> Function:
        """
        initialQueryStartTime()

        
        Returns the start time of the initial current query. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("initialQueryStartTime", *to_args(locals()))
    
    @staticmethod
    def initializeAggregation(aggregate_function: Any, arg1: Any, arg2: Any | None = None) -> Function:
        """
        initializeAggregation(aggregate_function, arg1[, arg2, ...])

        Args:
        - `aggregate_function` — Name of the aggregation function to initialize. [`String`](/sql-reference/data-types/string)
        - `arg1[, arg2, ...]` — Arguments of the aggregate function. [`Any`](/sql-reference/data-types)

        Returns the result of aggregation for every row passed to the function. The return type is the same as the return type of the function that `initializeAggregation` takes as a first argument. [`Any`](/sql-reference/data-types)
        """
        return Function("initializeAggregation", *to_args(locals()))
    
    @staticmethod
    def intDiv(x: Any, y: Any) -> Function:
        """
        intDiv(x, y)

        Args:
        - `x` — Left hand operand. - `y` — Right hand operand. 
        Result of integer division of `x` and `y`
        """
        return Function("intDiv", *to_args(locals()))
    
    @staticmethod
    def intDivOrNull(x: Any, y: Any) -> Function:
        """
        intDivOrNull(x, y)

        Args:
        - `x` — Left hand operand. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `y` — Right hand operand. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Result of integer division of `x` and `y`, or NULL.
        """
        return Function("intDivOrNull", *to_args(locals()))
    
    @staticmethod
    def intDivOrZero(a: Any, b: Any) -> Function:
        """
        intDivOrZero(a, b)

        Args:
        - `a` — Left hand operand. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `b` — Right hand operand. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Result of integer division of a and b, or zero.
        """
        return Function("intDivOrZero", *to_args(locals()))
    
    @staticmethod
    def intExp10(x: Any) -> Function:
        """
        intExp10(x)

        Args:
        - `x` — The exponent. [`Int*`](/sql-reference/data-types/int-uint) or [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns 10^x. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("intExp10", *to_args(locals()))
    
    @staticmethod
    def intExp2(x: Any) -> Function:
        """
        intExp2(x)

        Args:
        - `x` — The exponent. [`Int*`](/sql-reference/data-types/int-uint) or [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns 2^x. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("intExp2", *to_args(locals()))
    
    @staticmethod
    def intHash32(arg: Any) -> Function:
        """
        intHash32(arg)

        Args:
        - `arg` — Integer to hash. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the computed 32-bit hash code of the input integer [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("intHash32", *to_args(locals()))
    
    @staticmethod
    def intHash64(int: Any) -> Function:
        """
        intHash64(int)

        Args:
        - `int` — Integer to hash. [`(U)Int*`](/sql-reference/data-types/int-uint)

        64-bit hash code. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("intHash64", *to_args(locals()))
    
    @staticmethod
    def intervalLengthSum(start: Any, end: Any) -> Function:
        """
        intervalLengthSum(start, end)

        Args:
        - `start` — The starting value of the interval. [`(U)Int32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`DateTime`](/sql-reference/data-types/datetime) or [`Date`](/sql-reference/data-types/date)
        - `end` — The ending value of the interval. [`(U)Int32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`DateTime`](/sql-reference/data-types/datetime) or [`Date`](/sql-reference/data-types/date)

        Returns the total length of union of all ranges (segments on numeric axis). Depending on the type of the argument, the return value may be UInt64 or Float64 type. [`UInt64`](/sql-reference/data-types/int-uint) or [`Float64`](/sql-reference/data-types/float)
        """
        return Function("intervalLengthSum", *to_args(locals()))
    
    @staticmethod
    def isConstant(x: Any) -> Function:
        """
        isConstant(x)

        Args:
        - `x` — An expression to check. [`Any`](/sql-reference/data-types)

        Returns `1` if `x` is constant, `0` if `x` is non-constant. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isConstant", *to_args(locals()))
    
    @staticmethod
    def isDecimalOverflow(value: Any, precision: Any | None = None) -> Function:
        """
        isDecimalOverflow(value[, precision])

        Args:
        - `value` — Decimal value to check. [`Decimal`](/sql-reference/data-types/decimal)
        - `precision` — Optional. The precision of the Decimal type. If omitted, the initial precision of the first argument is used. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns `1` if the decimal value has more digits than allowed by its precision, `0` if the decimal value satisfies the specified precision. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isDecimalOverflow", *to_args(locals()))
    
    @staticmethod
    def isDistinctFrom(x: Any, y: Any) -> Function:
        """
        isDistinctFrom(x, y)

        Args:
        - `x` — First value to compare. Can be any ClickHouse data type. [`Any`](/sql-reference/data-types)
        - `y` — Second value to compare. Can be any ClickHouse data type. [`Any`](/sql-reference/data-types)

        Returns `true` if the two values are different, treating NULLs as comparable:
          - Returns `true` if x != y.
          - Returns `true` if exactly one of x or y is NULL.
          - Returns `false` if x = y, or both x and y are NULL. [`Bool`](/sql-reference/data-types/boolean)
        """
        return Function("isDistinctFrom", *to_args(locals()))
    
    @staticmethod
    def isDynamicElementInSharedData(dynamic: Any) -> Function:
        """
        isDynamicElementInSharedData(dynamic)

        Args:
        - `dynamic` — Dynamic column to inspect. [`Dynamic`](/sql-reference/data-types/dynamic)

        Returns true if the value is stored in shared variant format, false if stored as a separate subcolumn or is NULL. [`Bool`](/sql-reference/data-types/boolean)
        """
        return Function("isDynamicElementInSharedData", *to_args(locals()))
    
    @staticmethod
    def isFinite(x: Any) -> Function:
        """
        isFinite(x)

        Args:
        - `x` — Number to check for finiteness. [`Float*`](/sql-reference/data-types/float)

        `1` if x is not infinite and not `NaN`, otherwise `0`.
        """
        return Function("isFinite", *to_args(locals()))
    
    @staticmethod
    def isIPAddressInRange(address: Any, prefix: Any) -> Function:
        """
        isIPAddressInRange(address, prefix)

        Args:
        - `address` — An IPv4 or IPv6 address. [`String`](/sql-reference/data-types/string)
        - `prefix` — An IPv4 or IPv6 network prefix in CIDR. [`String`](/sql-reference/data-types/string)

        Returns `1` if the IP version of the address and the CIDR match, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isIPAddressInRange", *to_args(locals()))
    
    @staticmethod
    def isIPv4String(string: Any) -> Function:
        """
        isIPv4String(string)

        Args:
        - `string` — IP address string to check. [`String`](/sql-reference/data-types/string)

        Returns `1` if `string` is IPv4 address, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isIPv4String", *to_args(locals()))
    
    @staticmethod
    def isIPv6String(string: Any) -> Function:
        """
        isIPv6String(string)

        Args:
        - `string` — IP address string to check. [`String`](/sql-reference/data-types/string)

        Returns `1` if `string` is IPv6 address, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isIPv6String", *to_args(locals()))
    
    @staticmethod
    def isInfinite(x: Any) -> Function:
        """
        isInfinite(x)

        Args:
        - `x` — Number to check for infiniteness. [`Float*`](/sql-reference/data-types/float)

        `1` if x is infinite, otherwise `0` (including for `NaN`).
        """
        return Function("isInfinite", *to_args(locals()))
    
    @staticmethod
    def isMergeTreePartCoveredBy(nested_part: Any, covering_part: Any) -> Function:
        """
        isMergeTreePartCoveredBy(nested_part, covering_part)

        Args:
        - `nested_part` — Name of expected nested part. [`String`](/sql-reference/data-types/string)
        - `covering_part` — Name of expected covering part. [`String`](/sql-reference/data-types/string)

        Returns `1` if it covers, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isMergeTreePartCoveredBy", *to_args(locals()))
    
    @staticmethod
    def isNaN(x: Any) -> Function:
        """
        isNaN(x)

        Args:
        - `x` — Argument to evaluate for if it is `NaN`. [`Float*`](/sql-reference/data-types/float)

        `1` if `NaN`, otherwise `0`
        """
        return Function("isNaN", *to_args(locals()))
    
    @staticmethod
    def isNotDistinctFrom(x: Any, y: Any) -> Function:
        """
        isNotDistinctFrom(x, y)

        Args:
        - `x` — First value to compare. Can be any ClickHouse data type. [`Any`](/sql-reference/data-types)
        - `y` — Second value to compare. Can be any ClickHouse data type. [`Any`](/sql-reference/data-types)

        Returns `true` if the two values are equal, treating NULLs as comparable:
          - Returns `true` if x = y.
          - Returns `true` if both x and y are NULL.
          - Returns `false` if x != y, or exactly one of x or y is NULL. [`Bool`](/sql-reference/data-types/boolean)
        """
        return Function("isNotDistinctFrom", *to_args(locals()))
    
    @staticmethod
    def isNotNull(x: Any) -> Function:
        """
        isNotNull(x)

        Args:
        - `x` — A value of non-compound data type. [`Any`](/sql-reference/data-types)

        Returns `1` if `x` is not `NULL`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isNotNull", *to_args(locals()))
    
    @staticmethod
    def isNull(x: Any) -> Function:
        """
        isNull(x)

        Args:
        - `x` — A value of non-compound data type. [`Any`](/sql-reference/data-types)

        Returns `1` if `x` is `NULL`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isNull", *to_args(locals()))
    
    @staticmethod
    def isNullable(x: Any) -> Function:
        """
        isNullable(x)

        Args:
        - `x` — A value of any data type. [`Any`](/sql-reference/data-types)

        Returns `1` if `x` is of a `Nullable` data type, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isNullable", *to_args(locals()))
    
    @staticmethod
    def isValidASCII(str: Any) -> Function:
        """
        isValidASCII(str)

        
        
        """
        return Function("isValidASCII", *to_args(locals()))
    
    @staticmethod
    def isValidJSON(json: Any) -> Function:
        """
        isValidJSON(json)

        Args:
        - `json` — JSON string to validate [`String`](/sql-reference/data-types/string)

        Returns `1` if the string is valid JSON, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isValidJSON", *to_args(locals()))
    
    @staticmethod
    def isValidUTF8(s: Any) -> Function:
        """
        isValidUTF8(s)

        Args:
        - `s` — The string to check for UTF-8 encoded validity. [`String`](/sql-reference/data-types/string)

        Returns `1`, if the set of bytes constitutes valid UTF-8-encoded text, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("isValidUTF8", *to_args(locals()))
    
    @staticmethod
    def isZeroOrNull(x: Any) -> Function:
        """
        isZeroOrNull(x)

        Args:
        - `x` — A numeric value. [`UInt`](/sql-reference/data-types/int-uint)

        Returns `1` if `x` is `NULL` or equal to zero, otherwise `0`. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float32/Float64`](/sql-reference/data-types/float)
        """
        return Function("isZeroOrNull", *to_args(locals()))
    
    @staticmethod
    def jaroSimilarity(s1: Any, s2: Any) -> Function:
        """
        jaroSimilarity(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the Jaro similarity between the two strings. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("jaroSimilarity", *to_args(locals()))
    
    @staticmethod
    def jaroWinklerSimilarity(s1: Any, s2: Any) -> Function:
        """
        jaroWinklerSimilarity(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the Jaro-Winkler similarity between the two strings. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("jaroWinklerSimilarity", *to_args(locals()))
    
    @staticmethod
    def javaHash(arg: Any) -> Function:
        """
        javaHash(arg)

        Args:
        - `arg` — Input value to hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash of `arg` [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("javaHash", *to_args(locals()))
    
    @staticmethod
    def javaHashUTF16LE(arg: Any) -> Function:
        """
        javaHashUTF16LE(arg)

        Args:
        - `arg` — A string in UTF-16LE encoding. [`String`](/sql-reference/data-types/string)

        Returns the computed hash of the UTF-16LE encoded string. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("javaHashUTF16LE", *to_args(locals()))
    
    @staticmethod
    def joinGet(join_storage_table_name: Any, value_column: Any, join_keys: Any) -> Function:
        """
        joinGet(join_storage_table_name, value_column, join_keys)

        Args:
        - `join_storage_table_name` — An identifier which indicates where to perform the search. The identifier is searched in the default database (see parameter `default_database` in the config file). To override the default database, use the `USE database_name` query or specify the database and the table through a dot, like `database_name.table_name`. [`String`](/sql-reference/data-types/string)
        - `value_column` — The name of the column of the table that contains required data. [`const String`](/sql-reference/data-types/string)
        - `join_keys` — A list of join keys. [`Any`](/sql-reference/data-types)

        Returns list of values corresponded to list of keys. [`Any`](/sql-reference/data-types)
        """
        return Function("joinGet", *to_args(locals()))
    
    @staticmethod
    def joinGetOrNull(join_storage_table_name: Any, value_column: Any, join_keys: Any) -> Function:
        """
        joinGetOrNull(join_storage_table_name, value_column, join_keys)

        Args:
        - `join_storage_table_name` — An identifier which indicates where to perform the search. The identifier is searched in the default database (see parameter default_database in the config file). To override the default database, use the `USE database_name` query or specify the database and the table through a dot, like `database_name.table_name`. [`String`](/sql-reference/data-types/string)
        - `value_column` — The name of the column of the table that contains required data. [`const String`](/sql-reference/data-types/string)
        - `join_keys` — A list of join keys. [`Any`](/sql-reference/data-types)

        Returns a list of values corresponding to the list of keys, or `NULL` if a key is not found. [`Any`](/sql-reference/data-types)
        """
        return Function("joinGetOrNull", *to_args(locals()))
    
    @staticmethod
    def jumpConsistentHash(key: Any, buckets: Any) -> Function:
        """
        jumpConsistentHash(key, buckets)

        Args:
        - `key` — The input key. [`UInt64`](/sql-reference/data-types/int-uint)
        - `buckets` — The number of buckets. [`Int32`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("jumpConsistentHash", *to_args(locals()))
    
    @staticmethod
    def kafkaMurmurHash(arg1: Any, arg2: Any | None = None) -> Function:
        """
        kafkaMurmurHash(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of parameters for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the calculated hash value of the input arguments. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("kafkaMurmurHash", *to_args(locals()))
    
    @staticmethod
    def keccak256(message: Any) -> Function:
        """
        keccak256(message)

        Args:
        - `message` — The input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the 32-byte Keccak-256 hash of the input string as a fixed-length string. [`FixedString(32)`](/sql-reference/data-types/fixedstring)
        """
        return Function("keccak256", *to_args(locals()))
    
    @staticmethod
    def kolmogorovSmirnovTest(alternative: Any | None = None, computation_method: Any | None = None) -> Function:
        """
        kolmogorovSmirnovTest([alternative, computation_method])(sample_data, sample_index)

        Args:
        - `sample_data` — Sample data. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `sample_index` — Sample index. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a tuple with two elements: a calculated statistic and a calculated p-value. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("kolmogorovSmirnovTest", *to_args(locals()))
    
    @staticmethod
    def kostikConsistentHash(input: Any, n: Any) -> Function:
        """
        kostikConsistentHash(input, n)

        Args:
        - `input` — An integer key. [`UInt64`](/sql-reference/data-types/int-uint)
        - `n` — The number of buckets. [`UInt16`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("kostikConsistentHash", *to_args(locals()))
    
    @staticmethod
    def kql_array_sort_asc(array1: Any, array2: Any | None = None, nulls_last: Any | None = None) -> Function:
        """
        kql_array_sort_asc(array1[, array2, ..., nulls_last])

        Args:
        - `array1` — The array to sort. [`Array(T)`](/sql-reference/data-types/array)
        - `array2` — Optional. Additional arrays to reorder according to array1's sort order. [`Array(T)`](/sql-reference/data-types/array)
        - `nulls_last` — Optional. A boolean indicating whether nulls should appear last. Default is true. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple of arrays sorted in ascending order. [`Tuple(Array, ...)`](/sql-reference/data-types/tuple)
        """
        return Function("kql_array_sort_asc", *to_args(locals()))
    
    @staticmethod
    def kql_array_sort_desc(array1: Any, array2: Any | None = None, nulls_last: Any | None = None) -> Function:
        """
        kql_array_sort_desc(array1[, array2, ..., nulls_last])

        Args:
        - `array1` — The array to sort. [`Array(T)`](/sql-reference/data-types/array)
        - `array2` — Optional additional arrays to reorder according to array1's sort order. [`Array(T)`](/sql-reference/data-types/array)
        - `nulls_last` — Optional boolean indicating whether nulls should appear last. Default is true. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple of arrays sorted in descending order. [`Tuple(Array, ...)`](/sql-reference/data-types/tuple)
        """
        return Function("kql_array_sort_desc", *to_args(locals()))
    
    @staticmethod
    def kurtPop(expr: Any) -> Function:
        """
        kurtPop(expr)

        Args:
        - `expr` — [Expression](/sql-reference/syntax#expressions) returning a number. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the kurtosis of the given distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("kurtPop", *to_args(locals()))
    
    @staticmethod
    def kurtSamp(expr: Any) -> Function:
        """
        kurtSamp(expr)

        Args:
        - `expr` — [Expression](/sql-reference/syntax#expressions) returning a number. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the kurtosis of the given distribution. If `n <= 1` (`n` is a size of the sample), then the function returns `nan`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("kurtSamp", *to_args(locals()))
    
    @staticmethod
    def lag(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("lag", *to_args(locals()))
    
    @staticmethod
    def lagInFrame(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("lagInFrame", *to_args(locals()))
    
    @staticmethod
    def largestTriangleThreeBuckets(n: Any) -> Function:
        """
        largestTriangleThreeBuckets(n)(x, y)

        Args:
        - `x` — x coordinate. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `y` — y coordinate. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns an array of tuples with two elements.. [`Array(Tuple(Float64, Float64))`](/sql-reference/data-types/array)
        """
        return Function("largestTriangleThreeBuckets", *to_args(locals()))
    
    @staticmethod
    def lcm(x: Any, y: Any) -> Function:
        """
        lcm(x, y)

        Args:
        - `x` — First integer. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `y` — Second integer. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns the least common multiple of `x` and `y`. [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("lcm", *to_args(locals()))
    
    @staticmethod
    def lead(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("lead", *to_args(locals()))
    
    @staticmethod
    def leadInFrame(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("leadInFrame", *to_args(locals()))
    
    @staticmethod
    def least(x1: Any, x2: Any | None = None) -> Function:
        """
        least(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — A single value or multiple values to compare. All arguments must be of comparable types. [`Any`](/sql-reference/data-types)

        Returns the least value among the arguments, promoted to the largest compatible type. [`Any`](/sql-reference/data-types)
        """
        return Function("least", *to_args(locals()))
    
    @staticmethod
    def left(s: Any, offset: Any) -> Function:
        """
        left(s, offset)

        Args:
        - `s` — The string to calculate a substring from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `offset` — The number of bytes of the offset. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns:
        - For positive `offset`, a substring of `s` with `offset` many bytes, starting from the left of the string.
        - For negative `offset`, a substring of `s` with `length(s) - |offset|` bytes, starting from the left of the string.
        - An empty string if `length` is `0`.
             [`String`](/sql-reference/data-types/string)
        """
        return Function("left", *to_args(locals()))
    
    @staticmethod
    def leftPad(string: Any, length: Any, pad_string: Any | None = None) -> Function:
        """
        leftPad(string, length[, pad_string])

        Args:
        - `string` — Input string that should be padded. [`String`](/sql-reference/data-types/string)
        - `length` — The length of the resulting string. If the value is smaller than the input string length, then the input string is shortened to `length` characters. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `pad_string` — Optional. The string to pad the input string with. If not specified, then the input string is padded with spaces. [`String`](/sql-reference/data-types/string)

        Returns a left-padded string of the given length. [`String`](/sql-reference/data-types/string)
        """
        return Function("leftPad", *to_args(locals()))
    
    @staticmethod
    def leftPadUTF8(string: Any, length: Any, pad_string: Any | None = None) -> Function:
        """
        leftPadUTF8(string, length[, pad_string])

        Args:
        - `string` — Input string that should be padded. [`String`](/sql-reference/data-types/string)
        - `length` — The length of the resulting string. If the value is smaller than the input string length, then the input string is shortened to `length` characters. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `pad_string` — Optional. The string to pad the input string with. If not specified, then the input string is padded with spaces. [`String`](/sql-reference/data-types/string)

        Returns a left-padded string of the given length. [`String`](/sql-reference/data-types/string)
        """
        return Function("leftPadUTF8", *to_args(locals()))
    
    @staticmethod
    def leftUTF8(s: Any, offset: Any) -> Function:
        """
        leftUTF8(s, offset)

        Args:
        - `s` — The UTF-8 encoded string to calculate a substring from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `offset` — The number of bytes of the offset. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns:
        - For positive `offset`, a substring of `s` with `offset` many bytes, starting from the left of the string.\n"
        - For negative `offset`, a substring of `s` with `length(s) - |offset|` bytes, starting from the left of the string.\n"
        - An empty string if `length` is 0.
             [`String`](/sql-reference/data-types/string)
        """
        return Function("leftUTF8", *to_args(locals()))
    
    @staticmethod
    def lemmatize(lang: Any, word: Any) -> Function:
        """
        lemmatize(lang, word)

        Args:
        - `lang` — Language which rules will be applied. [`String`](/sql-reference/data-types/string)
        - `word` — Lowercase word that needs to be lemmatized. [`String`](/sql-reference/data-types/string)

        Returns the lemmatized form of the word [`String`](/sql-reference/data-types/string)
        """
        return Function("lemmatize", *to_args(locals()))
    
    @staticmethod
    def length(x: Any) -> Function:
        """
        length(x)

        Args:
        - `x` — Value for which to calculate the number of bytes (for String/FixedString) or elements (for Array). [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Array(T)`](/sql-reference/data-types/array)

        Returns the number of number of bytes in the String/FixedString `x` / the number of elements in array `x` [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("length", *to_args(locals()))
    
    @staticmethod
    def lengthUTF8(s: Any) -> Function:
        """
        lengthUTF8(s)

        Args:
        - `s` — String containing valid UTF-8 encoded text. [`String`](/sql-reference/data-types/string)

        Length of the string `s` in Unicode code points. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("lengthUTF8", *to_args(locals()))
    
    @staticmethod
    def less(a: Any, b: Any) -> Function:
        """
        less(a, b)
            -- a < b

        Args:
        - `a` — First value.<sup>[*](#comparison-rules)</sup> - `b` — Second value.<sup>[*](#comparison-rules)</sup> 
        Returns `1` if `a` is less than `b`, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("less", *to_args(locals()))
    
    @staticmethod
    def lessOrEquals(a: Any, b: Any) -> Function:
        """
        lessOrEquals(a, b)
        -- a <= b

        Args:
        - `a` — First value.<sup>[*](#comparison-rules)</sup> - `b` — Second value.<sup>[*](#comparison-rules)</sup> 
        Returns `1` if `a` is less than or equal to `b`, otherwise `0` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("lessOrEquals", *to_args(locals()))
    
    @staticmethod
    def lgamma(x: Any) -> Function:
        """
        lgamma(x)

        Args:
        - `x` — The number for which to compute the logarithm of the gamma function. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the logarithm of the gamma function of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("lgamma", *to_args(locals()))
    
    @staticmethod
    def like(haystack: Any, pattern: Any) -> Function:
        """
        like(haystack, pattern)
        -- haystack LIKE pattern

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `pattern` — `LIKE` pattern to match against. Can contain `%` (matches any number of characters), `_` (matches single character), and `\` for escaping. [`String`](/sql-reference/data-types/string)

        Returns `1` if the string matches the `LIKE` pattern, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("like", *to_args(locals()))
    
    @staticmethod
    def locate(needle: Any, haystack: Any, start_pos: Any | None = None) -> Function:
        """
        locate(needle, haystack[, start_pos])

        Args:
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `start_pos` — Optional. Position (1-based) in `haystack` at which the search starts. [`UInt`](/sql-reference/data-types/int-uint)

        Returns starting position in bytes and counting from 1, if the substring was found, `0`, if the substring was not found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("locate", *to_args(locals()))
    
    @staticmethod
    def log(x: Any) -> Function:
        """
        log(x)

        Args:
        - `x` — The number for which to compute the natural logarithm of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the natural logarithm of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("log", *to_args(locals()))
    
    @staticmethod
    def log10(x: Any) -> Function:
        """
        log10(x)

        Args:
        - `x` — Number for which to compute the decimal logarithm of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the decimal logarithm of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("log10", *to_args(locals()))
    
    @staticmethod
    def log1p(x: Any) -> Function:
        """
        log1p(x)

        Args:
        - `x` — Values from the interval: `-1 < x < +∞`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns values from the interval: -∞ < log1p(x) < +∞ [`Float64`](/sql-reference/data-types/float)
        """
        return Function("log1p", *to_args(locals()))
    
    @staticmethod
    def log2(x: Any) -> Function:
        """
        log2(x)

        Args:
        - `x` — The number for which to compute the binary logarithm of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the binary logarithm of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("log2", *to_args(locals()))
    
    @staticmethod
    def logTrace(message: Any) -> Function:
        """
        logTrace(message)

        Args:
        - `message` — Message that is emitted to the server log. [`const String`](/sql-reference/data-types/string)

        Returns `0` always. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("logTrace", *to_args(locals()))
    
    @staticmethod
    def lowCardinalityIndices(col: Any) -> Function:
        """
        lowCardinalityIndices(col)

        Args:
        - `col` — A low cardinality column. [`LowCardinality`](/sql-reference/data-types/lowcardinality)

        The position of the value in the dictionary of the current part. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("lowCardinalityIndices", *to_args(locals()))
    
    @staticmethod
    def lowCardinalityKeys(col: Any) -> Function:
        """
        lowCardinalityKeys(col)

        Args:
        - `col` — A low cardinality column. [`LowCardinality`](/sql-reference/data-types/lowcardinality)

        Returns the dictionary keys. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("lowCardinalityKeys", *to_args(locals()))
    
    @staticmethod
    def lower(s: Any) -> Function:
        """
        lower(s)

        Args:
        - `s` — A string to convert to lowercase. [`String`](/sql-reference/data-types/string)

        Returns a lowercase string from `s`. [`String`](/sql-reference/data-types/string)
        """
        return Function("lower", *to_args(locals()))
    
    @staticmethod
    def lowerUTF8(input: Any) -> Function:
        """
        lowerUTF8(input)

        Args:
        - `input` — Input string to convert to lowercase. [`String`](/sql-reference/data-types/string)

        Returns a lowercase string. [`String`](/sql-reference/data-types/string)
        """
        return Function("lowerUTF8", *to_args(locals()))
    
    @staticmethod
    def makeDate(year: Any, month: Any, day: Any) -> Function:
        """
        makeDate(year, month, day)
        makeDate(year, day_of_year)

        Args:
        - `year` — Year number. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `month` — Month number (1-12). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `day` — Day of the month (1-31). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `day_of_year` — Day of the year (1-365). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a `Date` value constructed from the provided arguments [`Date`](/sql-reference/data-types/date)
        """
        return Function("makeDate", *to_args(locals()))
    
    @staticmethod
    def makeDate32(year: Any, month: Any, day: Any) -> Function:
        """
        makeDate32(year, month, day)
        makeDate32(year, day_of_year)

        Args:
        - `year` — Year number. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `month` — Month number (1-12). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `day` — Day of the month (1-31). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `day_of_year` — Day of the year (1-365). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a `Date32` value constructed from the provided arguments [`Date32`](/sql-reference/data-types/date32)
        """
        return Function("makeDate32", *to_args(locals()))
    
    @staticmethod
    def makeDateTime(year: Any, month: Any, day: Any, hour: Any, minute: Any, second: Any, timezone: Any | None = None) -> Function:
        """
        makeDateTime(year, month, day, hour, minute, second[, timezone])

        Args:
        - `year` — Year number. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `month` — Month number (1-12). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `day` — Day of the month (1-31). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `hour` — Hour (0-23). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `minute` — Minute (0-59). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `second` — Second (0-59). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `timezone` — Timezone name. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime` value constructed from the provided arguments [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("makeDateTime", *to_args(locals()))
    
    @staticmethod
    def makeDateTime64(year: Any, month: Any, day: Any, hour: Any, minute: Any, second: Any, fraction: Any | None = None, precision: Any | None = None, timezone: Any | None = None) -> Function:
        """
        makeDateTime64(year, month, day, hour, minute, second[, fraction[, precision[, timezone]]])

        Args:
        - `year` — Year number. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `month` — Month number (1-12). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `day` — Day of the month (1-31). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `hour` — Hour (0-23). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `minute` — Minute (0-59). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `second` — Second (0-59). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `fraction` — Fractional part of the second. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `precision` — Precision for the fractional part (0-9). [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Timezone name. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime64` value constructed from the provided arguments [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("makeDateTime64", *to_args(locals()))
    
    @staticmethod
    def mannWhitneyUTest(alternative: Any, continuity_correction: Any | None = None) -> Function:
        """
        mannWhitneyUTest[(alternative[, continuity_correction])](sample_data, sample_index)

        Args:
        - `sample_data` — Sample data. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        - `sample_index` — Sample index. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a tuple with two elements: calculated U-statistic and calculated p-value. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("mannWhitneyUTest", *to_args(locals()))
    
    @staticmethod
    def map(key1: Any, value1: Any, key2: Any | None = None, value2: Any | None = None) -> Function:
        """
        map(key1, value1[, key2, value2, ...])

        Args:
        - `key_n` — The keys of the map entries. [`Any`](/sql-reference/data-types)
        - `value_n` — The values of the map entries. [`Any`](/sql-reference/data-types)

        Returns a map containing key:value pairs. [`Map(Any, Any)`](/sql-reference/data-types/map)
        """
        return Function("map", *to_args(locals()))
    
    @staticmethod
    def mapAdd(arg1: Any, arg2: Any | None = None) -> Function:
        """
        mapAdd(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — Maps or tuples of two arrays in which items in the first array represent keys, and the second array contains values for each key. [`Map(K, V)`](/sql-reference/data-types/map) or [`Tuple(Array(T), Array(T))`](/sql-reference/data-types/tuple)

        Returns a map or returns a tuple, where the first array contains the sorted keys and the second array contains values. [`Map(K, V)`](/sql-reference/data-types/map) or [`Tuple(Array(T), Array(T))`](/sql-reference/data-types/tuple)
        """
        return Function("mapAdd", *to_args(locals()))
    
    @staticmethod
    def mapAll(func: Any | None = None, map: Any | None = None) -> Function:
        """
        mapAll([func,] map)

        Args:
        - `func` — Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `map` — Map to check. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns `1` if all key-value pairs satisfy the condition, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("mapAll", *to_args(locals()))
    
    @staticmethod
    def mapApply(func: Any, map: Any) -> Function:
        """
        mapApply(func, map)

        Args:
        - `func` — Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `map` — Map to apply function to. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns a new map obtained from the original map by application of `func` for each element. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapApply", *to_args(locals()))
    
    @staticmethod
    def mapConcat(maps: Any) -> Function:
        """
        mapConcat(maps)

        Args:
        - `maps` — Arbitrarily many maps. [`Map`](/sql-reference/data-types/map)

        Returns a map with concatenated maps passed as arguments. [`Map`](/sql-reference/data-types/map)
        """
        return Function("mapConcat", *to_args(locals()))
    
    @staticmethod
    def mapContainsKey(map: Any, key: Any) -> Function:
        """
        mapContainsKey(map, key)

        Args:
        - `map` — Map to search in. [`Map(K, V)`](/sql-reference/data-types/map)
        - `key` — Key to search for. Type must match the key type of the map. [`Any`](/sql-reference/data-types)

        Returns 1 if map contains key, 0 if not. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("mapContainsKey", *to_args(locals()))
    
    @staticmethod
    def mapContainsKeyLike(map: Any, pattern: Any) -> Function:
        """
        mapContainsKeyLike(map, pattern)

        Args:
        - `map` — Map to search in. [`Map(K, V)`](/sql-reference/data-types/map)
        - `pattern` — Pattern to match keys against. [`const String`](/sql-reference/data-types/string)

        Returns `1` if `map` contains a key matching `pattern`, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("mapContainsKeyLike", *to_args(locals()))
    
    @staticmethod
    def mapContainsValue(map: Any, value: Any) -> Function:
        """
        mapContainsValue(map, value)

        Args:
        - `map` — Map to search in. [`Map(K, V)`](/sql-reference/data-types/map)
        - `value` — Value to search for. Type must match the value type of map. [`Any`](/sql-reference/data-types)

        Returns `1` if the map contains the value, `0` if not. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("mapContainsValue", *to_args(locals()))
    
    @staticmethod
    def mapContainsValueLike(map: Any, pattern: Any) -> Function:
        """
        mapContainsValueLike(map, pattern)

        Args:
        - `map` — Map to search in. [`Map(K, V)`](/sql-reference/data-types/map)
        - `pattern` — Pattern to match values against. [`const String`](/sql-reference/data-types/string)

        Returns `1` if `map` contains a value matching `pattern`, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("mapContainsValueLike", *to_args(locals()))
    
    @staticmethod
    def mapExists(func: Any | None = None, map: Any | None = None) -> Function:
        """
        mapExists([func,] map)

        Args:
        - `func` — Optional. Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `map` — Map to check. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns `1` if at least one key-value pair satisfies the condition, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("mapExists", *to_args(locals()))
    
    @staticmethod
    def mapExtractKeyLike(map: Any, pattern: Any) -> Function:
        """
        mapExtractKeyLike(map, pattern)

        Args:
        - `map` — Map to extract from. [`Map(K, V)`](/sql-reference/data-types/map)
        - `pattern` — Pattern to match keys against. [`const String`](/sql-reference/data-types/string)

        Returns a map containing elements the key matching the specified pattern. If no elements match the pattern, an empty map is returned. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapExtractKeyLike", *to_args(locals()))
    
    @staticmethod
    def mapExtractValueLike(map: Any, pattern: Any) -> Function:
        """
        mapExtractValueLike(map, pattern)

        Args:
        - `map` — Map to extract from. [`Map(K, V)`](/sql-reference/data-types/map)
        - `pattern` — Pattern to match values against. [`const String`](/sql-reference/data-types/string)

        Returns a map containing elements the value matching the specified pattern. If no elements match the pattern, an empty map is returned. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapExtractValueLike", *to_args(locals()))
    
    @staticmethod
    def mapFilter(func: Any, map: Any) -> Function:
        """
        mapFilter(func, map)

        Args:
        - `func` — Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `map` — Map to filter. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns a map containing only the elements in the map for which `func` returns something other than `0`. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapFilter", *to_args(locals()))
    
    @staticmethod
    def mapFromArrays(keys: Any, values: Any) -> Function:
        """
        mapFromArrays(keys, values)

        Args:
        - `keys` — Array or map of keys to create the map from. [`Array`](/sql-reference/data-types/array) or [`Map`](/sql-reference/data-types/map)
        - `values` — Array or map of values to create the map from. [`Array`](/sql-reference/data-types/array) or [`Map`](/sql-reference/data-types/map)

        Returns a map with keys and values constructed from the key array and value array/map. [`Map`](/sql-reference/data-types/map)
        """
        return Function("mapFromArrays", *to_args(locals()))
    
    @staticmethod
    def mapKeys(map: Any) -> Function:
        """
        mapKeys(map)

        Args:
        - `map` — Map to extract keys from. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns array containing all keys from the map. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("mapKeys", *to_args(locals()))
    
    @staticmethod
    def mapPartialReverseSort(func: Any | None = None, limit: Any | None = None, map: Any | None = None) -> Function:
        """
        mapPartialReverseSort([func,] limit, map)

        Args:
        - `func` — Optional. Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `limit` — Elements in the range `[1..limit]` are sorted. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `map` — Map to sort. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns a partially sorted map in descending order. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapPartialReverseSort", *to_args(locals()))
    
    @staticmethod
    def mapPartialSort(func: Any | None = None, limit: Any | None = None, map: Any | None = None) -> Function:
        """
        mapPartialSort([func,] limit, map)

        Args:
        - `func` — Optional. Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `limit` — Elements in the range `[1..limit]` are sorted. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `map` — Map to sort. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns a partially sorted map. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapPartialSort", *to_args(locals()))
    
    @staticmethod
    def mapPopulateSeries(map: Any, max: Any | None = None) -> Function:
        """
        mapPopulateSeries(map[, max]) | mapPopulateSeries(keys, values[, max])

        Args:
        - `map` — Map with integer keys. [`Map((U)Int*, V)`](/sql-reference/data-types/map)
        - `keys` — Array of keys. [`Array(T)`](/sql-reference/data-types/array)
        - `values` — Array of values. [`Array(T)`](/sql-reference/data-types/array)
        - `max` — Optional. Maximum key value. [`Int8`](/sql-reference/data-types/int-uint) or [`Int16`](/sql-reference/data-types/int-uint) or [`Int32`](/sql-reference/data-types/int-uint) or [`Int64`](/sql-reference/data-types/int-uint) or [`Int128`](/sql-reference/data-types/int-uint) or [`Int256`](/sql-reference/data-types/int-uint)

        Returns a map or a tuple of two arrays where the first has keys in sorted order, and the second values for the corresponding keys. [`Map(K, V)`](/sql-reference/data-types/map) or [`Tuple(Array(UInt*), Array(Any))`](/sql-reference/data-types/tuple)
        """
        return Function("mapPopulateSeries", *to_args(locals()))
    
    @staticmethod
    def mapReverseSort(func: Any | None = None, map: Any | None = None) -> Function:
        """
        mapReverseSort([func,] map)

        Args:
        - `func` — Optional. Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `map` — Map to sort. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns a map sorted in descending order. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapReverseSort", *to_args(locals()))
    
    @staticmethod
    def mapSort(func: Any | None = None, map: Any | None = None) -> Function:
        """
        mapSort([func,] map)

        Args:
        - `func` — Optional. Lambda function. [`Lambda function`](/sql-reference/functions/overview#arrow-operator-and-lambda)
        - `map` — Map to sort. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns a map sorted in ascending order. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapSort", *to_args(locals()))
    
    @staticmethod
    def mapSubtract(arg1: Any, arg2: Any | None = None) -> Function:
        """
        mapSubtract(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — Maps or tuples of two arrays in which items in the first array represent keys, and the second array contains values for each key. [`Map(K, V)`](/sql-reference/data-types/map) or [`Tuple(Array(T), Array(T))`](/sql-reference/data-types/tuple)

        Returns one map or tuple, where the first array contains the sorted keys and the second array contains values. [`Map(K, V)`](/sql-reference/data-types/map) or [`Tuple(Array(T), Array(T))`](/sql-reference/data-types/tuple)
        """
        return Function("mapSubtract", *to_args(locals()))
    
    @staticmethod
    def mapUpdate(map1: Any, map2: Any) -> Function:
        """
        mapUpdate(map1, map2)

        Args:
        - `map1` — The map to update. [`Map(K, V)`](/sql-reference/data-types/map)
        - `map2` — The map to use for updating. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns `map1` with values updated from values for the corresponding keys in `map2`. [`Map(K, V)`](/sql-reference/data-types/map)
        """
        return Function("mapUpdate", *to_args(locals()))
    
    @staticmethod
    def mapValues(map: Any) -> Function:
        """
        mapValues(map)

        Args:
        - `map` — Map to extract values from. [`Map(K, V)`](/sql-reference/data-types/map)

        Returns an array containing all the values from the map. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("mapValues", *to_args(locals()))
    
    @staticmethod
    def match(haystack: Any, pattern: Any) -> Function:
        """
        match(haystack, pattern)

        Args:
        - `haystack` — String in which the pattern is searched. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expression pattern. [`const String`](/sql-reference/data-types/string)

        Returns `1` if the pattern matches, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("match", *to_args(locals()))
    
    @staticmethod
    def materialize(x: Any) -> Function:
        """
        materialize(x)

        Args:
        - `x` — A constant. [`Any`](/sql-reference/data-types)

        Returns a full column containing the constant value. [`Any`](/sql-reference/data-types)
        """
        return Function("materialize", *to_args(locals()))
    
    @staticmethod
    def max(column: Any) -> Function:
        """
        max(column)

        Args:
        - `column` — Column name or expression. [`Any`](/sql-reference/data-types)

        The maximum value across the group with type equal to that of the input. [`Any`](/sql-reference/data-types)
        """
        return Function("max", *to_args(locals()))
    
    @staticmethod
    def max2(x: Any, y: Any) -> Function:
        """
        max2(x, y)

        Args:
        - `x` — First value [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second value [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the bigger value of `x` and `y`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("max2", *to_args(locals()))
    
    @staticmethod
    def maxIntersections(start_column: Any, end_column: Any) -> Function:
        """
        maxIntersections(start_column, end_column)

        Args:
        - `start_column` — A numeric column that represents the start of each interval. If `start_column` is `NULL` or 0 then the interval will be skipped. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `end_column` — A numeric column that represents the end of each interval. If `end_column` is `NULL` or 0 then the interval will be skipped. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the maximum number of intersected intervals. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("maxIntersections", *to_args(locals()))
    
    @staticmethod
    def maxIntersectionsPosition(start_column: Any, end_column: Any) -> Function:
        """
        maxIntersectionsPosition(start_column, end_column)

        Args:
        - `start_column` — A numeric column that represents the start of each interval. If `start_column` is `NULL` or 0 then the interval will be skipped. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `end_column` — A numeric column that represents the end of each interval. If `end_column` is `NULL` or 0 then the interval will be skipped. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the start positions of the maximum number of intersected intervals. [`Any`](/sql-reference/data-types)
        """
        return Function("maxIntersectionsPosition", *to_args(locals()))
    
    @staticmethod
    def maxMappedArrays(key: Any, value: Any) -> Function:
        """
        maxMappedArrays(key, value)
        maxMappedArrays(Tuple(key, value))

        Args:
        - `key` — Array of keys. [`Array(T)`](/sql-reference/data-types/array)
        - `value` — Array of values. [`Array(T)`](/sql-reference/data-types/array)

        Returns a tuple of two arrays: keys in sorted order, and values calculated for the corresponding keys. [`Tuple(Array(T), Array(T))`](/sql-reference/data-types/tuple)
        """
        return Function("maxMappedArrays", *to_args(locals()))
    
    @staticmethod
    def meanZTest(population_variance_x: Any, population_variance_y: Any, confidence_level: Any) -> Function:
        """
        meanZTest(population_variance_x, population_variance_y, confidence_level)(sample_data, sample_index)

        Args:
        - `sample_data` — Sample data. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `sample_index` — Sample index. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a tuple with four elements: calculated z-statistic, calculated p-value, calculated confidence-interval-low, calculated confidence-interval-high. [`Tuple(Float64, Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("meanZTest", *to_args(locals()))
    
    @staticmethod
    def mergeTreePartInfo(part_name: Any) -> Function:
        """
        mergeTreePartInfo(part_name)

        Args:
        - `part_name` — Name of part to unpack. [`String`](/sql-reference/data-types/string)

        Returns a Tuple with subcolumns: `partition_id`, `min_block`, `max_block`, `level`, `mutation`. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("mergeTreePartInfo", *to_args(locals()))
    
    @staticmethod
    def metroHash64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        metroHash64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("metroHash64", *to_args(locals()))
    
    @staticmethod
    def midpoint(x1: Any, x2: Any | None = None) -> Function:
        """
        midpoint(x1[, x2, ...])

        Args:
        - `x1[, x2, ...]` — Accepts a single value or multiple values for averaging. 
        Returns the average value of the provided arguments, promoted to the largest compatible type.
        """
        return Function("midpoint", *to_args(locals()))
    
    @staticmethod
    def min(column: Any) -> Function:
        """
        min(column)

        Args:
        - `column` — Column name or expression. [`Any`](/sql-reference/data-types)

        Returns the minimum value across the group with type equal to that of the input. [`Any`](/sql-reference/data-types)
        """
        return Function("min", *to_args(locals()))
    
    @staticmethod
    def min2(x: Any, y: Any) -> Function:
        """
        min2(x, y)

        Args:
        - `x` — First value [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — Second value [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the smaller value of `x` and `y`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("min2", *to_args(locals()))
    
    @staticmethod
    def minMappedArrays(key: Any, value: Any) -> Function:
        """
        minMappedArrays(key, value)
        minMappedArrays(Tuple(key, value))

        Args:
        - `key` — Array of keys. [`Array(T)`](/sql-reference/data-types/array)
        - `value` — Array of values. [`Array(T)`](/sql-reference/data-types/array)

        Returns a tuple of two arrays: keys in sorted order, and values calculated for the corresponding keys. [`Tuple(Array(T), Array(T))`](/sql-reference/data-types/tuple)
        """
        return Function("minMappedArrays", *to_args(locals()))
    
    @staticmethod
    def minSampleSizeContinuous(baseline: Any, sigma: Any, mde: Any, power: Any, alpha: Any) -> Function:
        """
        minSampleSizeContinuous(baseline, sigma, mde, power, alpha)

        Args:
        - `baseline` — Baseline value of a metric. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `sigma` — Baseline standard deviation of a metric. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `mde` — Minimum detectable effect (MDE) as percentage of the baseline value (e.g. for a baseline value 112.25 the MDE 0.03 means an expected change to 112.25 ± 112.25*0.03). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `power` — Required statistical power of a test (1 - probability of Type II error). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `alpha` — Required significance level of a test (probability of Type I error). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns a named Tuple with 3 elements: `minimum_sample_size`, `detect_range_lower` and  `detect_range_upper`. These are respectively: the required sample size, the lower bound of the range of values not detectable with the returned required sample size, calculated as `baseline * (1 - mde)`, and the upper bound of the range of values not detectable with the returned required sample size, calculated as `baseline * (1 + mde)` (Float64). [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("minSampleSizeContinuous", *to_args(locals()))
    
    @staticmethod
    def minSampleSizeConversion(baseline: Any, mde: Any, power: Any, alpha: Any) -> Function:
        """
        minSampleSizeConversion(baseline, mde, power, alpha)

        Args:
        - `baseline` — Baseline conversion. [`Float*`](/sql-reference/data-types/float)
        - `mde` — Minimum detectable effect (MDE) as percentage points (e.g. for a baseline conversion 0.25 the MDE 0.03 means an expected change to 0.25 ± 0.03). [`Float*`](/sql-reference/data-types/float)
        - `power` — Required statistical power of a test (1 - probability of Type II error). [`Float*`](/sql-reference/data-types/float)
        - `alpha` — Required significance level of a test (probability of Type I error). [`Float*`](/sql-reference/data-types/float)

        Returns a named Tuple with 3 elements: `minimum_sample_size`, `detect_range_lower`, `detect_range_upper`. These are, respectively: the required sample size, the lower bound of the range of values not detectable with the returned required sample size, calculated as `baseline - mde`, the upper bound of the range of values not detectable with the returned required sample size, calculated as `baseline + mde`. [`Tuple(Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("minSampleSizeConversion", *to_args(locals()))
    
    @staticmethod
    def minus(x: Any, y: Any) -> Function:
        """
        minus(x, y)

        Args:
        - `x` — Minuend. - `y` — Subtrahend. 
        x minus y
        """
        return Function("minus", *to_args(locals()))
    
    @staticmethod
    def modulo(a: Any, b: Any) -> Function:
        """
        modulo(a, b)

        Args:
        - `a` — The dividend - `b` — The divisor (modulus) 
        The remainder of a % b
        """
        return Function("modulo", *to_args(locals()))
    
    @staticmethod
    def moduloLegacy(a: Any, b: Any) -> Function:
        """
        moduloLegacy(a, b)

        Args:
        - `a` — The dividend. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `b` — The divisor. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the remainder of the division. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("moduloLegacy", *to_args(locals()))
    
    @staticmethod
    def moduloOrNull(x: Any, y: Any) -> Function:
        """
        moduloOrNull(x, y)

        Args:
        - `x` — The dividend. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `y` — The divisor (modulus). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the remainder of the division of `x` by `y`, or null when the divisor is zero.
        """
        return Function("moduloOrNull", *to_args(locals()))
    
    @staticmethod
    def moduloOrZero(a: Any, b: Any) -> Function:
        """
        moduloOrZero(a, b)

        Args:
        - `a` — The dividend. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `b` — The divisor (modulus). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the remainder of a % b, or `0` when the divisor is `0`.
        """
        return Function("moduloOrZero", *to_args(locals()))
    
    @staticmethod
    def monthName(datetime: Any) -> Function:
        """
        monthName(datetime)

        Args:
        - `datetime` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the name of the month. [`String`](/sql-reference/data-types/string)
        """
        return Function("monthName", *to_args(locals()))
    
    @staticmethod
    def mortonDecode(tuple_size: Any, code: Any) -> Function:
        """
        -- Simple mode
        mortonDecode(tuple_size, code)

        -- Expanded mode
        mortonDecode(range_mask, code)

        Args:
        - `tuple_size` — Integer value no more than 8. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)
        - `range_mask` — For the expanded mode, the mask for each argument. The mask is a tuple of unsigned integers. Each number in the mask configures the amount of range shrink. [`Tuple(UInt8/16/32/64)`](/sql-reference/data-types/tuple)
        - `code` — UInt64 code. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple of the specified size. [`Tuple(UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("mortonDecode", *to_args(locals()))
    
    @staticmethod
    def mortonEncode(args: Any) -> Function:
        """
        -- Simplified mode
        mortonEncode(args)

        -- Expanded mode
        mortonEncode(range_mask, args)

        Args:
        - `args` — Up to 8 unsigned integers or columns of the aforementioned type. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)
        - `range_mask` — For the expanded mode, the mask for each argument. The mask is a tuple of unsigned integers from `1` - `8`. Each number in the mask configures the amount of range shrink. [`Tuple(UInt8/16/32/64)`](/sql-reference/data-types/tuple)

        Returns a `UInt64` code. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("mortonEncode", *to_args(locals()))
    
    @staticmethod
    def multiFuzzyMatchAllIndices(haystack: Any, distance: Any, pattern1: Any | None = None, pattern2: Any | None = None, patternN: Any | None = None) -> Function:
        """
        multiFuzzyMatchAllIndices(haystack, distance, [pattern1, pattern2, ..., patternN])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `distance` — The maximum edit distance for fuzzy matching. [`UInt8`](/sql-reference/data-types/int-uint)
        - `pattern` — Array of patterns to match against. [`Array(String)`](/sql-reference/data-types/array)

        Returns an array of all indices (starting from 1) that match the haystack within the specified edit distance in any order. Returns an empty array if no matches are found. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("multiFuzzyMatchAllIndices", *to_args(locals()))
    
    @staticmethod
    def multiFuzzyMatchAny(haystack: Any, distance: Any, pattern1: Any | None = None, pattern2: Any | None = None, patternN: Any | None = None) -> Function:
        """
        multiFuzzyMatchAny(haystack, distance, [pattern1, pattern2, ..., patternN])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `distance` — The maximum edit distance for fuzzy matching. [`UInt8`](/sql-reference/data-types/int-uint)
        - `pattern` — Optional. An array of patterns to match against. [`Array(String)`](/sql-reference/data-types/array)

        Returns `1` if any pattern matches the haystack within the specified edit distance, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiFuzzyMatchAny", *to_args(locals()))
    
    @staticmethod
    def multiFuzzyMatchAnyIndex(haystack: Any, distance: Any, pattern1: Any | None = None, pattern2: Any | None = None, patternn: Any | None = None) -> Function:
        """
        multiFuzzyMatchAnyIndex(haystack, distance, [pattern1, pattern2, ..., patternn])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `distance` — The maximum edit distance for fuzzy matching. [`UInt8`](/sql-reference/data-types/int-uint)
        - `pattern` — Array of patterns to match against. [`Array(String)`](/sql-reference/data-types/array)

        Returns the index (starting from 1) of any pattern that matches the haystack within the specified edit distance, otherwise `0`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiFuzzyMatchAnyIndex", *to_args(locals()))
    
    @staticmethod
    def multiIf(cond_1: Any, then_1: Any, cond_2: Any, then_2: Any, else_: Any) -> Function:
        """
        multiIf(cond_1, then_1, cond_2, then_2, ..., else)

        Args:
        - `cond_N` — The N-th evaluated condition which controls if `then_N` is returned. [`UInt8`](/sql-reference/data-types/int-uint) or [`Nullable(UInt8)`](/sql-reference/data-types/nullable) or [`NULL`](/sql-reference/syntax#null)
        - `then_N` — The result of the function when `cond_N` is true. - `else` — The result of the function if none of the conditions is true. 
        Returns the result of `then_N` for matching `cond_N`, otherwise returns the `else` condition.
        """
        return Function("multiIf", *to_args(locals()))
    
    @staticmethod
    def multiMatchAllIndices(haystack: Any, pattern1: Any | None = None, pattern2: Any | None = None, patternn: Any | None = None) -> Function:
        """
        multiMatchAllIndices(haystack, [pattern1, pattern2, ..., patternn])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expressions to match against. [`String`](/sql-reference/data-types/string)

        Array of all indices (starting from 1) that match the haystack in any order. Returns an empty array if no matches are found. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("multiMatchAllIndices", *to_args(locals()))
    
    @staticmethod
    def multiMatchAny(haystack: Any, pattern1: Any, pattern2: Any | None = None) -> Function:
        """
        multiMatchAny(haystack, pattern1[, pattern2, ...])

        Args:
        - `haystack` — String in which patterns are searched. [`String`](/sql-reference/data-types/string)
        - `pattern1[, pattern2, ...]` — An array of one or more regular expression patterns. [`Array(String)`](/sql-reference/data-types/array)

        Returns `1` if any pattern matches, `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiMatchAny", *to_args(locals()))
    
    @staticmethod
    def multiMatchAnyIndex(haystack: Any, pattern1: Any | None = None, pattern2: Any | None = None, patternn: Any | None = None) -> Function:
        """
        multiMatchAnyIndex(haystack, [pattern1, pattern2, ..., patternn])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `pattern` — Regular expressions to match against. [`Array(String)`](/sql-reference/data-types/array)

        Returns the index (starting from 1) of the first pattern that matches, or 0 if no match is found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiMatchAnyIndex", *to_args(locals()))
    
    @staticmethod
    def multiSearchAllPositions(haystack: Any, needle1: Any, needle2: Any | None = None) -> Function:
        """
        multiSearchAllPositions(haystack, needle1[, needle2, ...])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle1[, needle2, ...]` — An array of one or more substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns array of the starting position in bytes and counting from 1, if the substring was found, `0`, if the substring was not found. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("multiSearchAllPositions", *to_args(locals()))
    
    @staticmethod
    def multiSearchAllPositionsCaseInsensitive(haystack: Any, needle1: Any, needle2: Any | None = None) -> Function:
        """
        multiSearchAllPositionsCaseInsensitive(haystack, needle1[, needle2, ...])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle1[, needle2, ...]` — An array of one or more substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns array of the starting position in bytes and counting from 1 (if the substring was found), `0` if the substring was not found. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("multiSearchAllPositionsCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def multiSearchAllPositionsCaseInsensitiveUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchAllPositionsCaseInsensitiveUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — UTF-8 encoded string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — UTF-8 encoded substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Array of the starting position in bytes and counting from 1 (if the substring was found). Returns 0 if the substring was not found. [`Array`](/sql-reference/data-types/array)
        """
        return Function("multiSearchAllPositionsCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchAllPositionsUTF8(haystack: Any, needle1: Any, needle2: Any | None = None) -> Function:
        """
        multiSearchAllPositionsUTF8(haystack, needle1[, needle2, ...])

        Args:
        - `haystack` — UTF-8 encoded string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle1[, needle2, ...]` — An array of UTF-8 encoded substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns array of the starting position in bytes and counting from 1 (if the substring was found), `0` if the substring was not found. [`Array`](/sql-reference/data-types/array)
        """
        return Function("multiSearchAllPositionsUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchAny(haystack: Any, needle1: Any, needle2: Any | None = None) -> Function:
        """
        multiSearchAny(haystack, needle1[, needle2, ...])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle1[, needle2, ...]` — An array of substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns `1`, if there was at least one match, otherwise `0`, if there was not at least one match. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchAny", *to_args(locals()))
    
    @staticmethod
    def multiSearchAnyCaseInsensitive(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchAnyCaseInsensitive(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns `1`, if there was at least one case-insensitive match, otherwise `0`, if there was not at least one case-insensitive match. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchAnyCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def multiSearchAnyCaseInsensitiveUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchAnyCaseInsensitiveUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — UTF-8 string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — UTF-8 substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns `1`, if there was at least one case-insensitive match, otherwise `0`, if there was not at least one case-insensitive match. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchAnyCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchAnyUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchAnyUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — UTF-8 string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — UTF-8 substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns `1`, if there was at least one match, otherwise `0`, if there was not at least one match. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchAnyUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstIndex(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchFirstIndex(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — The string to search in. [`String`](/sql-reference/data-types/string)
        - `needles` — Array of strings to search for. [`Array(String)`](/sql-reference/data-types/array)

        Returns the 1-based index (position in the needles array) of the first needle found in the haystack. Returns 0 if no needles are found. The search is case-sensitive. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstIndex", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstIndexCaseInsensitive() -> Function:
        """
        multiSearchFirstIndexCaseInsensitive(haystack, [needle1, needle2, ..., needleN]

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns the index (starting from 1) of the leftmost found needle. Otherwise `0`, if there was no match. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstIndexCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstIndexCaseInsensitiveUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchFirstIndexCaseInsensitiveUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — The string to search in. [`String`](/sql-reference/data-types/string)
        - `needles` — Array of strings to search for. [`Array(String)`](/sql-reference/data-types/array)

        Returns the 1-based index (position in the needles array) of the first needle found in the haystack. Returns 0 if no needles are found. The search is case-insensitive and respects UTF-8 character encoding. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstIndexCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstIndexUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchFirstIndexUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — UTF-8 string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Array of UTF-8 substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns the index (starting from 1) of the leftmost found needle. Otherwise 0, if there was no match. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstIndexUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstPosition(haystack: Any, needle1: Any, needle2: Any | None = None) -> Function:
        """
        multiSearchFirstPosition(haystack, needle1[, needle2, ...])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle1[, needle2, ...]` — An array of one or more substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns the leftmost offset in a `haystack` string which matches any of multiple `needle` strings, otherwise `0`, if there was no match. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstPosition", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstPositionCaseInsensitive(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchFirstPositionCaseInsensitive(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Array of substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns the leftmost offset in a `haystack` string which matches any of multiple `needle` strings. Returns `0`, if there was no match. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstPositionCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstPositionCaseInsensitiveUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchFirstPositionCaseInsensitiveUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — UTF-8 string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Array of UTF-8 substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Returns the leftmost offset in a `haystack` string which matches any of multiple `needle` strings, ignoring case. Returns `0`, if there was no match. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstPositionCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def multiSearchFirstPositionUTF8(haystack: Any, needle1: Any | None = None, needle2: Any | None = None, needleN: Any | None = None) -> Function:
        """
        multiSearchFirstPositionUTF8(haystack, [needle1, needle2, ..., needleN])

        Args:
        - `haystack` — UTF-8 string in which the search is performed. [`String`](/sql-reference/data-types/string)
        - `needle` — Array of UTF-8 substrings to be searched. [`Array(String)`](/sql-reference/data-types/array)

        Leftmost offset in a `haystack` string which matches any of multiple `needle` strings. Returns `0`, if there was no match. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("multiSearchFirstPositionUTF8", *to_args(locals()))
    
    @staticmethod
    def multiply(x: Any, y: Any) -> Function:
        """
        multiply(x, y)

        Args:
        - `x` — factor. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — factor. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the product of x and y
        """
        return Function("multiply", *to_args(locals()))
    
    @staticmethod
    def multiplyDecimal(a: Any, b: Any, result_scale: Any | None = None) -> Function:
        """
        multiplyDecimal(a, b[, result_scale])

        Args:
        - `a` — First value. [`Decimal`](/sql-reference/data-types/decimal)
        - `b` — Second value. [`Decimal`](/sql-reference/data-types/decimal)
        - `result_scale` — Scale of result. [`(U)Int*`](/sql-reference/data-types/int-uint)

        The result of multiplication with the given scale. Type: [`Decimal256`](/sql-reference/data-types/decimal)
        """
        return Function("multiplyDecimal", *to_args(locals()))
    
    @staticmethod
    def murmurHash2_32(arg1: Any, arg2: Any | None = None) -> Function:
        """
        murmurHash2_32(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash value of the input arguments. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("murmurHash2_32", *to_args(locals()))
    
    @staticmethod
    def murmurHash2_64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        murmurHash2_64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("murmurHash2_64", *to_args(locals()))
    
    @staticmethod
    def murmurHash3_128(arg1: Any, arg2: Any | None = None) -> Function:
        """
        murmurHash3_128(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed 128-bit `MurmurHash3` hash value of the input arguments. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("murmurHash3_128", *to_args(locals()))
    
    @staticmethod
    def murmurHash3_32(arg1: Any, arg2: Any | None = None) -> Function:
        """
        murmurHash3_32(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash value of the input arguments. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("murmurHash3_32", *to_args(locals()))
    
    @staticmethod
    def murmurHash3_64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        murmurHash3_64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed hash value of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("murmurHash3_64", *to_args(locals()))
    
    @staticmethod
    def naiveBayesClassifier(model_name: Any, input_text: Any) -> Function:
        """
        naiveBayesClassifier(model_name, input_text)

        Args:
        - `model_name` — Name of the pre-configured model. The model must be defined in ClickHouse's configuration files. [`String`](/sql-reference/data-types/string)
        - `input_text` — Text to classify. Input is processed exactly as provided (case/punctuation preserved). [`String`](/sql-reference/data-types/string)

        Predicted class ID as an unsigned integer. Class IDs correspond to categories defined during model construction. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("naiveBayesClassifier", *to_args(locals()))
    
    @staticmethod
    def naturalSortKey(s: Any) -> Function:
        """
        naturalSortKey(s)

        Args:
        - `s` — A string to convert to natural sort key. [`String`](/sql-reference/data-types/string)

        Returns a natural sort key string from `s`. [`String`](/sql-reference/data-types/string)
        """
        return Function("naturalSortKey", *to_args(locals()))
    
    @staticmethod
    def negate(x: Any) -> Function:
        """
        negate(x)

        Args:
        - `x` — The value to negate. 
        Returns -x from x
        """
        return Function("negate", *to_args(locals()))
    
    @staticmethod
    def neighbor(column: Any, offset: Any, default_value: Any | None = None) -> Function:
        """
        neighbor(column, offset[, default_value])

        Args:
        - `column` — The source column. [`Any`](/sql-reference/data-types)
        - `offset` — The offset from the current row. Positive values look forward, negative values look backward. [`Integer`](/sql-reference/data-types/int-uint)
        - `default_value` — Optional. The value to return if the offset goes beyond the data bounds. If not specified, uses the default value for the column type. [`Any`](/sql-reference/data-types)

        Returns a value from the specified offset, or default if out of bounds. [`Any`](/sql-reference/data-types)
        """
        return Function("neighbor", *to_args(locals()))
    
    @staticmethod
    def nested(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("nested", *to_args(locals()))
    
    @staticmethod
    def netloc(url: Any) -> Function:
        """
        netloc(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns `username:password@host:port` from a given URL. [`String`](/sql-reference/data-types/string)
        """
        return Function("netloc", *to_args(locals()))
    
    @staticmethod
    def ngramDistance(haystack: Any, needle: Any) -> Function:
        """
        ngramDistance(haystack, needle)

        Args:
        - `haystack` — String for comparison. [`String`](/sql-reference/data-types/string)
        - `needle` — String for comparison. [`String`](/sql-reference/data-types/string)

        Returns a Float32 number between `0` and `1`. The smaller the returned value, the more similar the strings are. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("ngramDistance", *to_args(locals()))
    
    @staticmethod
    def ngramDistanceCaseInsensitive(haystack: Any, needle: Any) -> Function:
        """
        ngramDistanceCaseInsensitive(haystack, needle)

        Args:
        - `haystack` — First comparison string. [`String`](/sql-reference/data-types/string)
        - `needle` — Second comparison string. [`String`](/sql-reference/data-types/string)

        Returns a Float32 number between `0` and `1`. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("ngramDistanceCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def ngramDistanceCaseInsensitiveUTF8(haystack: Any, needle: Any) -> Function:
        """
        ngramDistanceCaseInsensitiveUTF8(haystack, needle)

        Args:
        - `haystack` — First UTF-8 encoded comparison string. [`String`](/sql-reference/data-types/string)
        - `needle` — Second UTF-8 encoded comparison string. [`String`](/sql-reference/data-types/string)

        Returns a Float32 number between `0` and `1`. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("ngramDistanceCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramDistanceUTF8(haystack: Any, needle: Any) -> Function:
        """
        ngramDistanceUTF8(haystack, needle)

        Args:
        - `haystack` — First UTF-8 encoded comparison string. [`String`](/sql-reference/data-types/string)
        - `needle` — Second UTF-8 encoded comparison string. [`String`](/sql-reference/data-types/string)

        Returns a Float32 number between `0` and `1`. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("ngramDistanceUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramMinHash(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHash(string[, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHash", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashArg(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashArg(string[, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` n-grams each. [`Tuple(String)`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashArg", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashArgCaseInsensitive(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashArgCaseInsensitive(string[, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` n-grams each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashArgCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashArgCaseInsensitiveUTF8(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashArgCaseInsensitiveUTF8(string[, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` n-grams each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashArgCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashArgUTF8(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashArgUTF8(string[, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` n-grams each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashArgUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashCaseInsensitive(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashCaseInsensitive(string[, ngramsize, hashnum])

        Args:
        - `string` — String. [String](../data-types/string.md). - `ngramsize` — The size of an n-gram. Optional. Possible values: any number from `1` to `25`. Default value: `3`. [UInt8](../data-types/int-uint.md). - `hashnum` — The number of minimum and maximum hashes used to calculate the result. Optional. Possible values: any number from `1` to `25`. Default value: `6`. [UInt8](../data-types/int-uint.md). 
        Tuple with two hashes — the minimum and the maximum. [Tuple](../data-types/tuple.md)([UInt64](../data-types/int-uint.md), [UInt64](../data-types/int-uint.md)). [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashCaseInsensitiveUTF8(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashCaseInsensitiveUTF8(string [, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramMinHashUTF8(string: Any, ngramsize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        ngramMinHashUTF8(string[, ngramsize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("ngramMinHashUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramSearch(haystack: Any, needle: Any) -> Function:
        """
        ngramSearch(haystack, needle)

        Args:
        - `haystack` — String for comparison. [`String`](/sql-reference/data-types/string)
        - `needle` — String for comparison. [`String`](/sql-reference/data-types/string)

        Returns `1` if the 4-gram distance between the strings is less than or equal to a threshold (`1.0` by default), `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSearch", *to_args(locals()))
    
    @staticmethod
    def ngramSearchCaseInsensitive(haystack: Any, needle: Any) -> Function:
        """
        ngramSearchCaseInsensitive(haystack, needle)

        Args:
        - `haystack` — String for comparison. [`String`](/sql-reference/data-types/string)
        - `needle` — String for comparison. [`String`](/sql-reference/data-types/string)

        Returns `1` if the 4-gram distance between the strings is less than or equal to a threshold (`1.0` by default), `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSearchCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def ngramSearchCaseInsensitiveUTF8(haystack: Any, needle: Any) -> Function:
        """
        ngramSearchCaseInsensitiveUTF8(haystack, needle)

        Args:
        - `haystack` — UTF-8 string for comparison. [`String`](/sql-reference/data-types/string)
        - `needle` — UTF-8 string for comparison. [`String`](/sql-reference/data-types/string)

        Returns `1` if the 3-gram distance between the strings is less than or equal to a threshold (`1.0` by default), `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSearchCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramSearchUTF8(haystack: Any, needle: Any) -> Function:
        """
        ngramSearchUTF8(haystack, needle)

        Args:
        - `haystack` — UTF-8 string for comparison. [`String`](/sql-reference/data-types/string)
        - `needle` — UTF-8 string for comparison. [`String`](/sql-reference/data-types/string)

        Returns `1` if the 3-gram distance between the strings is less than or equal to a threshold (`1.0` by default), `0` otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSearchUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramSimHash(string: Any, ngramsize: Any | None = None) -> Function:
        """
        ngramSimHash(string[, ngramsize])

        Args:
        - `string` — String for which to compute the case sensitive `simhash`. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is`3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash of the input string. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSimHash", *to_args(locals()))
    
    @staticmethod
    def ngramSimHashCaseInsensitive(string: Any, ngramsize: Any | None = None) -> Function:
        """
        ngramSimHashCaseInsensitive(string[, ngramsize])

        Args:
        - `string` — String for which to compute the case insensitive `simhash`. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Hash value. [UInt64](../data-types/int-uint.md). [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSimHashCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def ngramSimHashCaseInsensitiveUTF8(string: Any, ngramsize: Any | None = None) -> Function:
        """
        ngramSimHashCaseInsensitiveUTF8(string[, ngramsize])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSimHashCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def ngramSimHashUTF8(string: Any, ngramsize: Any | None = None) -> Function:
        """
        ngramSimHashUTF8(string[, ngramsize])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `ngramsize` — Optional. The size of an n-gram, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("ngramSimHashUTF8", *to_args(locals()))
    
    @staticmethod
    def ngrams(s: Any, N: Any) -> Function:
        """
        ngrams(s, N)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `N` — The n-gram length. [`const UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns an array with n-grams. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("ngrams", *to_args(locals()))
    
    @staticmethod
    def nonNegativeDerivative(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("nonNegativeDerivative", *to_args(locals()))
    
    @staticmethod
    def normalizeQuery(x: Any) -> Function:
        """
        normalizeQuery(x)

        Args:
        - `x` — Sequence of characters. [`String`](/sql-reference/data-types/string)

        Returns the given sequence of characters with placeholders. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeQuery", *to_args(locals()))
    
    @staticmethod
    def normalizeQueryKeepNames(x: Any) -> Function:
        """
        normalizeQueryKeepNames(x)

        Args:
        - `x` — Sequence of characters. [`String`](/sql-reference/data-types/string)

        Returns the given sequence of characters with placeholders. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeQueryKeepNames", *to_args(locals()))
    
    @staticmethod
    def normalizeUTF8NFC(str: Any) -> Function:
        """
        normalizeUTF8NFC(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        Returns the NFC normalized form of the UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeUTF8NFC", *to_args(locals()))
    
    @staticmethod
    def normalizeUTF8NFD(str: Any) -> Function:
        """
        normalizeUTF8NFD(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        Returns the NFD normalized form of the UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeUTF8NFD", *to_args(locals()))
    
    @staticmethod
    def normalizeUTF8NFKC(str: Any) -> Function:
        """
        normalizeUTF8NFKC(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        Returns the NFKC normalized form of the UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeUTF8NFKC", *to_args(locals()))
    
    @staticmethod
    def normalizeUTF8NFKCCasefold(str: Any) -> Function:
        """
        normalizeUTF8NFKCCasefold(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        Returns the NFKC_Casefold normalized form of the UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeUTF8NFKCCasefold", *to_args(locals()))
    
    @staticmethod
    def normalizeUTF8NFKD(str: Any) -> Function:
        """
        normalizeUTF8NFKD(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        Returns the NFKD normalized form of the UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("normalizeUTF8NFKD", *to_args(locals()))
    
    @staticmethod
    def normalizedQueryHash(x: Any) -> Function:
        """
        normalizedQueryHash(x)

        Args:
        - `x` — Sequence of characters. [`String`](/sql-reference/data-types/string)

        Returns a 64 bit hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("normalizedQueryHash", *to_args(locals()))
    
    @staticmethod
    def normalizedQueryHashKeepNames(x: Any) -> Function:
        """
        normalizedQueryHashKeepNames(x)

        Args:
        - `x` — Sequence of characters. [`String`](/sql-reference/data-types/string)

        Returns a 64 bit hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("normalizedQueryHashKeepNames", *to_args(locals()))
    
    @staticmethod
    def not_(val: Any) -> Function:
        """
        not(val)

        Args:
        - `val` — The value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns:
        - `1`, if `val` evaluates to `false`
        - `0`, if `val` evaluates to `true`
        - `NULL`, if `val` is `NULL`.
                 [`Nullable(UInt8)`](/sql-reference/data-types/nullable)
        """
        return Function("not", *to_args(locals()))
    
    @staticmethod
    def notEmpty(arr: Any) -> Function:
        """
        notEmpty(arr)

        Args:
        - `arr` — Input array. [`Array(T)`](/sql-reference/data-types/array)

        Returns `1` for a non-empty array or `0` for an empty array [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notEmpty", *to_args(locals()))
    
    @staticmethod
    def notEquals(a: Any, b: Any) -> Function:
        """
        notEquals(a, b)
            -- a != b
            -- a <> b

        Args:
        - `a` — First value.<sup>[*](#comparison-rules)</sup> - `b` — Second value.<sup>[*](#comparison-rules)</sup> 
        Returns `1` if `a` is not equal to `b`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notEquals", *to_args(locals()))
    
    @staticmethod
    def notILike(haystack: Any, pattern: Any) -> Function:
        """
        notILike(haystack, pattern)

        Args:
        - `haystack` — The input string to search in. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `pattern` — The SQL LIKE pattern to match against. `%` matches any number of characters (including zero), `_` matches exactly one character. [`String`](/sql-reference/data-types/string)

        Returns `1` if the string does not match the pattern (case-insensitive), otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notILike", *to_args(locals()))
    
    @staticmethod
    def notIn(x: Any, set: Any) -> Function:
        """
        notIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notIn", *to_args(locals()))
    
    @staticmethod
    def notInIgnoreSet(x: Any, set: Any) -> Function:
        """
        notIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def notLike(haystack: Any, pattern: Any) -> Function:
        """
        notLike(haystack, pattern)
        -- haystack NOT LIKE pattern

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `pattern` — LIKE pattern to match against. [`String`](/sql-reference/data-types/string)

        Returns `1` if the string does not match the `LIKE` pattern, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notLike", *to_args(locals()))
    
    @staticmethod
    def notNullIn(x: Any, set: Any) -> Function:
        """
        notNullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notNullIn", *to_args(locals()))
    
    @staticmethod
    def notNullInIgnoreSet(x: Any, set: Any) -> Function:
        """
        notNullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is not in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("notNullInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def nothing(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("nothing", *to_args(locals()))
    
    @staticmethod
    def nothingNull(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("nothingNull", *to_args(locals()))
    
    @staticmethod
    def nothingUInt64(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("nothingUInt64", *to_args(locals()))
    
    @staticmethod
    def now(timezone: Any | None = None) -> Function:
        """
        now([timezone])

        Args:
        - `timezone` — Optional. Timezone name for the returned value. [`String`](/sql-reference/data-types/string)

        Returns the current date and time. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("now", *to_args(locals()))
    
    @staticmethod
    def now64(scale: Any | None = None, timezone: Any | None = None) -> Function:
        """
        now64([scale[, timezone]])

        Args:
        - `scale` — Optional. Tick size (precision): 10^-precision seconds. Valid range: [0 : 9]. Typically, are used - 3 (default) (milliseconds), 6 (microseconds), 9 (nanoseconds). [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name for the returned value. [`String`](/sql-reference/data-types/string)

        Returns current date and time with sub-second precision. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("now64", *to_args(locals()))
    
    @staticmethod
    def nowInBlock(timezone: Any | None = None) -> Function:
        """
        nowInBlock([timezone])

        Args:
        - `timezone` — Optional. Timezone name for the returned value. [`String`](/sql-reference/data-types/string)

        Returns the current date and time at the moment of processing of each block of data. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("nowInBlock", *to_args(locals()))
    
    @staticmethod
    def nowInBlock64(scale: Any | None = None, timezone: Any | None = None) -> Function:
        """
        nowInBlock64([scale[, timezone]])

        Args:
        - `scale` — Optional. Tick size (precision): 10^-precision seconds. Valid range: [0 : 9]. Typically, are used - 3 (default) (milliseconds), 6 (microseconds), 9 (nanoseconds). [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name for the returned value. [`String`](/sql-reference/data-types/string)

        Returns the current date and time at the moment of processing of each block of data with sub-second precision. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("nowInBlock64", *to_args(locals()))
    
    @staticmethod
    def nth_value(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("nth_value", *to_args(locals()))
    
    @staticmethod
    def ntile(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("ntile", *to_args(locals()))
    
    @staticmethod
    def nullIf(x: Any, y: Any) -> Function:
        """
        nullIf(x, y)

        Args:
        - `x` — The first value. [`Any`](/sql-reference/data-types)
        - `y` — The second value. [`Any`](/sql-reference/data-types)

        Returns `NULL` if both arguments are equal, otherwise returns the first argument. [`NULL`](/sql-reference/syntax#null) or [`Nullable(x)`](/sql-reference/data-types/nullable)
        """
        return Function("nullIf", *to_args(locals()))
    
    @staticmethod
    def nullIn(x: Any, set: Any) -> Function:
        """
        nullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("nullIn", *to_args(locals()))
    
    @staticmethod
    def nullInIgnoreSet(x: Any, set: Any) -> Function:
        """
        nullIn(x, set)

        Args:
        - `x` — The value to check. - `set` — The set of values. 
        Returns 1 if x is in the set, 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("nullInIgnoreSet", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorAllValueSum(v: Any) -> Function:
        """
        numericIndexedVectorAllValueSum(v)

        Args:
        - `v` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns the sum. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("numericIndexedVectorAllValueSum", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorBuild(map: Any) -> Function:
        """
        numericIndexedVectorBuild(map)

        Args:
        - `map` — A mapping from index to value. [`Map`](/sql-reference/data-types/map)

        Returns a NumericIndexedVector object. [`AggregateFunction`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("numericIndexedVectorBuild", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorCardinality(v: Any) -> Function:
        """
        numericIndexedVectorCardinality(v)

        Args:
        - `v` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns the number of unique indexes. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("numericIndexedVectorCardinality", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorGetValue(v: Any, i: Any) -> Function:
        """
        numericIndexedVectorGetValue(v, i)

        Args:
        - `v` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `i` — The index for which the value is to be retrieved. [`(U)Int*`](/sql-reference/data-types/int-uint)

        A numeric value with the same type as the value type of NumericIndexedVector. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("numericIndexedVectorGetValue", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseAdd(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseAdd(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseAdd", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseDivide(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseDivide(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseDivide", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseEqual(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseEqual(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseEqual", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseGreater(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseGreater(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseGreater", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseGreaterEqual(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseGreaterEqual(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseGreaterEqual", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseLess(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseLess(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseLess", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseLessEqual(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseLessEqual(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseLessEqual", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseMultiply(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseMultiply(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseMultiply", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseNotEqual(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseNotEqual(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseNotEqual", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorPointwiseSubtract(v1: Any, v2: Any) -> Function:
        """
        numericIndexedVectorPointwiseSubtract(v1, v2)

        Args:
        - `v1` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        - `v2` — A numeric constant or numericIndexedVector object. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a new numericIndexedVector object. [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)
        """
        return Function("numericIndexedVectorPointwiseSubtract", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorShortDebugString(v: Any) -> Function:
        """
        numericIndexedVectorShortDebugString(v)

        Args:
        - `v` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a JSON string containing debug information. [`String`](/sql-reference/data-types/string)
        """
        return Function("numericIndexedVectorShortDebugString", *to_args(locals()))
    
    @staticmethod
    def numericIndexedVectorToMap(v: Any) -> Function:
        """
        numericIndexedVectorToMap(v)

        Args:
        - `v` —  [`numericIndexedVector`](/sql-reference/functions/numeric-indexed-vector-functions#create-numeric-indexed-vector-object)

        Returns a map with index-value pairs. [`Map`](/sql-reference/data-types/map)
        """
        return Function("numericIndexedVectorToMap", *to_args(locals()))
    
    @staticmethod
    def or_(val1: Any, val2: Any) -> Function:
        """
        or(val1, val2[, ...])

        Args:
        - `val1, val2[, ...]` — List of at least two values. [`Nullable((U)Int*)`](/sql-reference/data-types/nullable) or [`Nullable(Float*)`](/sql-reference/data-types/nullable)

        Returns:
        - `1`, if at least one argument evaluates to `true`
        - `0`, if all arguments evaluate to `false`
        - `NULL`, if all arguments evaluate to `false` and at least one argument is `NULL`
                 [`Nullable(UInt8)`](/sql-reference/data-types/nullable)
        """
        return Function("or", *to_args(locals()))
    
    @staticmethod
    def overlay(s: Any, replace: Any, offset: Any, length: Any | None = None) -> Function:
        """
        overlay(s, replace, offset[, length])

        Args:
        - `s` — The input string. [`String`](/sql-reference/data-types/string)
        - `replace` — The replacement string [`const String`](/sql-reference/data-types/string)
        - `offset` — An integer type `Int` (1-based). If `offset` is negative, it is counted from the end of the string `s`. [`Int`](/sql-reference/data-types/int-uint)
        - `length` — Optional. An integer type `Int`. `length` specifies the length of the snippet within the input string `s` to be replaced. If `length` is not specified, the number of bytes removed from `s` equals the length of `replace`; otherwise `length` bytes are removed. [`Int`](/sql-reference/data-types/int-uint)

        Returns a string with replacement. [`String`](/sql-reference/data-types/string)
        """
        return Function("overlay", *to_args(locals()))
    
    @staticmethod
    def overlayUTF8(s: Any, replace: Any, offset: Any, length: Any | None = None) -> Function:
        """
        overlayUTF8(s, replace, offset[, length])

        Args:
        - `s` — The input string. [`String`](/sql-reference/data-types/string)
        - `replace` — The replacement string. [`const String`](/sql-reference/data-types/string)
        - `offset` — An integer type `Int` (1-based). If `offset` is negative, it is counted from the end of the input string `s`. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `length` — Optional. Specifies the length of the snippet within the input string `s` to be replaced. If `length` is not specified, the number of characters removed from `s` equals the length of `replace`, otherwise `length` characters are removed. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a string with replacement. [`String`](/sql-reference/data-types/string)
        """
        return Function("overlayUTF8", *to_args(locals()))
    
    @staticmethod
    def parseDateTime(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime. [`String`](/sql-reference/data-types/string)
        - `format` — Format string specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns a DateTime parsed from the input string according to the MySQL style format string. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTime", *to_args(locals()))
    
    @staticmethod
    def parseDateTime32BestEffort(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTime32BestEffort(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a `DateTime`. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTime32BestEffort", *to_args(locals()))
    
    @staticmethod
    def parseDateTime32BestEffortOrNull(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTime32BestEffortOrNull(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime` object parsed from the string, or `NULL` if the parsing fails. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTime32BestEffortOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTime32BestEffortOrZero(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTime32BestEffortOrZero(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime` object parsed from the string, or zero date (`1970-01-01 00:00:00`) if the parsing fails. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTime32BestEffortOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime64(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime64. [`String`](/sql-reference/data-types/string)
        - `format` — Format string specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns a DateTime64 parsed from the input string according to the MySQL style format string. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64BestEffort(time_string: Any, precision: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        parseDateTime64BestEffort(time_string[, precision[, time_zone]])

        Args:
        - `time_string` — String containing a date or date with time to convert. [`String`](/sql-reference/data-types/string)
        - `precision` — Optional. Required precision. `3` for milliseconds, `6` for microseconds. Default: `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. Timezone. The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns `time_string` converted to the [`DateTime64`](../../sql-reference/data-types/datetime64.md) data type. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64BestEffort", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64BestEffortOrNull(time_string: Any, precision: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        parseDateTime64BestEffortOrNull(time_string[, precision[, time_zone]])

        Args:
        - `time_string` — String containing a date or date with time to convert. [`String`](/sql-reference/data-types/string)
        - `precision` — Optional. Required precision. `3` for milliseconds, `6` for microseconds. Default: `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. Timezone. The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns `time_string` converted to [`DateTime64`](../../sql-reference/data-types/datetime64.md), or `NULL` if the input cannot be parsed. [`DateTime64`](/sql-reference/data-types/datetime64) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("parseDateTime64BestEffortOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64BestEffortOrZero(time_string: Any, precision: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        parseDateTime64BestEffortOrZero(time_string[, precision[, time_zone]])

        Args:
        - `time_string` — String containing a date or date with time to convert. [`String`](/sql-reference/data-types/string)
        - `precision` — Optional. Required precision. `3` for milliseconds, `6` for microseconds. Default: `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. Timezone. The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns `time_string` converted to [`DateTime64`](../../sql-reference/data-types/datetime64.md), or zero date/datetime (`1970-01-01 00:00:00.000`) if the input cannot be parsed. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64BestEffortOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64BestEffortUS(time_string: Any, precision: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        parseDateTime64BestEffortUS(time_string [, precision [, time_zone]])

        Args:
        - `time_string` — String containing a date or date with time to convert. [`String`](/sql-reference/data-types/string)
        - `precision` — Optional. Required precision. `3` for milliseconds, `6` for microseconds. Default: `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. Timezone. The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns `time_string` converted to [`DateTime64`](../../sql-reference/data-types/datetime64.md) using US date format preference for ambiguous cases. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64BestEffortUS", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64BestEffortUSOrNull(time_string: Any, precision: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        parseDateTime64BestEffortUSOrNull(time_string[, precision[, time_zone]])

        Args:
        - `time_string` — String containing a date or date with time to convert. [`String`](/sql-reference/data-types/string)
        - `precision` — Optional. Required precision. `3` for milliseconds, `6` for microseconds. Default: `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. Timezone. The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns `time_string` converted to [`DateTime64`](../../sql-reference/data-types/datetime64.md) using US format preference, or `NULL` if the input cannot be parsed. [`DateTime64`](/sql-reference/data-types/datetime64) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("parseDateTime64BestEffortUSOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64BestEffortUSOrZero(time_string: Any, precision: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        parseDateTime64BestEffortUSOrZero(time_string [, precision [, time_zone]])

        Args:
        - `time_string` — String containing a date or date with time to convert. [`String`](/sql-reference/data-types/string)
        - `precision` — Optional. Required precision. `3` for milliseconds, `6` for microseconds. Default: `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. Timezone. The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns `time_string` converted to [`DateTime64`](../../sql-reference/data-types/datetime64.md) using US format preference, or zero date/datetime (`1970-01-01 00:00:00.000`) if the input cannot be parsed. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64BestEffortUSOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64InJodaSyntax(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime64InJodaSyntax(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime64. [`String`](/sql-reference/data-types/string)
        - `format` — Format string in Joda syntax specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns a DateTime64 parsed from the input string according to the Joda style format string. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64InJodaSyntax", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64InJodaSyntaxOrNull(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime64InJodaSyntaxOrNull(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime64. [`String`](/sql-reference/data-types/string)
        - `format` — Format string in Joda syntax specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime64 parsed from input string, or NULL if parsing fails. [`Nullable(DateTime64)`](/sql-reference/data-types/nullable)
        """
        return Function("parseDateTime64InJodaSyntaxOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64InJodaSyntaxOrZero(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime64InJodaSyntaxOrZero(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime64. [`String`](/sql-reference/data-types/string)
        - `format` — Format string in Joda syntax specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime64 parsed from input string, or zero DateTime64 if parsing fails. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64InJodaSyntaxOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64OrNull(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime64OrNull(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime64. [`String`](/sql-reference/data-types/string)
        - `format` — Format string specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime64 parsed from input string, or NULL if parsing fails. [`Nullable(DateTime64)`](/sql-reference/data-types/nullable)
        """
        return Function("parseDateTime64OrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTime64OrZero(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTime64OrZero(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime64. [`String`](/sql-reference/data-types/string)
        - `format` — Format string specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime64 parsed from input string, or zero DateTime64 if parsing fails. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("parseDateTime64OrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeBestEffort(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTimeBestEffort(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a `DateTime`. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeBestEffort", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeBestEffortOrNull(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTimeBestEffortOrNull(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a DateTime, or `NULL` if the input cannot be parsed. [`DateTime`](/sql-reference/data-types/datetime) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("parseDateTimeBestEffortOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeBestEffortOrZero(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTimeBestEffortOrZero(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a `DateTime`, or zero date/datetime (`1970-01-01` or `1970-01-01 00:00:00`) if the input cannot be parsed. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeBestEffortOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeBestEffortUS(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTimeBestEffortUS(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a `DateTime` using US date format preference for ambiguous cases. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeBestEffortUS", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeBestEffortUSOrNull(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTimeBestEffortUSOrNull(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a DateTime using US format preference, or `NULL` if the input cannot be parsed. [`DateTime`](/sql-reference/data-types/datetime) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("parseDateTimeBestEffortUSOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeBestEffortUSOrZero(time_string: Any, time_zone: Any | None = None) -> Function:
        """
        parseDateTimeBestEffortUSOrZero(time_string[, time_zone])

        Args:
        - `time_string` — String containing a date and time to convert. [`String`](/sql-reference/data-types/string)
        - `time_zone` — Optional. Time zone according to which `time_string` is parsed. [`String`](/sql-reference/data-types/string)

        Returns `time_string` as a `DateTime` using US format preference, or zero date/datetime (`1970-01-01` or `1970-01-01 00:00:00`) if the input cannot be parsed. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeBestEffortUSOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeInJodaSyntax(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTimeInJodaSyntax(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime. [`String`](/sql-reference/data-types/string)
        - `format` — Format string in Joda syntax specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns a DateTime parsed from the input string according to the Joda style format string. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeInJodaSyntax", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeInJodaSyntaxOrNull(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTimeInJodaSyntaxOrNull(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime. [`String`](/sql-reference/data-types/string)
        - `format` — Format string in Joda syntax specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime parsed from input string, or NULL if parsing fails. [`Nullable(DateTime)`](/sql-reference/data-types/nullable)
        """
        return Function("parseDateTimeInJodaSyntaxOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeInJodaSyntaxOrZero(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTimeInJodaSyntaxOrZero(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime. [`String`](/sql-reference/data-types/string)
        - `format` — Format string in Joda syntax specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime parsed from input string, or zero DateTime if parsing fails. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeInJodaSyntaxOrZero", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeOrNull(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTimeOrNull(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime. [`String`](/sql-reference/data-types/string)
        - `format` — Format string specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime parsed from input string, or NULL if parsing fails. [`Nullable(DateTime)`](/sql-reference/data-types/nullable)
        """
        return Function("parseDateTimeOrNull", *to_args(locals()))
    
    @staticmethod
    def parseDateTimeOrZero(time_string: Any, format: Any, timezone: Any | None = None) -> Function:
        """
        parseDateTimeOrZero(time_string, format[, timezone])

        Args:
        - `time_string` — String to be parsed into DateTime. [`String`](/sql-reference/data-types/string)
        - `format` — Format string specifying how to parse time_string. [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone. [`String`](/sql-reference/data-types/string)

        Returns DateTime parsed from input string, or zero DateTime if parsing fails. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("parseDateTimeOrZero", *to_args(locals()))
    
    @staticmethod
    def parseReadableSize(x: Any) -> Function:
        """
        parseReadableSize(x)

        Args:
        - `x` — Readable size with ISO/IEC 80000-13 or decimal byte unit. [`String`](/sql-reference/data-types/string)

        Returns the number of bytes, rounded up to the nearest integer. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("parseReadableSize", *to_args(locals()))
    
    @staticmethod
    def parseReadableSizeOrNull(x: Any) -> Function:
        """
        parseReadableSizeOrNull(x)

        Args:
        - `x` — Readable size with ISO/IEC 80000-13 or decimal byte unit. [`String`](/sql-reference/data-types/string)

        Returns the number of bytes, rounded up to the nearest integer, or `NULL` if unable to parse the input [`Nullable(UInt64)`](/sql-reference/data-types/nullable)
        """
        return Function("parseReadableSizeOrNull", *to_args(locals()))
    
    @staticmethod
    def parseReadableSizeOrZero(x: Any) -> Function:
        """
        parseReadableSizeOrZero(x)

        Args:
        - `x` — Readable size with ISO/IEC 80000-13 or decimal byte unit. [`String`](/sql-reference/data-types/string)

        Returns the number of bytes, rounded up to the nearest integer, or `0` if unable to parse the input. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("parseReadableSizeOrZero", *to_args(locals()))
    
    @staticmethod
    def parseTimeDelta(timestr: Any) -> Function:
        """
        parseTimeDelta(timestr)

        Args:
        - `timestr` — A sequence of numbers followed by something resembling a time unit. [`String`](/sql-reference/data-types/string)

        The number of seconds. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("parseTimeDelta", *to_args(locals()))
    
    @staticmethod
    def partitionId(column1: Any, column2: Any | None = None) -> Function:
        """
        partitionId(column1[, column2, ...])

        Args:
        - `column1, column2, ...` — Column for which to return the partition ID. 
        Returns the partition ID that the row belongs to. [`String`](/sql-reference/data-types/string)
        """
        return Function("partitionId", *to_args(locals()))
    
    @staticmethod
    def path(url: Any) -> Function:
        """
        path(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the path of the URL without query string. [`String`](/sql-reference/data-types/string)
        """
        return Function("path", *to_args(locals()))
    
    @staticmethod
    def pathFull(url: Any) -> Function:
        """
        pathFull(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the path of the URL including query string and fragment. [`String`](/sql-reference/data-types/string)
        """
        return Function("pathFull", *to_args(locals()))
    
    @staticmethod
    def percentRank(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("percentRank", *to_args(locals()))
    
    @staticmethod
    def perimeterCartesian(object: Any) -> Function:
        """
        perimeterCartesian(object)

        Args:
        - `object` — geometry object [`Variant`](/sql-reference/data-types/variant)

        Returns the perimeter of the object. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("perimeterCartesian", *to_args(locals()))
    
    @staticmethod
    def perimeterSpherical(object: Any) -> Function:
        """
        perimeterSpherical(object)

        Args:
        - `object` — geometry object [`Variant`](/sql-reference/data-types/variant)

        Returns the perimeter of the object. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("perimeterSpherical", *to_args(locals()))
    
    @staticmethod
    def pi() -> Function:
        """
        pi()

        
        Returns pi [`Float64`](/sql-reference/data-types/float)
        """
        return Function("pi", *to_args(locals()))
    
    @staticmethod
    def plus(x: Any, y: Any) -> Function:
        """
        plus(x, y)

        Args:
        - `x` — Left hand operand. - `y` — Right hand operand. 
        Returns the sum of x and y
        """
        return Function("plus", *to_args(locals()))
    
    @staticmethod
    def pointInPolygon(x: Any, y: Any) -> Function:
        """
        pointInPolygon((x, y), [(a, b), (c, d) ...], ...)

        Args:
        - `(x, y)` — Coordinates of a point on the plane. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        - `[(a, b), (c, d) ...]` — Polygon vertices as an array of coordinate pairs. Vertices should be in clockwise or counterclockwise order. Minimum 3 vertices required. [`Array(Tuple(Float64, Float64))`](/sql-reference/data-types/array)
        - `...` — Optional. Additional arguments for polygons with holes (as separate arrays) or multipolygons (as separate polygons). [`Array(Tuple(Float64, Float64))`](/sql-reference/data-types/array) or [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)

        Returns `1` if the point is inside the polygon, `0` if it is not. If the point is on the polygon boundary, the function may return either `0` or `1`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("pointInPolygon", *to_args(locals()))
    
    @staticmethod
    def polygonAreaCartesian(polygon: Any) -> Function:
        """
        polygonAreaCartesian(polygon)

        Args:
        - `polygon` — A polygon value [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the area of the polygon [`Float64`](/sql-reference/data-types/float)
        """
        return Function("polygonAreaCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonAreaSpherical(polygon: Any) -> Function:
        """
        polygonAreaSpherical(polygon)

        Args:
        - `polygon` — A polygon value. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the surface area of the polygon [`Float64`](/sql-reference/data-types/float)
        """
        return Function("polygonAreaSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonConvexHullCartesian(multipolygon: Any) -> Function:
        """
        polygonConvexHullCartesian(multipolygon)

        Args:
        - `multipolygon` — A MultiPolygon value. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)

        Returns the convex hull as a Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        """
        return Function("polygonConvexHullCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonPerimeterCartesian(polygon: Any) -> Function:
        """
        polygonPerimeterCartesian(polygon)

        Args:
        - `polygon` — A Polygon value. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the perimeter of the polygon. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("polygonPerimeterCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonPerimeterSpherical(polygon: Any) -> Function:
        """
        polygonPerimeterSpherical(polygon)

        Args:
        - `polygon` — A value of type [`Polygon`](/sql-reference/data-types/geo#polygon) 
        The perimeter of the polygon on a sphere [`Float64`](/sql-reference/data-types/float)
        """
        return Function("polygonPerimeterSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonsDistanceCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsDistanceCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — A Polygon value [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — A Polygon value [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the minimal distance between the two polygons [`Float64`](/sql-reference/data-types/float)
        """
        return Function("polygonsDistanceCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsDistanceSpherical(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsDistanceSpherical(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon value. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon value. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the minimal distance between the two polygons on a sphere [`Float64`](/sql-reference/data-types/float)
        """
        return Function("polygonsDistanceSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonsEqualsCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsEqualsCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns `1` if equal, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("polygonsEqualsCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsIntersectCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsIntersectCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — A value of type [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon). - `polygon2` — A value of type [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon). 
        Returns true (1) if the two polygons intersect. [`Bool`](/sql-reference/data-types/boolean).
        """
        return Function("polygonsIntersectCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsIntersectSpherical(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsIntersectSpherical(polygon1, polygon2)

        Args:
        - `polygon1` — A value of type [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon). - `polygon2` — A value of type [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon). 
        Returns true (1) if the two polygons intersect (share any common area or boundary). [`Bool`](/sql-reference/data-types/boolean).
        """
        return Function("polygonsIntersectSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonsIntersectionCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsIntersectionCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the intersection of the polygons as a MultiPolygon. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("polygonsIntersectionCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsIntersectionSpherical(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsIntersectionSpherical(polygon1, polygon2)

        Args:
        - `polygon1` — First Polygon with spherical coordinates. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — Second Polygon with spherical coordinates. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the intersection of the polygons as a MultiPolygon. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("polygonsIntersectionSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonsSymDifferenceCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsSymDifferenceCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the symmetric difference of the polygons as a MultiPolygon. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("polygonsSymDifferenceCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsSymDifferenceSpherical(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsSymDifferenceSpherical(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the symmetric difference of the polygons as a MultiPolygon. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("polygonsSymDifferenceSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonsUnionCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsUnionCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the union of the polygons as a MultiPolygon. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("polygonsUnionCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsUnionSpherical(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsUnionSpherical(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns the union of the polygons as a MultiPolygon. [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("polygonsUnionSpherical", *to_args(locals()))
    
    @staticmethod
    def polygonsWithinCartesian(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsWithinCartesian(polygon1, polygon2)

        Args:
        - `polygon1` — The first polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns `1` if `polygon1` is contained in `polygon2`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("polygonsWithinCartesian", *to_args(locals()))
    
    @staticmethod
    def polygonsWithinSpherical(polygon1: Any, polygon2: Any) -> Function:
        """
        polygonsWithinSpherical(polygon1, polygon2)

        Args:
        - `polygon1` — The first Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)
        - `polygon2` — The second Polygon. [`Polygon`](/sql-reference/data-types/geo#polygon)

        Returns `1` if `polygon1` lies completely within `polygon2`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("polygonsWithinSpherical", *to_args(locals()))
    
    @staticmethod
    def port(url: Any, default_port: Any | None = None) -> Function:
        """
        port(url[, default_port])

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)
        - `default_port` — Optional. The default port number to be returned. `0` by default. [`UInt16`](/sql-reference/data-types/int-uint)

        Returns the port of the URL, or the default port if there is no port in the URL or in case of a validation error. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("port", *to_args(locals()))
    
    @staticmethod
    def portRFC(url: Any, default_port: Any | None = None) -> Function:
        """
        portRFC(url[, default_port])

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)
        - `default_port` — Optional. The default port number to be returned. `0` by default. [`UInt16`](/sql-reference/data-types/int-uint)

        Returns the port or the default port if there is no port in the URL or in case of a validation error. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("portRFC", *to_args(locals()))
    
    @staticmethod
    def position(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        position(haystack, needle[, start_pos])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `start_pos` — Position (1-based) in `haystack` at which the search starts. Optional. [`UInt`](/sql-reference/data-types/int-uint)

        Returns starting position in bytes and counting from 1, if the substring was found, otherwise `0`, if the substring was not found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("position", *to_args(locals()))
    
    @staticmethod
    def positionCaseInsensitive(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        positionCaseInsensitive(haystack, needle[, start_pos])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `start_pos` — Optional. Position (1-based) in `haystack` at which the search starts. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns starting position in bytes and counting from 1, if the substring was found, otherwise `0`, if the substring was not found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("positionCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def positionCaseInsensitiveUTF8(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        positionCaseInsensitiveUTF8(haystack, needle[, start_pos])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `start_pos` — Optional. Position (1-based) in `haystack` at which the search starts. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns starting position in bytes and counting from 1, if the substring was found, otherwise `0`, if the substring was not found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("positionCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def positionUTF8(haystack: Any, needle: Any, start_pos: Any | None = None) -> Function:
        """
        positionUTF8(haystack, needle[, start_pos])

        Args:
        - `haystack` — String in which the search is performed. [`String`](/sql-reference/data-types/string) or [`Enum`](/sql-reference/data-types/enum)
        - `needle` — Substring to be searched. [`String`](/sql-reference/data-types/string)
        - `start_pos` — Optional. Position (1-based) in `haystack` at which the search starts. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns starting position in bytes and counting from 1, if the substring was found, otherwise `0`, if the substring was not found. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("positionUTF8", *to_args(locals()))
    
    @staticmethod
    def positiveModulo(x: Any, y: Any) -> Function:
        """
        positiveModulo(x, y)

        Args:
        - `x` — The dividend. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `y` — The divisor (modulus). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the difference between `x` and the nearest integer not greater than
        `x` divisible by `y`.
        """
        return Function("positiveModulo", *to_args(locals()))
    
    @staticmethod
    def positiveModuloOrNull(x: Any, y: Any) -> Function:
        """
        positiveModuloOrNull(x, y)

        Args:
        - `x` — The dividend. [`(U)Int*`](/sql-reference/data-types/int-uint)/[`Float32/64`](/sql-reference/data-types/float). - `x` — The divisor (modulus). [`(U)Int*`](/sql-reference/data-types/int-uint)/[`Float32/64`](/sql-reference/data-types/float). 
        Returns the difference between `x` and the nearest integer not greater than
        `x` divisible by `y`, `null` when the divisor is zero.
        """
        return Function("positiveModuloOrNull", *to_args(locals()))
    
    @staticmethod
    def pow(x: Any, y: Any) -> Function:
        """
        pow(x, y)

        Args:
        - `x` — The base. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        - `y` — The exponent. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns x^y [`Float64`](/sql-reference/data-types/float)
        """
        return Function("pow", *to_args(locals()))
    
    @staticmethod
    def printf(format: Any, sub1: Any | None = None, sub2: Any | None = None) -> Function:
        """
        printf(format[, sub1, sub2, ...])

        Args:
        - `format` — The format string with `%` specifiers. [`String`](/sql-reference/data-types/string)
        - `sub1, sub2, ...` — Optional. Zero or more values to substitute into the format string. [`Any`](/sql-reference/data-types)

        Returns a formatted string. [`String`](/sql-reference/data-types/string)
        """
        return Function("printf", *to_args(locals()))
    
    @staticmethod
    def proportionsZTest(successes_x: Any, successes_y: Any, trials_x: Any, trials_y: Any, conf_level: Any, pool_type: Any) -> Function:
        """
        proportionsZTest(successes_x, successes_y, trials_x, trials_y, conf_level, pool_type)

        Args:
        - `successes_x` — Number of successes in population x. [`UInt64`](/sql-reference/data-types/int-uint)
        - `successes_y` — Number of successes in population y. [`UInt64`](/sql-reference/data-types/int-uint)
        - `trials_x` — Number of trials in population x. [`UInt64`](/sql-reference/data-types/int-uint)
        - `trials_y` — Number of trials in population y. [`UInt64`](/sql-reference/data-types/int-uint)
        - `conf_level` — Confidence level for the test. [`Float64`](/sql-reference/data-types/float)
        - `pool_type` — Selection of pooling method for standard error estimation. Can be either 'unpooled' or 'pooled'. [`String`](/sql-reference/data-types/string)

        Returns a tuple containing: `z_stat` (Z statistic), `p_val` (P value), `ci_low` (lower confidence interval), `ci_high` (upper confidence interval). [`Tuple(Float64, Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("proportionsZTest", *to_args(locals()))
    
    @staticmethod
    def protocol(url: Any) -> Function:
        """
        protocol(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the protocol of the URL, or an empty string if it cannot be determined. [`String`](/sql-reference/data-types/string)
        """
        return Function("protocol", *to_args(locals()))
    
    @staticmethod
    def punycodeDecode(s: Any) -> Function:
        """
        punycodeDecode(s)

        Args:
        - `s` — Punycode-encoded string. [`String`](/sql-reference/data-types/string)

        Returns the plaintext of the input value. [`String`](/sql-reference/data-types/string)
        """
        return Function("punycodeDecode", *to_args(locals()))
    
    @staticmethod
    def punycodeEncode(s: Any) -> Function:
        """
        punycodeEncode(s)

        Args:
        - `s` — Input value. [`String`](/sql-reference/data-types/string)

        Returns a Punycode representation of the input value. [`String`](/sql-reference/data-types/string)
        """
        return Function("punycodeEncode", *to_args(locals()))
    
    @staticmethod
    def quantile(level: Any) -> Function:
        """
        quantile(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantile", *to_args(locals()))
    
    @staticmethod
    def quantileBFloat16(level: Any) -> Function:
        """
        quantileBFloat16[(level)](expr)

        Args:
        - `expr` — Column with numeric data. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantileBFloat16", *to_args(locals()))
    
    @staticmethod
    def quantileBFloat16Weighted(level: Any) -> Function:
        """
        quantileBFloat16Weighted(level)(expr, weight)

        Args:
        - `expr` — Column with numeric data. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `weight` — Column with weights of sequence members. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantileBFloat16Weighted", *to_args(locals()))
    
    @staticmethod
    def quantileDD(relative_accuracy: Any, level: Any | None = None) -> Function:
        """
        quantileDD(relative_accuracy, [level])(expr)

        Args:
        - `expr` — Column with numeric data. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantileDD", *to_args(locals()))
    
    @staticmethod
    def quantileDeterministic(level: Any) -> Function:
        """
        quantileDeterministic(level)(expr, determinator)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `determinator` — Number whose hash is used instead of a random number generator in the reservoir sampling algorithm to make the result of sampling deterministic. As a determinator you can use any deterministic positive number, for example, a user id or an event id. If the same determinator value occurs too often, the function works incorrectly. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns an approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileDeterministic", *to_args(locals()))
    
    @staticmethod
    def quantileExact(level: Any) -> Function:
        """
        quantileExact(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Quantile of the specified level. For numeric data types the output format will be the same as the input format. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileExact", *to_args(locals()))
    
    @staticmethod
    def quantileExactExclusive(level: Any) -> Function:
        """
        quantileExactExclusive(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantileExactExclusive", *to_args(locals()))
    
    @staticmethod
    def quantileExactHigh(level: Any) -> Function:
        """
        quantileExactHigh(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileExactHigh", *to_args(locals()))
    
    @staticmethod
    def quantileExactInclusive(level: Any) -> Function:
        """
        quantileExactInclusive(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantileExactInclusive", *to_args(locals()))
    
    @staticmethod
    def quantileExactLow(level: Any) -> Function:
        """
        quantileExactLow(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileExactLow", *to_args(locals()))
    
    @staticmethod
    def quantileExactWeighted(level: Any) -> Function:
        """
        quantileExactWeighted(level)(expr, weight)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `weight` — Column with weights of sequence members. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileExactWeighted", *to_args(locals()))
    
    @staticmethod
    def quantileExactWeightedInterpolated(level: Any) -> Function:
        """
        quantileExactWeightedInterpolated(level)(expr, weight)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `weight` — Column with weights of sequence members. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileExactWeightedInterpolated", *to_args(locals()))
    
    @staticmethod
    def quantileGK(accuracy: Any, level: Any) -> Function:
        """
        quantileGK(accuracy, level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the quantile of the specified level and accuracy. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileGK", *to_args(locals()))
    
    @staticmethod
    def quantileInterpolatedWeighted(level: Any) -> Function:
        """
        quantileInterpolatedWeighted(level)(expr, weight)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `weight` — Column with weights of sequence members. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileInterpolatedWeighted", *to_args(locals()))
    
    @staticmethod
    def quantilePrometheusHistogram(level: Any) -> Function:
        """
        quantilePrometheusHistogram(level)(bucket_upper_bound, cumulative_bucket_value)

        Args:
        - `bucket_upper_bound` — Upper bounds of the histogram buckets. The highest bucket must have an upper bound of `+Inf`. [`Float64`](/sql-reference/data-types/float)
        - `cumulative_bucket_value` — Cumulative values of the histogram buckets. Values must be monotonically increasing as the bucket upper bound increases. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float64`](/sql-reference/data-types/float)

        Returns the quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantilePrometheusHistogram", *to_args(locals()))
    
    @staticmethod
    def quantileTDigest(level: Any) -> Function:
        """
        quantileTDigest(level)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileTDigest", *to_args(locals()))
    
    @staticmethod
    def quantileTDigestWeighted(level: Any) -> Function:
        """
        quantileTDigestWeighted(level)(expr, weight)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `weight` — Column with weights of sequence elements. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Approximate quantile of the specified level. [`Float64`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("quantileTDigestWeighted", *to_args(locals()))
    
    @staticmethod
    def quantileTiming(level: Any) -> Function:
        """
        quantileTiming(level)(expr)

        Args:
        - `expr` — Expression over a column values returning a Float*-type number. If negative values are passed to the function, the behavior is undefined. If the value is greater than 30,000 (a page loading time of more than 30 seconds), it is assumed to be 30,000. [`Float*`](/sql-reference/data-types/float)

        Quantile of the specified level. If no values are passed to the function (when using `quantileTimingIf`), NaN is returned. The purpose of this is to differentiate these cases from cases that result in zero. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("quantileTiming", *to_args(locals()))
    
    @staticmethod
    def quantileTimingWeighted(level: Any) -> Function:
        """
        quantileTimingWeighted(level)(expr, weight)

        Args:
        - `expr` — Expression over a column values returning a Float*-type number. If negative values are passed to the function, the behavior is undefined. If the value is greater than 30,000 (a page loading time of more than 30 seconds), it is assumed to be 30,000. [`Float*`](/sql-reference/data-types/float)
        - `weight` — Column with weights of sequence elements. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Quantile of the specified level. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("quantileTimingWeighted", *to_args(locals()))
    
    @staticmethod
    def quantiles(level1: Any, level2: Any) -> Function:
        """
        quantiles(level1, level2, ...)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Array of approximate quantiles of the specified levels in the same order as the levels were specified. [`Array(Float64)`](/sql-reference/data-types/array) or [`Array(Date)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        """
        return Function("quantiles", *to_args(locals()))
    
    @staticmethod
    def quantilesBFloat16(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesBFloat16", *to_args(locals()))
    
    @staticmethod
    def quantilesBFloat16Weighted(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesBFloat16Weighted", *to_args(locals()))
    
    @staticmethod
    def quantilesDD(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesDD", *to_args(locals()))
    
    @staticmethod
    def quantilesDeterministic(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesDeterministic", *to_args(locals()))
    
    @staticmethod
    def quantilesExact(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesExact", *to_args(locals()))
    
    @staticmethod
    def quantilesExactExclusive(level1: Any, level2: Any) -> Function:
        """
        quantilesExactExclusive(level1, level2, ...)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Array of quantiles of the specified levels in the same order as the levels were specified. [`Array(Float64)`](/sql-reference/data-types/array)
        """
        return Function("quantilesExactExclusive", *to_args(locals()))
    
    @staticmethod
    def quantilesExactHigh(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesExactHigh", *to_args(locals()))
    
    @staticmethod
    def quantilesExactInclusive(level1: Any, level2: Any) -> Function:
        """
        quantilesExactInclusive(level1, level2, ...)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Array of quantiles of the specified levels in the same order as the levels were specified. [`Array(Float64)`](/sql-reference/data-types/array)
        """
        return Function("quantilesExactInclusive", *to_args(locals()))
    
    @staticmethod
    def quantilesExactLow(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesExactLow", *to_args(locals()))
    
    @staticmethod
    def quantilesExactWeighted(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesExactWeighted", *to_args(locals()))
    
    @staticmethod
    def quantilesExactWeightedInterpolated(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesExactWeightedInterpolated", *to_args(locals()))
    
    @staticmethod
    def quantilesGK(accuracy: Any, level1: Any, level2: Any) -> Function:
        """
        quantilesGK(accuracy, level1, level2, ...)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Array of quantiles of the specified levels in the same order as the levels were specified. [`Array(Float64)`](/sql-reference/data-types/array) or [`Array(Date)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        """
        return Function("quantilesGK", *to_args(locals()))
    
    @staticmethod
    def quantilesInterpolatedWeighted(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("quantilesInterpolatedWeighted", *to_args(locals()))
    
    @staticmethod
    def quantilesPrometheusHistogram(level: Any) -> Function:
        """
        quantilePrometheusHistogram(level)(bucket_upper_bound, cumulative_bucket_value)

        Args:
        - `bucket_upper_bound` — Upper bounds of the histogram buckets. The highest bucket must have an upper bound of `+Inf`. [`Float64`](/sql-reference/data-types/float)
        - `cumulative_bucket_value` — Cumulative values of the histogram buckets. Values must be monotonically increasing as the bucket upper bound increases. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float64`](/sql-reference/data-types/float)

        Returns the quantile of the specified level. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("quantilesPrometheusHistogram", *to_args(locals()))
    
    @staticmethod
    def quantilesTDigest(level1: Any, level2: Any) -> Function:
        """
        quantilesTDigest(level1, level2, ...)(expr)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Array of approximate quantiles of the specified levels in the same order as the levels were specified. [`Array(Float64)`](/sql-reference/data-types/array) or [`Array(Date)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        """
        return Function("quantilesTDigest", *to_args(locals()))
    
    @staticmethod
    def quantilesTDigestWeighted(level1: Any, level2: Any) -> Function:
        """
        quantilesTDigestWeighted(level1, level2, ...)(expr, weight)

        Args:
        - `expr` — Expression over the column values resulting in numeric data types, Date or DateTime. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `weight` — Column with weights of sequence elements. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Array of approximate quantiles of the specified levels in the same order as the levels were specified. [`Array(Float64)`](/sql-reference/data-types/array) or [`Array(Date)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        """
        return Function("quantilesTDigestWeighted", *to_args(locals()))
    
    @staticmethod
    def quantilesTiming(level1: Any, level2: Any) -> Function:
        """
        quantilesTiming(level1, level2, ...)(expr)

        Args:
        - `expr` — Expression over a column values returning a Float*-type number. If negative values are passed to the function, the behavior is undefined. If the value is greater than 30,000 (a page loading time of more than 30 seconds), it is assumed to be 30,000. [`Float*`](/sql-reference/data-types/float)

        Array of quantiles of the specified levels in the same order as the levels were specified. [`Array(Float32)`](/sql-reference/data-types/array)
        """
        return Function("quantilesTiming", *to_args(locals()))
    
    @staticmethod
    def quantilesTimingWeighted(level1: Any, level2: Any) -> Function:
        """
        quantilesTimingWeighted(level1, level2, ...)(expr, weight)

        Args:
        - `expr` — Expression over a column values returning a Float*-type number. If negative values are passed to the function, the behavior is undefined. If the value is greater than 30,000 (a page loading time of more than 30 seconds), it is assumed to be 30,000. [`Float*`](/sql-reference/data-types/float)
        - `weight` — Column with weights of sequence elements. Weight is a number of value occurrences. [`UInt*`](/sql-reference/data-types/int-uint)

        Array of quantiles of the specified levels in the same order as the levels were specified. [`Array(Float32)`](/sql-reference/data-types/array)
        """
        return Function("quantilesTimingWeighted", *to_args(locals()))
    
    @staticmethod
    def queryID() -> Function:
        """
        queryID()

        
        Returns the ID of the current query. [`String`](/sql-reference/data-types/string)
        """
        return Function("queryID", *to_args(locals()))
    
    @staticmethod
    def queryString(url: Any) -> Function:
        """
        queryString(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the query string of the URL without the initial question mark and fragment. [`String`](/sql-reference/data-types/string)
        """
        return Function("queryString", *to_args(locals()))
    
    @staticmethod
    def queryStringAndFragment(url: Any) -> Function:
        """
        queryStringAndFragment(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the query string and fragment identifier of the URL. [`String`](/sql-reference/data-types/string)
        """
        return Function("queryStringAndFragment", *to_args(locals()))
    
    @staticmethod
    def radians(x: Any) -> Function:
        """
        radians(x)

        Args:
        - `x` — Input in degrees. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns value in radians [`Float64`](/sql-reference/data-types/float)
        """
        return Function("radians", *to_args(locals()))
    
    @staticmethod
    def rand(x: Any | None = None) -> Function:
        """
        rand([x])

        Args:
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random number of type `UInt32`. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("rand", *to_args(locals()))
    
    @staticmethod
    def rand64(x: Any | None = None) -> Function:
        """
        rand64([x])

        Args:
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random UInt64 number with uniform distribution. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("rand64", *to_args(locals()))
    
    @staticmethod
    def randBernoulli(probability: Any, x: Any | None = None) -> Function:
        """
        randBernoulli(probability[, x])

        Args:
        - `probability` — The probability of success as a value between `0` and `1`. [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified Bernoulli distribution. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("randBernoulli", *to_args(locals()))
    
    @staticmethod
    def randBinomial(experiments: Any, probability: Any, x: Any | None = None) -> Function:
        """
        randBinomial(experiments, probability[, x])

        Args:
        - `experiments` — The number of experiments [`UInt64`](/sql-reference/data-types/int-uint)
        - `probability` — The probability of success in each experiment as a value between `0` and `1` [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified binomial distribution. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("randBinomial", *to_args(locals()))
    
    @staticmethod
    def randCanonical(x: Any | None = None) -> Function:
        """
        randCanonical([x])

        Args:
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randCanonical", *to_args(locals()))
    
    @staticmethod
    def randChiSquared(degree_of_freedom: Any, x: Any | None = None) -> Function:
        """
        randChiSquared(degree_of_freedom[, x])

        Args:
        - `degree_of_freedom` — Degrees of freedom. [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified chi-square distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randChiSquared", *to_args(locals()))
    
    @staticmethod
    def randConstant(x: Any | None = None) -> Function:
        """
        randConstant([x])

        Args:
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a column of type `UInt32` containing the same random value in each row. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("randConstant", *to_args(locals()))
    
    @staticmethod
    def randExponential(lambda_: Any, x: Any | None = None) -> Function:
        """
        randExponential(lambda[, x])

        Args:
        - `lambda` — Rate parameter or lambda value of the distribution [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified exponential distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randExponential", *to_args(locals()))
    
    @staticmethod
    def randFisherF(d1: Any, d2: Any, x: Any | None = None) -> Function:
        """
        randFisherF(d1, d2[, x])

        Args:
        - `d1` — d1 degree of freedom in `X = (S1 / d1) / (S2 / d2)`. [`Float64`](/sql-reference/data-types/float)
        - `d2` — d2 degree of freedom in `X = (S1 / d1) / (S2 / d2)`. [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified F-distribution [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randFisherF", *to_args(locals()))
    
    @staticmethod
    def randLogNormal(mean: Any, stddev: Any, x: Any | None = None) -> Function:
        """
        randLogNormal(mean, stddev[, x])

        Args:
        - `mean` — The mean value of distribution. [`Float64`](/sql-reference/data-types/float)
        - `stddev` — The standard deviation of the distribution. [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified log-normal distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randLogNormal", *to_args(locals()))
    
    @staticmethod
    def randNegativeBinomial(experiments: Any, probability: Any, x: Any | None = None) -> Function:
        """
        randNegativeBinomial(experiments, probability[, x])

        Args:
        - `experiments` — The number of experiments. [`UInt64`](/sql-reference/data-types/int-uint)
        - `probability` — `The probability of failure in each experiment as a value between `0` and `1`. [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified negative binomial distribution [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("randNegativeBinomial", *to_args(locals()))
    
    @staticmethod
    def randNormal(mean: Any, stddev: Any, x: Any | None = None) -> Function:
        """
        randNormal(mean, stddev[, x])

        Args:
        - `mean` — The mean value of distribution [`Float64`](/sql-reference/data-types/float)
        - `stddev` — The standard deviation of the distribution [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified normal distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randNormal", *to_args(locals()))
    
    @staticmethod
    def randPoisson(n: Any, x: Any | None = None) -> Function:
        """
        randPoisson(n[, x])

        Args:
        - `n` — The mean number of occurrences. [`UInt64`](/sql-reference/data-types/int-uint)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified Poisson distribution. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("randPoisson", *to_args(locals()))
    
    @staticmethod
    def randStudentT(degree_of_freedom: Any, x: Any | None = None) -> Function:
        """
        randStudentT(degree_of_freedom[, x])

        Args:
        - `degree_of_freedom` — Degrees of freedom. [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random Float64 number drawn from the specified Student's t-distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randStudentT", *to_args(locals()))
    
    @staticmethod
    def randUniform(min: Any, max: Any, x: Any | None = None) -> Function:
        """
        randUniform(min, max[, x])

        Args:
        - `min` — Left boundary of the range (inclusive). [`Float64`](/sql-reference/data-types/float)
        - `max` — Right boundary of the range (inclusive). [`Float64`](/sql-reference/data-types/float)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a random number drawn uniformly from the interval formed by `min` and `max`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("randUniform", *to_args(locals()))
    
    @staticmethod
    def randomFixedString(length: Any) -> Function:
        """
        randomFixedString(length)

        Args:
        - `length` — Length of the string in bytes. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns a string filled with random bytes. [`FixedString`](/sql-reference/data-types/fixedstring)
        """
        return Function("randomFixedString", *to_args(locals()))
    
    @staticmethod
    def randomPrintableASCII(length: Any, x: Any | None = None) -> Function:
        """
        randomPrintableASCII(length[, x])

        Args:
        - `length` — String length in bytes. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a string with a random set of ASCII printable characters. [`String`](/sql-reference/data-types/string)
        """
        return Function("randomPrintableASCII", *to_args(locals()))
    
    @staticmethod
    def randomString(length: Any, x: Any | None = None) -> Function:
        """
        randomString(length[, x])

        Args:
        - `length` — Length of the string in bytes. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `x` — Optional and ignored. The only purpose of the argument is to prevent [common subexpression elimination](/sql-reference/functions/overview#common-subexpression-elimination) when the same function call is used multiple times in a query. [`Any`](/sql-reference/data-types)

        Returns a string filled with random bytes. [`String`](/sql-reference/data-types/string)
        """
        return Function("randomString", *to_args(locals()))
    
    @staticmethod
    def randomStringUTF8(length: Any) -> Function:
        """
        randomStringUTF8(length)

        Args:
        - `length` — Length of the string in code points. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a string filled with random UTF-8 codepoints. [`String`](/sql-reference/data-types/string)
        """
        return Function("randomStringUTF8", *to_args(locals()))
    
    @staticmethod
    def range(start: Any | None = None, end: Any | None = None, step: Any | None = None) -> Function:
        """
        range([start, ] end [, step])

        Args:
        - `start` — Optional. The first element of the array. Required if `step` is used. Default value: `0`. - `end` — Required. The number before which the array is constructed. - `step` — Optional. Determines the incremental step between each element in the array. Default value: `1`. 
        Array of numbers from `start` to `end - 1` by `step`. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("range", *to_args(locals()))
    
    @staticmethod
    def rank(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("rank", *to_args(locals()))
    
    @staticmethod
    def rankCorr(x: Any, y: Any) -> Function:
        """
        rankCorr(x, y)

        Args:
        - `x` — Arbitrary value. [`Float*`](/sql-reference/data-types/float)
        - `y` — Arbitrary value. [`Float*`](/sql-reference/data-types/float)

        Returns a rank correlation coefficient of the ranks of x and y. The value ranges from -1 to +1. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("rankCorr", *to_args(locals()))
    
    @staticmethod
    def readWKB(wkb_string: Any) -> Function:
        """
        readWKB(wkb_string)

        Args:
        - `wkb_string` — The input WKB string representing a Point geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the Geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKB", *to_args(locals()))
    
    @staticmethod
    def readWKBLineString(wkb_string: Any) -> Function:
        """
        readWKBLineString(wkb_string)

        Args:
        - `wkb_string` — The input WKB string representing a LineString geometry. [`String`](/sql-reference/data-types/string)

        Returns returns a ClickHouse internal representation of the linestring geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKBLineString", *to_args(locals()))
    
    @staticmethod
    def readWKBMultiLineString(wkb_string: Any) -> Function:
        """
        readWKBMultiLineString(wkb_string)

        Args:
        - `wkb_string` — The input WKB string representing a MultiLineString geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the multilinestring geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKBMultiLineString", *to_args(locals()))
    
    @staticmethod
    def readWKBMultiPolygon(wkb_string: Any) -> Function:
        """
        readWKBMultiPolygon(wkb_string)

        Args:
        - `wkb_string` — The input WKB string representing a MultiPolygon geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the MultiPolygon geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKBMultiPolygon", *to_args(locals()))
    
    @staticmethod
    def readWKBPoint(wkb_string: Any) -> Function:
        """
        readWKBPoint(wkb_string)

        Args:
        - `wkb_string` — The input WKB string representing a Point geometry. [`String`](/sql-reference/data-types/string)

        The function returns a ClickHouse internal representation of the point geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKBPoint", *to_args(locals()))
    
    @staticmethod
    def readWKBPolygon(wkb_string: Any) -> Function:
        """
        readWKBPolygon(wkb_string)

        Args:
        - `wkb_string` — The input WKB string representing a Polygon geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the Polygon geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKBPolygon", *to_args(locals()))
    
    @staticmethod
    def readWKT(wkt_string: Any) -> Function:
        """
        readWKT(wkt_string)

        Args:
        - `wkt_string` — The input WKT string representing a LineString geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the Geometry.
        """
        return Function("readWKT", *to_args(locals()))
    
    @staticmethod
    def readWKTLineString(wkt_string: Any) -> Function:
        """
        readWKTLineString(wkt_string)

        Args:
        - `wkt_string` — The input WKT string representing a LineString geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the linestring geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKTLineString", *to_args(locals()))
    
    @staticmethod
    def readWKTMultiLineString(wkt_string: Any) -> Function:
        """
        readWKTMultiLineString(wkt_string)

        Args:
        - `wkt_string` — The input WKT string representing a MultiLineString geometry. [`String`](/sql-reference/data-types/string)

        Returns the function returns a ClickHouse internal representation of the multilinestring geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKTMultiLineString", *to_args(locals()))
    
    @staticmethod
    def readWKTMultiPolygon(wkt_string: Any) -> Function:
        """
        readWKTMultiPolygon(wkt_string)

        Args:
        - `wkt_string` — String starting with `MULTIPOLYGON` [`String`](/sql-reference/data-types/string)

        Returns a MultiPolygon [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        """
        return Function("readWKTMultiPolygon", *to_args(locals()))
    
    @staticmethod
    def readWKTPoint(wkt_string: Any) -> Function:
        """
        readWKTPoint(wkt_string)

        Args:
        - `wkt_string` — The input WKT string representing a Point geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the Point geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKTPoint", *to_args(locals()))
    
    @staticmethod
    def readWKTPolygon(wkt_string: Any) -> Function:
        """
        readWKTPolygon(wkt_string)

        Args:
        - `wkt_string` — String starting with `POLYGON` [`String`](/sql-reference/data-types/string)

        Returns a Polygon [`Polygon`](/sql-reference/data-types/geo#polygon)
        """
        return Function("readWKTPolygon", *to_args(locals()))
    
    @staticmethod
    def readWKTRing(wkt_string: Any) -> Function:
        """
        readWKTRing(wkt_string)

        Args:
        - `wkt_string` — The input WKT string representing a Polygon geometry. [`String`](/sql-reference/data-types/string)

        Returns a ClickHouse internal representation of the ring (closed linestring) geometry. [`Geo`](/sql-reference/data-types/geo)
        """
        return Function("readWKTRing", *to_args(locals()))
    
    @staticmethod
    def regexpExtract(haystack: Any, pattern: Any, index: Any | None = None) -> Function:
        """
        regexpExtract(haystack, pattern[, index])

        Args:
        - `haystack` — String, in which regexp pattern will be matched. [`String`](/sql-reference/data-types/string)
        - `pattern` — String, regexp expression. `pattern` may contain multiple regexp groups, `index` indicates which regex group to extract. An index of 0 means matching the entire regular expression. [`const String`](/sql-reference/data-types/string)
        - `index` — Optional. An integer number greater or equal 0 with default 1. It represents which regex group to extract. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a string match [`String`](/sql-reference/data-types/string)
        """
        return Function("regexpExtract", *to_args(locals()))
    
    @staticmethod
    def regexpQuoteMeta(s: Any) -> Function:
        """
        regexpQuoteMeta(s)

        Args:
        - `s` — The input string containing characters to be escaped for regex. [`String`](/sql-reference/data-types/string)

        Returns a string with regex special characters escaped. [`String`](/sql-reference/data-types/string)
        """
        return Function("regexpQuoteMeta", *to_args(locals()))
    
    @staticmethod
    def regionHierarchy(id: Any, geobase: Any | None = None) -> Function:
        """
        regionHierarchy(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Array of region IDs consisting of the passed region and all parents along the chain [`Array(UInt32)`](/sql-reference/data-types/array)
        """
        return Function("regionHierarchy", *to_args(locals()))
    
    @staticmethod
    def regionIn(lhs: Any, rhs: Any, geobase: Any | None = None) -> Function:
        """
        regionIn(lhs, rhs[, geobase])

        Args:
        - `lhs` — Lhs region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `rhs` — Rhs region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns `1` if the region belongs, `0` otherwise [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("regionIn", *to_args(locals()))
    
    @staticmethod
    def regionToArea(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToArea(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the region ID for the appropriate area, if it exists, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToArea", *to_args(locals()))
    
    @staticmethod
    def regionToCity(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToCity(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the region ID for the appropriate city, if it exists, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToCity", *to_args(locals()))
    
    @staticmethod
    def regionToContinent(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToContinent(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the region ID for the appropriate continent, if it exists, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToContinent", *to_args(locals()))
    
    @staticmethod
    def regionToCountry(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToCountry(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the region ID for the appropriate country, if it exists, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToCountry", *to_args(locals()))
    
    @staticmethod
    def regionToDistrict(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToDistrict(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the region ID for the appropriate district, if it exists, otherwise returns `0` [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToDistrict", *to_args(locals()))
    
    @staticmethod
    def regionToName(id: Any, lang: Any | None = None) -> Function:
        """
        regionToName(id[, lang])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `lang` — Optional. Language code for the region name (e.g., 'en', 'ru'). Defaults to 'en'. [`String`](/sql-reference/data-types/string)

        Name of the region in the specified language, or an empty string if the region doesn't exist [`String`](/sql-reference/data-types/string)
        """
        return Function("regionToName", *to_args(locals()))
    
    @staticmethod
    def regionToPopulation(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToPopulation(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the population for the region, or `0` if there is none [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToPopulation", *to_args(locals()))
    
    @staticmethod
    def regionToTopContinent(id: Any, geobase: Any | None = None) -> Function:
        """
        regionToTopContinent(id[, geobase])

        Args:
        - `id` — Region ID from the geobase [`UInt32`](/sql-reference/data-types/int-uint)
        - `geobase` — Optional. The dictionary key. [`String`](/sql-reference/data-types/string)

        Returns the identifier of the top level continent (the latter when you climb the hierarchy of regions), or `0` if there is none [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("regionToTopContinent", *to_args(locals()))
    
    @staticmethod
    def reinterpret(x: Any, type: Any) -> Function:
        """
        reinterpret(x, type)

        Args:
        - `x` — Any type. [`Any`](/sql-reference/data-types)
        - `type` — Destination type. If it is an array, then the array element type must be a fixed length type. [`String`](/sql-reference/data-types/string)

        Destination type value. [`Any`](/sql-reference/data-types)
        """
        return Function("reinterpret", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsDate(x: Any) -> Function:
        """
        reinterpretAsDate(x)

        Args:
        - `x` — Number of days since the beginning of the Unix Epoch. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Date. [`Date`](/sql-reference/data-types/date)
        """
        return Function("reinterpretAsDate", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsDateTime(x: Any) -> Function:
        """
        reinterpretAsDateTime(x)

        Args:
        - `x` — Number of seconds since the beginning of the Unix Epoch. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Date and Time. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("reinterpretAsDateTime", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsFixedString(x: Any) -> Function:
        """
        reinterpretAsFixedString(x)

        Args:
        - `x` — Value to reinterpret to string. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Fixed string containing bytes representing `x`. [`FixedString`](/sql-reference/data-types/fixedstring)
        """
        return Function("reinterpretAsFixedString", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsFloat32(x: Any) -> Function:
        """
        reinterpretAsFloat32(x)

        Args:
        - `x` — Value to reinterpret as Float32. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("reinterpretAsFloat32", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsFloat64(x: Any) -> Function:
        """
        reinterpretAsFloat64(x)

        Args:
        - `x` — Value to reinterpret as Float64. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("reinterpretAsFloat64", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsInt128(x: Any) -> Function:
        """
        reinterpretAsInt128(x)

        Args:
        - `x` — Value to reinterpret as Int128. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Int128`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsInt128", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsInt16(x: Any) -> Function:
        """
        reinterpretAsInt16(x)

        Args:
        - `x` — Value to reinterpret as Int16. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Int16`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsInt16", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsInt256(x: Any) -> Function:
        """
        reinterpretAsInt256(x)

        Args:
        - `x` — Value to reinterpret as Int256. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Int256`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsInt256", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsInt32(x: Any) -> Function:
        """
        reinterpretAsInt32(x)

        Args:
        - `x` — Value to reinterpret as Int32. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsInt32", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsInt64(x: Any) -> Function:
        """
        reinterpretAsInt64(x)

        Args:
        - `x` — Value to reinterpret as Int64. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsInt64", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsInt8(x: Any) -> Function:
        """
        reinterpretAsInt8(x)

        Args:
        - `x` — Value to reinterpret as Int8. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`Int8`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsInt8", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsString(x: Any) -> Function:
        """
        reinterpretAsString(x)

        Args:
        - `x` — Value to reinterpret to string. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        String containing bytes representing `x`. [`String`](/sql-reference/data-types/string)
        """
        return Function("reinterpretAsString", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUInt128(x: Any) -> Function:
        """
        reinterpretAsUInt128(x)

        Args:
        - `x` — Value to reinterpret as UInt128. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`UInt128`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsUInt128", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUInt16(x: Any) -> Function:
        """
        reinterpretAsUInt16(x)

        Args:
        - `x` — Value to reinterpret as UInt16. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsUInt16", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUInt256(x: Any) -> Function:
        """
        reinterpretAsUInt256(x)

        Args:
        - `x` — Value to reinterpret as UInt256. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`UInt256`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsUInt256", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUInt32(x: Any) -> Function:
        """
        reinterpretAsUInt32(x)

        Args:
        - `x` — Value to reinterpret as UInt32. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsUInt32", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUInt64(x: Any) -> Function:
        """
        reinterpretAsUInt64(x)

        Args:
        - `x` — Value to reinterpret as UInt64. [`Int*`](/sql-reference/data-types/int-uint) or [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value of `x`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsUInt64", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUInt8(x: Any) -> Function:
        """
        reinterpretAsUInt8(x)

        Args:
        - `x` — Value to reinterpret as UInt8. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`UUID`](/sql-reference/data-types/uuid) or [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the reinterpreted value `x`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("reinterpretAsUInt8", *to_args(locals()))
    
    @staticmethod
    def reinterpretAsUUID(fixed_string: Any) -> Function:
        """
        reinterpretAsUUID(fixed_string)

        Args:
        - `fixed_string` — Big-endian byte string. [`FixedString`](/sql-reference/data-types/fixedstring)

        The UUID type value. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("reinterpretAsUUID", *to_args(locals()))
    
    @staticmethod
    def removeDiacriticsUTF8(str: Any) -> Function:
        """
        removeDiacriticsUTF8(str)

        Args:
        - `str` — UTF-8 encoded input string. [`String`](/sql-reference/data-types/string)

        UTF-8 string with diacritics removed. [`String`](/sql-reference/data-types/string)
        """
        return Function("removeDiacriticsUTF8", *to_args(locals()))
    
    @staticmethod
    def repeat(s: Any, n: Any) -> Function:
        """
        repeat(s, n)

        Args:
        - `s` — The string to repeat. [`String`](/sql-reference/data-types/string)
        - `n` — The number of times to repeat the string. [`(U)Int*`](/sql-reference/data-types/int-uint)

        A string containing string `s` repeated `n` times. If `n` is negative, the function returns the empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("repeat", *to_args(locals()))
    
    @staticmethod
    def replaceAll(haystack: Any, pattern: Any, replacement: Any) -> Function:
        """
        replaceAll(haystack, pattern, replacement)

        Args:
        - `haystack` — The input string to search in. [`String`](/sql-reference/data-types/string)
        - `pattern` — The substring to find and replace. [`const String`](/sql-reference/data-types/string)
        - `replacement` — The string to replace the pattern with. [`const String`](/sql-reference/data-types/string)

        Returns a string with all occurrences of pattern replaced. [`String`](/sql-reference/data-types/string)
        """
        return Function("replaceAll", *to_args(locals()))
    
    @staticmethod
    def replaceOne(haystack: Any, pattern: Any, replacement: Any) -> Function:
        """
        replaceOne(haystack, pattern, replacement)

        Args:
        - `haystack` — The input string to search in. [`String`](/sql-reference/data-types/string)
        - `pattern` — The substring to find and replace. [`const String`](/sql-reference/data-types/string)
        - `replacement` — The string to replace the pattern with. [`const String`](/sql-reference/data-types/string)

        Returns a string with the first occurrence of pattern replaced. [`String`](/sql-reference/data-types/string)
        """
        return Function("replaceOne", *to_args(locals()))
    
    @staticmethod
    def replaceRegexpAll(haystack: Any, pattern: Any, replacement: Any) -> Function:
        """
        replaceRegexpAll(haystack, pattern, replacement)

        Args:
        - `haystack` — The input string to search in. [`String`](/sql-reference/data-types/string)
        - `pattern` — The regular expression pattern to find. [`const String`](/sql-reference/data-types/string)
        - `replacement` — The string to replace the pattern with, may contain substitutions. [`const String`](/sql-reference/data-types/string)

        Returns a string with all regex matches replaced. [`String`](/sql-reference/data-types/string)
        """
        return Function("replaceRegexpAll", *to_args(locals()))
    
    @staticmethod
    def replaceRegexpOne(haystack: Any, pattern: Any, replacement: Any) -> Function:
        """
        replaceRegexpOne(haystack, pattern, replacement)

        Args:
        - `haystack` — The input string to search in. [`String`](/sql-reference/data-types/string)
        - `pattern` — The regular expression pattern to find. [`const String`](/sql-reference/data-types/string)
        - `replacement` — The string to replace the pattern with, may contain substitutions. [`const String`](/sql-reference/data-types/string)

        Returns a string with the first regex match replaced. [`String`](/sql-reference/data-types/string)
        """
        return Function("replaceRegexpOne", *to_args(locals()))
    
    @staticmethod
    def replicate(x: Any, arr: Any) -> Function:
        """
        replicate(x, arr)

        Args:
        - `x` — The value to fill the result array with. [`Any`](/sql-reference/data-types)
        - `arr` — An array. [`Array(T)`](/sql-reference/data-types/array)

        Returns an array of the same length as `arr` filled with value `x`. [`Array(T)`](/sql-reference/data-types/array)
        """
        return Function("replicate", *to_args(locals()))
    
    @staticmethod
    def retention(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("retention", *to_args(locals()))
    
    @staticmethod
    def reverse(arr: Any, str: Any) -> Function:
        """
        reverse(arr | str)

        Args:
        - `arr | str` — The source array or string. [`Array(T)`](/sql-reference/data-types/array) or [`String`](/sql-reference/data-types/string)

        Returns an array or string with the order of elements or characters reversed.
        """
        return Function("reverse", *to_args(locals()))
    
    @staticmethod
    def reverseBySeparator(string: Any, separator: Any | None = None) -> Function:
        """
        reverseBySeparator(string[, separator])

        Args:
        - `string` — The input string to reverse the order of its parts. [`String`](/sql-reference/data-types/string)
        - `separator` — The separator string used to identify parts. If not provided, uses '.' (dot). Default: '.' [`String`](/sql-reference/data-types/string)

        Returns a string with substrings ordered from right to left of the original string, joined by the same separator. [`String`](/sql-reference/data-types/string)
        """
        return Function("reverseBySeparator", *to_args(locals()))
    
    @staticmethod
    def reverseUTF8(s: Any) -> Function:
        """
        reverseUTF8(s)

        Args:
        - `s` — String containing valid UTF-8 encoded text. [`String`](/sql-reference/data-types/string)

        Returns a string with the sequence of Unicode code points reversed. [`String`](/sql-reference/data-types/string)
        """
        return Function("reverseUTF8", *to_args(locals()))
    
    @staticmethod
    def revision() -> Function:
        """
        revision()

        
        Returns the current ClickHouse server revision. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("revision", *to_args(locals()))
    
    @staticmethod
    def right(s: Any, offset: Any) -> Function:
        """
        right(s, offset)

        Args:
        - `s` — The string to calculate a substring from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `offset` — The number of bytes of the offset. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns:
        - For positive `offset`, a substring of `s` with `offset` many bytes, starting from the right of the string.
        - For negative `offset`, a substring of `s` with `length(s) - |offset|` bytes, starting from the right of the string.
        - An empty string if `length` is `0`.
             [`String`](/sql-reference/data-types/string)
        """
        return Function("right", *to_args(locals()))
    
    @staticmethod
    def rightPad(string: Any, length: Any, pad_string: Any | None = None) -> Function:
        """
        rightPad(string, length[, pad_string])

        Args:
        - `string` — Input string that should be padded. [`String`](/sql-reference/data-types/string)
        - `length` — The length of the resulting string. If the value is smaller than the input string length, then the input string is shortened to `length` characters. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `pad_string` — Optional. The string to pad the input string with. If not specified, then the input string is padded with spaces. [`String`](/sql-reference/data-types/string)

        Returns a right-padded string of the given length. [`String`](/sql-reference/data-types/string)
        """
        return Function("rightPad", *to_args(locals()))
    
    @staticmethod
    def rightPadUTF8(string: Any, length: Any, pad_string: Any | None = None) -> Function:
        """
        rightPadUTF8(string, length[, pad_string])

        Args:
        - `string` — Input string that should be padded. [`String`](/sql-reference/data-types/string)
        - `length` — The length of the resulting string. If the value is smaller than the input string length, then the input string is shortened to `length` characters. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `pad_string` — Optional. The string to pad the input string with. If not specified, then the input string is padded with spaces. [`String`](/sql-reference/data-types/string)

        Returns a right-padded string of the given length. [`String`](/sql-reference/data-types/string)
        """
        return Function("rightPadUTF8", *to_args(locals()))
    
    @staticmethod
    def rightUTF8(s: Any, offset: Any) -> Function:
        """
        rightUTF8(s, offset)

        Args:
        - `s` — The UTF-8 encoded string to calculate a substring from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `offset` — The number of bytes of the offset. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns:
        - For positive `offset`, a substring of `s` with `offset` many bytes, starting from the right of the string.
        - For negative `offset`, a substring of `s` with `length(s) - |offset|` bytes, starting from the right of the string.
        - An empty string if `length` is `0`.
             [`String`](/sql-reference/data-types/string)
        """
        return Function("rightUTF8", *to_args(locals()))
    
    @staticmethod
    def round(x: Any, N: Any | None = None) -> Function:
        """
        round(x[, N])

        Args:
        - `x` — A number to round. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `N` — Optional. The number of decimal places to round to. Defaults to `0`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a rounded number of the same type as `x`. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("round", *to_args(locals()))
    
    @staticmethod
    def roundAge(num: Any) -> Function:
        """
        roundAge(num)

        Args:
        - `age` — A number representing an age in years. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns either the highest or lowest age of the range `age` falls within. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("roundAge", *to_args(locals()))
    
    @staticmethod
    def roundBankers(x: Any, N: Any | None = None) -> Function:
        """
        roundBankers(x[, N])

        Args:
        - `x` — A number to round. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float)
        - `[, N]` — Optional. The number of decimal places to round to. Defaults to `0`. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a value rounded by the banker's rounding method. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("roundBankers", *to_args(locals()))
    
    @staticmethod
    def roundDown(num: Any, arr: Any) -> Function:
        """
        roundDown(num, arr)

        Args:
        - `num` — A number to round down. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float)
        - `arr` — Array of elements to round `num` down to. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns a number rounded down to an element in `arr`. If the value is less than the lowest bound, the lowest bound is returned. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("roundDown", *to_args(locals()))
    
    @staticmethod
    def roundDuration(num: Any) -> Function:
        """
        roundDuration(num)

        Args:
        - `num` — A number to round to one of the numbers in the set of common durations. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `0`, for `num` < 1. Otherwise, one of: `1, 10, 30, 60, 120, 180, 240, 300, 600, 1200, 1800, 3600, 7200, 18000, 36000`. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("roundDuration", *to_args(locals()))
    
    @staticmethod
    def roundToExp2(num: Any) -> Function:
        """
        roundToExp2(num)

        Args:
        - `num` — A number to round. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `num` rounded down to the nearest (whole non-negative) power of two, otherwise `0` for `num < 1`. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        """
        return Function("roundToExp2", *to_args(locals()))
    
    @staticmethod
    def rowNumberInAllBlocks() -> Function:
        """
        rowNumberInAllBlocks()

        
        Returns the ordinal number of the row in the data block starting from `0`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("rowNumberInAllBlocks", *to_args(locals()))
    
    @staticmethod
    def rowNumberInBlock() -> Function:
        """
        rowNumberInBlock()

        
        Returns the ordinal number of the row in the data block starting from `0`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("rowNumberInBlock", *to_args(locals()))
    
    @staticmethod
    def row_number(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("row_number", *to_args(locals()))
    
    @staticmethod
    def runningAccumulate(agg_state: Any, grouping: Any | None = None) -> Function:
        """
        runningAccumulate(agg_state[, grouping])

        Args:
        - `agg_state` — State of the aggregate function. [`AggregateFunction`](/sql-reference/data-types/aggregatefunction)
        - `grouping` — Optional. Grouping key. The state of the function is reset if the `grouping` value is changed. It can be any of the supported data types for which the equality operator is defined. [`Any`](/sql-reference/data-types)

        Returns the accumulated result for each row. [`Any`](/sql-reference/data-types)
        """
        return Function("runningAccumulate", *to_args(locals()))
    
    @staticmethod
    def runningConcurrency(start: Any, end: Any) -> Function:
        """
        runningConcurrency(start, end)

        Args:
        - `start` — A column with the start time of events. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `end` — A column with the end time of events. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of concurrent events at each event start time. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("runningConcurrency", *to_args(locals()))
    
    @staticmethod
    def runningDifference(x: Any) -> Function:
        """
        runningDifference(x)

        Args:
        - `x` — Column for which to calculate the running difference. [`Any`](/sql-reference/data-types)

        Returns the difference between consecutive values, with 0 for the first row.
        """
        return Function("runningDifference", *to_args(locals()))
    
    @staticmethod
    def runningDifferenceStartingWithFirstValue(x: Any) -> Function:
        """
        runningDifferenceStartingWithFirstValue(x)

        Args:
        - `x` — Column for which to calculate the running difference. [`Any`](/sql-reference/data-types)

        Returns the difference between consecutive values, with the first row's value for the first row. [`Any`](/sql-reference/data-types)
        """
        return Function("runningDifferenceStartingWithFirstValue", *to_args(locals()))
    
    @staticmethod
    def s2CapContains(center: Any, degrees: Any, point: Any) -> Function:
        """
        s2CapContains(center, degrees, point)

        Args:
        - `center` — S2 cell identifier of the cap center point. [`UInt64`](/sql-reference/data-types/int-uint)
        - `degrees` — Radius of the cap in degrees. [`Float64`](/sql-reference/data-types/float)
        - `point` — S2 cell identifier of the point to test. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns 1 if the cap contains the point and 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("s2CapContains", *to_args(locals()))
    
    @staticmethod
    def s2CapUnion(center1: Any, radius1: Any, center2: Any, radius2: Any) -> Function:
        """
        s2CapUnion(center1, radius1, center2, radius2)

        Args:
        - `center1` — S2 cell identifier of the first cap center. [`UInt64`](/sql-reference/data-types/int-uint)
        - `radius1` — Radius of the first cap in degrees. [`Float64`](/sql-reference/data-types/float)
        - `center2` — S2 cell identifier of the second cap center. [`UInt64`](/sql-reference/data-types/int-uint)
        - `radius2` — Radius of the second cap in degrees. [`Float64`](/sql-reference/data-types/float)

        Returns a tuple (center, radius) representing the smallest cap containing both input caps. [`Tuple(UInt64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("s2CapUnion", *to_args(locals()))
    
    @staticmethod
    def s2CellsIntersect(s2index1: Any, s2index2: Any) -> Function:
        """
        s2CellsIntersect(s2index1, s2index2)

        Args:
        - `s2index1` — First S2 cell identifier. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2index2` — Second S2 cell identifier. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns 1 if the cells intersect and 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("s2CellsIntersect", *to_args(locals()))
    
    @staticmethod
    def s2GetNeighbors(s2index: Any) -> Function:
        """
        s2GetNeighbors(s2index)

        Args:
        - `s2index` — The S2 cell identifier. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of 4 neighbor S2 cell identifiers. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("s2GetNeighbors", *to_args(locals()))
    
    @staticmethod
    def s2RectAdd(s2RectLow: Any, s2RectHigh: Any, s2Point: Any) -> Function:
        """
        s2RectAdd(s2RectLow, s2RectHigh, s2Point)

        Args:
        - `s2RectLow` — S2 cell identifier of the low vertex of the rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2RectHigh` — S2 cell identifier of the high vertex of the rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Point` — S2 cell identifier of the point to add. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple (s2RectLow, s2RectHigh) representing the expanded rectangle. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("s2RectAdd", *to_args(locals()))
    
    @staticmethod
    def s2RectContains(s2RectLow: Any, s2RectHigh: Any, s2Point: Any) -> Function:
        """
        s2RectContains(s2RectLow, s2RectHigh, s2Point)

        Args:
        - `s2RectLow` — S2 cell identifier of the low vertex of the rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2RectHigh` — S2 cell identifier of the high vertex of the rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Point` — S2 cell identifier of the point to test. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns 1 if the rectangle contains the point and 0 otherwise. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("s2RectContains", *to_args(locals()))
    
    @staticmethod
    def s2RectIntersection(s2Rect1Low: Any, s2Rect1High: Any, s2Rect2Low: Any, s2Rect2High: Any) -> Function:
        """
        s2RectIntersection(s2Rect1Low, s2Rect1High, s2Rect2Low, s2Rect2High)

        Args:
        - `s2Rect1Low` — S2 cell identifier of the low vertex of the first rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Rect1High` — S2 cell identifier of the high vertex of the first rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Rect2Low` — S2 cell identifier of the low vertex of the second rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Rect2High` — S2 cell identifier of the high vertex of the second rectangle. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple (s2RectLow, s2RectHigh) representing the intersection rectangle. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("s2RectIntersection", *to_args(locals()))
    
    @staticmethod
    def s2RectUnion(s2Rect1Low: Any, s2Rect1High: Any, s2Rect2Low: Any, s2Rect2High: Any) -> Function:
        """
        s2RectUnion(s2Rect1Low, s2Rect1High, s2Rect2Low, s2Rect2High)

        Args:
        - `s2Rect1Low` — S2 cell identifier of the low vertex of the first rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Rect1High` — S2 cell identifier of the high vertex of the first rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Rect2Low` — S2 cell identifier of the low vertex of the second rectangle. [`UInt64`](/sql-reference/data-types/int-uint)
        - `s2Rect2High` — S2 cell identifier of the high vertex of the second rectangle. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple (s2RectLow, s2RectHigh) representing the union rectangle. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("s2RectUnion", *to_args(locals()))
    
    @staticmethod
    def s2ToGeo(s2index: Any) -> Function:
        """
        s2ToGeo(s2index)

        Args:
        - `s2index` — The S2 cell identifier. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a tuple (lon, lat) of Float64 values representing the longitude and latitude. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("s2ToGeo", *to_args(locals()))
    
    @staticmethod
    def sequenceCount(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("sequenceCount", *to_args(locals()))
    
    @staticmethod
    def sequenceMatch(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("sequenceMatch", *to_args(locals()))
    
    @staticmethod
    def sequenceMatchEvents(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("sequenceMatchEvents", *to_args(locals()))
    
    @staticmethod
    def sequenceNextNode(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("sequenceNextNode", *to_args(locals()))
    
    @staticmethod
    def seriesDecomposeSTL(series: Any, period: Any) -> Function:
        """
        seriesDecomposeSTL(series, period)

        Args:
        - `series` — An array of numeric values [`Array((U)Int8/16/32/64)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `period` — A positive integer [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns an array of four arrays where the first array includes seasonal components, the second array - trend, the third array - residue component, and the fourth array - baseline(seasonal + trend) component. [`Array(Array(Float32), Array(Float32), Array(Float32), Array(Float32))`](/sql-reference/data-types/array)
        """
        return Function("seriesDecomposeSTL", *to_args(locals()))
    
    @staticmethod
    def seriesOutliersDetectTukey(series: Any, min_percentile: Any | None = None, max_percentile: Any | None = None, K: Any | None = None) -> Function:
        """
        seriesOutliersDetectTukey(series[, min_percentile, max_percentile, K])

        Args:
        - `series` — An array of numeric values. [`Array((UInt8/16/32/64))`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)
        - `min_percentile` — Optional. The minimum percentile to be used to calculate inter-quantile range [(IQR)](https://en.wikipedia.org/wiki/Interquartile_range). The value must be in range [0.02,0.98]. The default is 0.25. [`Float*`](/sql-reference/data-types/float)
        - `max_percentile` — Optional. The maximum percentile to be used to calculate inter-quantile range (IQR). The value must be in range [0.02,0.98]. The default is 0.75. [`Float*`](/sql-reference/data-types/float)
        - `K` — Optional. Non-negative constant value to detect mild or stronger outliers. The default value is 1.5. [`Float*`](/sql-reference/data-types/float)

        Returns an array of the same length as the input array where each value represents score of possible anomaly of corresponding element in the series. A non-zero score indicates a possible anomaly. [`Array(Float32)`](/sql-reference/data-types/array)
        """
        return Function("seriesOutliersDetectTukey", *to_args(locals()))
    
    @staticmethod
    def seriesPeriodDetectFFT(series: Any) -> Function:
        """
        seriesPeriodDetectFFT(series)

        Args:
        - `series` — An array of numeric values. [`Array((U)Int8/16/32/64)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns a real value equal to the period of series data. NaN when number of data points are less than four. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("seriesPeriodDetectFFT", *to_args(locals()))
    
    @staticmethod
    def serverTimezone() -> Function:
        """
        serverTimezone()

        
        Returns the server timezone as a [`String`](/sql-reference/data-types/string)
        """
        return Function("serverTimezone", *to_args(locals()))
    
    @staticmethod
    def serverUUID() -> Function:
        """
        serverUUID()

        
        Returns the random UUID of the server. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("serverUUID", *to_args(locals()))
    
    @staticmethod
    def shardCount() -> Function:
        """
        shardCount()

        
        Returns the total number of shards or `0`. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("shardCount", *to_args(locals()))
    
    @staticmethod
    def shardNum() -> Function:
        """
        shardNum()

        
        Returns the shard index or a constant `0`. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("shardNum", *to_args(locals()))
    
    @staticmethod
    def showCertificate() -> Function:
        """
        showCertificate()

        
        Returns map of key-value pairs relating to the configured SSL certificate. [`Map(String, String)`](/sql-reference/data-types/map)
        """
        return Function("showCertificate", *to_args(locals()))
    
    @staticmethod
    def sigmoid(x: Any) -> Function:
        """
        sigmoid(x)

        Args:
        - `x` — The input value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the sigmoid of the input value, in the range (0, 1). [`Float64`](/sql-reference/data-types/float)
        """
        return Function("sigmoid", *to_args(locals()))
    
    @staticmethod
    def sign(x: Any) -> Function:
        """
        sign(x)

        Args:
        - `x` — Values from -∞ to +∞. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal*`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float)

        Returns `-1` for `x < 0`, `0` for `x = 0`, `1` for `x > 0`. [`Int8`](/sql-reference/data-types/int-uint)
        """
        return Function("sign", *to_args(locals()))
    
    @staticmethod
    def simpleJSONExtractBool(json: Any, field_name: Any) -> Function:
        """
        simpleJSONExtractBool(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns `1` if the value of the field is `true`, `0` otherwise. This means this function will return `0` including (and not only) in the following cases:
        - If the field doesn't exists.
        - If the field contains `true` as a string, e.g.: `{"field":"true"}`.
        - If the field contains `1` as a numerical value. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("simpleJSONExtractBool", *to_args(locals()))
    
    @staticmethod
    def simpleJSONExtractFloat(json: Any, field_name: Any) -> Function:
        """
        simpleJSONExtractFloat(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns the number parsed from the field if the field exists and contains a number, otherwise `0`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("simpleJSONExtractFloat", *to_args(locals()))
    
    @staticmethod
    def simpleJSONExtractInt(json: Any, field_name: Any) -> Function:
        """
        simpleJSONExtractInt(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns the number parsed from the field if the field exists and contains a number, `0` otherwise [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("simpleJSONExtractInt", *to_args(locals()))
    
    @staticmethod
    def simpleJSONExtractRaw(json: Any, field_name: Any) -> Function:
        """
        simpleJSONExtractRaw(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns the value of the field as a string, including separators if the field exists, or an empty string otherwise [`String`](/sql-reference/data-types/string)
        """
        return Function("simpleJSONExtractRaw", *to_args(locals()))
    
    @staticmethod
    def simpleJSONExtractString(json: Any, field_name: Any) -> Function:
        """
        simpleJSONExtractString(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns the unescaped value of a field as a string, including separators. An empty string is returned if the field doesn't contain a double quoted string, if unescaping fails or if the field doesn't exist [`String`](/sql-reference/data-types/string)
        """
        return Function("simpleJSONExtractString", *to_args(locals()))
    
    @staticmethod
    def simpleJSONExtractUInt(json: Any, field_name: Any) -> Function:
        """
        simpleJSONExtractUInt(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns the number parsed from the field if the field exists and contains a number, `0` otherwise [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("simpleJSONExtractUInt", *to_args(locals()))
    
    @staticmethod
    def simpleJSONHas(json: Any, field_name: Any) -> Function:
        """
        simpleJSONHas(json, field_name)

        Args:
        - `json` — The JSON in which the field is searched for. [`String`](/sql-reference/data-types/string)
        - `field_name` — The name of the field to search for. [`const String`](/sql-reference/data-types/string)

        Returns `1` if the field exists, `0` otherwise [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("simpleJSONHas", *to_args(locals()))
    
    @staticmethod
    def simpleLinearRegression(x: Any, y: Any) -> Function:
        """
        simpleLinearRegression(x, y)

        Args:
        - `x` — Column with explanatory variable values. [`Float64`](/sql-reference/data-types/float)
        - `y` — Column with dependent variable values. [`Float64`](/sql-reference/data-types/float)

        Returns constants `(k, b)` of the resulting line `y = k*x + b`. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("simpleLinearRegression", *to_args(locals()))
    
    @staticmethod
    def sin(x: Any) -> Function:
        """
        sin(x)

        Args:
        - `x` — The number whose sine will be returned. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the sine of x.
        """
        return Function("sin", *to_args(locals()))
    
    @staticmethod
    def singleValueOrNull(x: Any) -> Function:
        """
        singleValueOrNull(x)

        Args:
        - `x` — A column of any data type except Map, Array or Tuple which cannot be of type Nullable. [`Any`](/sql-reference/data-types)

        Returns the unique value if there is only one unique non-NULL value in `x`. Returns `NULL` if there are zero or at least two distinct values. [`Any`](/sql-reference/data-types) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("singleValueOrNull", *to_args(locals()))
    
    @staticmethod
    def sinh(x: Any) -> Function:
        """
        sinh(x)

        Args:
        - `x` — The angle, in radians. Values from the interval: -∞ < x < +∞. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns values from the interval: -∞ < sinh(x) < +∞ [`Float64`](/sql-reference/data-types/float)
        """
        return Function("sinh", *to_args(locals()))
    
    @staticmethod
    def sipHash128(arg1: Any, arg2: Any | None = None) -> Function:
        """
        sipHash128(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns a 128-bit `SipHash` hash value. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("sipHash128", *to_args(locals()))
    
    @staticmethod
    def sipHash128Keyed(k0: Any, k1: Any) -> Function:
        """
        sipHash128Keyed((k0, k1), [arg1, arg2, ...])

        Args:
        - `(k0, k1)` — A tuple of two UInt64 values representing the key. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        A 128-bit `SipHash` hash value of type [FixedString(16)](../data-types/fixedstring.md). [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("sipHash128Keyed", *to_args(locals()))
    
    @staticmethod
    def sipHash128Reference(arg1: Any, arg2: Any | None = None) -> Function:
        """
        sipHash128Reference(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed 128-bit `SipHash` hash value of the input arguments. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("sipHash128Reference", *to_args(locals()))
    
    @staticmethod
    def sipHash128ReferenceKeyed(k0: Any, k1: Any) -> Function:
        """
        sipHash128ReferenceKeyed((k0, k1), arg1[, arg2, ...])

        Args:
        - `(k0, k1)` — Tuple of two values representing the key [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        - `arg1[, arg2, ...]` — A variable number of input arguments for which to compute the hash. [`Any`](/sql-reference/data-types)

        Returns the computed 128-bit `SipHash` hash value of the input arguments. [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        """
        return Function("sipHash128ReferenceKeyed", *to_args(locals()))
    
    @staticmethod
    def sipHash64(arg1: Any, arg2: Any | None = None) -> Function:
        """
        sipHash64(arg1[, arg2, ...])

        Args:
        - `arg1[, arg2, ...]` — A variable number of input arguments. [`Any`](/sql-reference/data-types)

        Returns a computed hash value of the input arguments. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("sipHash64", *to_args(locals()))
    
    @staticmethod
    def sipHash64Keyed(k0: Any, k1: Any) -> Function:
        """
        sipHash64Keyed((k0, k1), arg1[,arg2, ...])

        Args:
        - `(k0, k1)` — A tuple of two values representing the key. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        - `arg1[,arg2, ...]` — A variable number of input arguments. [`Any`](/sql-reference/data-types)

        Returns the computed hash of the input values. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("sipHash64Keyed", *to_args(locals()))
    
    @staticmethod
    def skewPop(expr: Any) -> Function:
        """
        skewPop(expr)

        Args:
        - `expr` — An expression returning a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns the skewness of the given distribution. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("skewPop", *to_args(locals()))
    
    @staticmethod
    def skewSamp(expr: Any) -> Function:
        """
        skewSamp(expr)

        Args:
        - `expr` — An expression returning a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns the skewness of the given distribution. If `n <= 1` (`n` is the size of the sample), then the function returns `nan`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("skewSamp", *to_args(locals()))
    
    @staticmethod
    def sleep(seconds: Any) -> Function:
        """
        sleep(seconds)

        Args:
        - `seconds` — The number of seconds to pause the query execution to a maximum of 3 seconds. It can be a floating-point value to specify fractional seconds. [`const UInt*`](/sql-reference/data-types/int-uint) or [`const Float*`](/sql-reference/data-types/float)

        Returns `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("sleep", *to_args(locals()))
    
    @staticmethod
    def sleepEachRow(seconds: Any) -> Function:
        """
        sleepEachRow(seconds)

        Args:
        - `seconds` — The number of seconds to pause the query execution for each row in the result set to a maximum of 3 seconds. It can be a floating-point value to specify fractional seconds. [`const UInt*`](/sql-reference/data-types/int-uint) or [`const Float*`](/sql-reference/data-types/float)

        Returns `0` for each row. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("sleepEachRow", *to_args(locals()))
    
    @staticmethod
    def snowflakeIDToDateTime(value: Any, epoch: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        snowflakeIDToDateTime(value[, epoch[, time_zone]])

        Args:
        - `value` — Snowflake ID. [`UInt64`](/sql-reference/data-types/int-uint)
        - `epoch` — Optional. Epoch of the Snowflake ID in milliseconds since 1970-01-01. Defaults to 0 (1970-01-01). For the Twitter/X epoch (2015-01-01), provide 1288834974657. [`UInt*`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. [Timezone](/operations/server-configuration-parameters/settings.md#timezone). The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns the timestamp component of `value`. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("snowflakeIDToDateTime", *to_args(locals()))
    
    @staticmethod
    def snowflakeIDToDateTime64(value: Any, epoch: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        snowflakeIDToDateTime64(value[, epoch[, time_zone]])

        Args:
        - `value` — Snowflake ID. [`UInt64`](/sql-reference/data-types/int-uint)
        - `epoch` — Optional. Epoch of the Snowflake ID in milliseconds since 1970-01-01. Defaults to 0 (1970-01-01). For the Twitter/X epoch (2015-01-01), provide 1288834974657. [`UInt*`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. [Timezone](/operations/server-configuration-parameters/settings.md#timezone). The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns the timestamp component of `value` as a `DateTime64` with scale = 3, i.e. millisecond precision. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("snowflakeIDToDateTime64", *to_args(locals()))
    
    @staticmethod
    def snowflakeToDateTime(value: Any, time_zone: Any | None = None) -> Function:
        """
        snowflakeToDateTime(value[, time_zone])

        Args:
        - `value` — Snowflake ID. [`Int64`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. [Timezone](/operations/server-configuration-parameters/settings.md#timezone). The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns the timestamp component of `value`. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("snowflakeToDateTime", *to_args(locals()))
    
    @staticmethod
    def snowflakeToDateTime64(value: Any, time_zone: Any | None = None) -> Function:
        """
        snowflakeToDateTime64(value[, time_zone])

        Args:
        - `value` — Snowflake ID. [`Int64`](/sql-reference/data-types/int-uint)
        - `time_zone` — Optional. [Timezone](/operations/server-configuration-parameters/settings.md#timezone). The function parses `time_string` according to the timezone. [`String`](/sql-reference/data-types/string)

        Returns the timestamp component of `value`. [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("snowflakeToDateTime64", *to_args(locals()))
    
    @staticmethod
    def soundex(s: Any) -> Function:
        """
        soundex(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns the Soundex code of the input string. [`String`](/sql-reference/data-types/string)
        """
        return Function("soundex", *to_args(locals()))
    
    @staticmethod
    def space(n: Any) -> Function:
        """
        space(n)

        Args:
        - `n` — The number of times to repeat the space. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns astring containing a space repeated `n` times. If `n <= 0`, the function returns the empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("space", *to_args(locals()))
    
    @staticmethod
    def sparkbar(buckets: Any, min_x: Any | None = None, max_x: Any | None = None) -> Function:
        """
        sparkbar(buckets[, min_x, max_x])(x, y)

        Args:
        - `x` — The field with values. [`const String`](/sql-reference/data-types/string)
        - `y` — The field with the frequency of values. [`const String`](/sql-reference/data-types/string)

        Returns the frequency histogram. [`String`](/sql-reference/data-types/string)
        """
        return Function("sparkbar", *to_args(locals()))
    
    @staticmethod
    def sparseGrams(s: Any, min_ngram_length: Any | None = None, max_ngram_length: Any | None = None) -> Function:
        """
        sparseGrams(s[, min_ngram_length, max_ngram_length])

        Args:
        - `s` — An input string. [`String`](/sql-reference/data-types/string)
        - `min_ngram_length` — Optional. The minimum length of extracted ngram. The default and minimal value is 3. [`UInt*`](/sql-reference/data-types/int-uint)
        - `max_ngram_length` — Optional. The maximum length of extracted ngram. The default value is 100. Should be not less than `min_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)
        - `min_cutoff_length` — Optional. If specified, only n-grams with length greater or equal than `min_cutoff_length` are returned. The default value is the same as `min_ngram_length`. Should be not less than `min_ngram_length` and not greater than `max_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an array of selected substrings. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("sparseGrams", *to_args(locals()))
    
    @staticmethod
    def sparseGramsHashes(s: Any, min_ngram_length: Any | None = None, max_ngram_length: Any | None = None) -> Function:
        """
        sparseGramsHashes(s[, min_ngram_length, max_ngram_length])

        Args:
        - `s` — An input string. [`String`](/sql-reference/data-types/string)
        - `min_ngram_length` — Optional. The minimum length of extracted ngram. The default and minimal value is 3. [`UInt*`](/sql-reference/data-types/int-uint)
        - `max_ngram_length` — Optional. The maximum length of extracted ngram. The default value is 100. Should be not less than `min_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)
        - `min_cutoff_length` — Optional. If specified, only n-grams with length greater or equal than `min_cutoff_length` are returned. The default value is the same as `min_ngram_length`. Should be not less than `min_ngram_length` and not greater than `max_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an array of selected substrings CRC32 hashes. [`Array(UInt32)`](/sql-reference/data-types/array)
        """
        return Function("sparseGramsHashes", *to_args(locals()))
    
    @staticmethod
    def sparseGramsHashesUTF8(s: Any, min_ngram_length: Any | None = None, max_ngram_length: Any | None = None) -> Function:
        """
        sparseGramsHashesUTF8(s[, min_ngram_length, max_ngram_length])

        Args:
        - `s` — An input string. [`String`](/sql-reference/data-types/string)
        - `min_ngram_length` — Optional. The minimum length of extracted ngram. The default and minimal value is 3. [`UInt*`](/sql-reference/data-types/int-uint)
        - `max_ngram_length` — Optional. The maximum length of extracted ngram. The default value is 100. Should be not less than `min_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)
        - `min_cutoff_length` — Optional. If specified, only n-grams with length greater or equal than `min_cutoff_length` are returned. The default value is the same as `min_ngram_length`. Should be not less than `min_ngram_length` and not greater than `max_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an array of selected UTF-8 substrings CRC32 hashes. [`Array(UInt32)`](/sql-reference/data-types/array)
        """
        return Function("sparseGramsHashesUTF8", *to_args(locals()))
    
    @staticmethod
    def sparseGramsUTF8(s: Any, min_ngram_length: Any | None = None, max_ngram_length: Any | None = None) -> Function:
        """
        sparseGramsUTF8(s[, min_ngram_length, max_ngram_length])

        Args:
        - `s` — An input string. [`String`](/sql-reference/data-types/string)
        - `min_ngram_length` — Optional. The minimum length of extracted ngram. The default and minimal value is 3. [`UInt*`](/sql-reference/data-types/int-uint)
        - `max_ngram_length` — Optional. The maximum length of extracted ngram. The default value is 100. Should be not less than `min_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)
        - `min_cutoff_length` — Optional. If specified, only n-grams with length greater or equal than `min_cutoff_length` are returned. The default value is the same as `min_ngram_length`. Should be not less than `min_ngram_length` and not greater than `max_ngram_length`. [`UInt*`](/sql-reference/data-types/int-uint)

        Returns an array of selected UTF-8 substrings. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("sparseGramsUTF8", *to_args(locals()))
    
    @staticmethod
    def splitByChar(separator: Any, s: Any, max_substrings: Any | None = None) -> Function:
        """
        splitByChar(separator, s[, max_substrings])

        Args:
        - `separator` — The separator must be a single-byte character. [`String`](/sql-reference/data-types/string)
        - `s` — The string to split. [`String`](/sql-reference/data-types/string)
        - `max_substrings` — Optional. If `max_substrings > 0`, the returned array will contain at most `max_substrings` substrings, otherwise the function will return as many substrings as possible. The default value is `0`.  [`Int64`](/sql-reference/data-types/int-uint)

        Returns an array of selected substrings. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("splitByChar", *to_args(locals()))
    
    @staticmethod
    def splitByNonAlpha(s: Any, max_substrings: Any | None = None) -> Function:
        """
        splitByNonAlpha(s[, max_substrings])

        Args:
        - `s` — The string to split. [`String`](/sql-reference/data-types/string)
        - `max_substrings` — Optional. When `max_substrings > 0`, the returned substrings will be no more than `max_substrings`, otherwise the function will return as many substrings as possible. Default value: `0`. [`Int64`](/sql-reference/data-types/int-uint)

        Returns an array of selected substrings of `s`. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("splitByNonAlpha", *to_args(locals()))
    
    @staticmethod
    def splitByRegexp(regexp: Any, s: Any, max_substrings: Any | None = None) -> Function:
        """
        splitByRegexp(regexp, s[, max_substrings])

        Args:
        - `regexp` — Regular expression. Constant. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `s` — The string to split. [`String`](/sql-reference/data-types/string)
        - `max_substrings` — Optional. When `max_substrings > 0`, the returned substrings will be no more than `max_substrings`, otherwise the function will return as many substrings as possible. Default value: `0`. [`Int64`](/sql-reference/data-types/int-uint)

        Returns an array of the selected substrings of `s`. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("splitByRegexp", *to_args(locals()))
    
    @staticmethod
    def splitByString(separator: Any, s: Any, max_substrings: Any | None = None) -> Function:
        """
        splitByString(separator, s[, max_substrings])

        Args:
        - `separator` — The separator. [`String`](/sql-reference/data-types/string)
        - `s` — The string to split. [`String`](/sql-reference/data-types/string)
        - `max_substrings` — Optional. When `max_substrings > 0`, the returned substrings will be no more than `max_substrings`, otherwise the function will return as many substrings as possible. Default value: `0`. [`Int64`](/sql-reference/data-types/int-uint)

        Returns an array of selected substrings of `s` [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("splitByString", *to_args(locals()))
    
    @staticmethod
    def splitByWhitespace(s: Any, max_substrings: Any | None = None) -> Function:
        """
        splitByWhitespace(s[, max_substrings])

        Args:
        - `s` — The string to split. [`String`](/sql-reference/data-types/string)
        - `max_substrings` — Optional. When `max_substrings > 0`, the returned substrings will be no more than `max_substrings`, otherwise the function will return as many substrings as possible. Default value: `0`. [`Int64`](/sql-reference/data-types/int-uint)

        Returns an array of the selected substrings of `s`. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("splitByWhitespace", *to_args(locals()))
    
    @staticmethod
    def sqidDecode(sqid: Any) -> Function:
        """
        sqidDecode(sqid)

        Args:
        - `sqid` — The sqid to decode. [`String`](/sql-reference/data-types/string)

        Returns an array of numbers from `sqid`. [`Array(UInt64)`](/sql-reference/data-types/array)
        """
        return Function("sqidDecode", *to_args(locals()))
    
    @staticmethod
    def sqidEncode(n1: Any, n2: Any | None = None) -> Function:
        """
        sqidEncode(n1[, n2, ...])

        Args:
        - `n1[, n2, ...]` — Arbitrarily many numbers. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns a hash ID [`String`](/sql-reference/data-types/string)
        """
        return Function("sqidEncode", *to_args(locals()))
    
    @staticmethod
    def sqrt(x: Any) -> Function:
        """
        sqrt(x)

        Args:
        - `x` — The number for which to find the square root of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the square root of x [`Float*`](/sql-reference/data-types/float)
        """
        return Function("sqrt", *to_args(locals()))
    
    @staticmethod
    def startsWith(s: Any, prefix: Any) -> Function:
        """
        startsWith(s, prefix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `prefix` — Prefix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` starts with `prefix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("startsWith", *to_args(locals()))
    
    @staticmethod
    def startsWithCaseInsensitive(s: Any, prefix: Any) -> Function:
        """
        startsWithCaseInsensitive(s, prefix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `prefix` — Case-insensitive prefix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` starts with case-insensitive `prefix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("startsWithCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def startsWithCaseInsensitiveUTF8(s: Any, prefix: Any) -> Function:
        """
        startsWithCaseInsensitiveUTF8(s, prefix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `prefix` — Case-insensitive prefix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` starts with case-insensitive `prefix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("startsWithCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def startsWithUTF8(s: Any, prefix: Any) -> Function:
        """
        startsWithUTF8(s, prefix)

        Args:
        - `s` — String to check. [`String`](/sql-reference/data-types/string)
        - `prefix` — Prefix to check for. [`String`](/sql-reference/data-types/string)

        Returns `1` if `s` starts with `prefix`, otherwise `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("startsWithUTF8", *to_args(locals()))
    
    @staticmethod
    def stddevPop(x: Any) -> Function:
        """
        stddevPop(x)

        Args:
        - `x` — Population of values to find the standard deviation of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the square root of population variance of `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stddevPop", *to_args(locals()))
    
    @staticmethod
    def stddevPopStable(x: Any) -> Function:
        """
        stddevPopStable(x)

        Args:
        - `x` — Population of values to find the standard deviation of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the square root of the variance of `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stddevPopStable", *to_args(locals()))
    
    @staticmethod
    def stddevSamp(x: Any) -> Function:
        """
        stddevSamp(x)

        Args:
        - `x` — Values for which to find the square root of sample variance. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the square root of sample variance of `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stddevSamp", *to_args(locals()))
    
    @staticmethod
    def stddevSampStable(x: Any) -> Function:
        """
        stddevSampStable(x)

        Args:
        - `x` — Values for which to find the square root of sample variance. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the square root of sample variance of `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stddevSampStable", *to_args(locals()))
    
    @staticmethod
    def stem(lang: Any, word: Any) -> Function:
        """
        stem(lang, word)

        Args:
        - `lang` — Language which rules will be applied. Use the two letter ISO 639-1 code. [`String`](/sql-reference/data-types/string)
        - `word` — Lowercase word that needs to be stemmed. [`String`](/sql-reference/data-types/string)

        Returns the stemmed form of the word [`String`](/sql-reference/data-types/string)
        """
        return Function("stem", *to_args(locals()))
    
    @staticmethod
    def stochasticLinearRegression(learning_rate: Any | None = None, l2_regularization_coef: Any | None = None, mini_batch_size: Any | None = None, method: Any | None = None) -> Function:
        """
        stochasticLinearRegression([learning_rate, l2_regularization_coef, mini_batch_size, method])(target, x1, x2, ...)

        Args:
        - `learning_rate` — The coefficient on step length when gradient descent step is performed. A learning rate that is too big may cause infinite weights of the model. Default is `0.00001`. [`Float64`](/sql-reference/data-types/float)
        - `l2_regularization_coef` — L2 regularization coefficient which may help to prevent overfitting. Default is `0.1`. [`Float64`](/sql-reference/data-types/float)
        - `mini_batch_size` — Sets the number of elements which gradients will be computed and summed to perform one step of gradient descent. Pure stochastic descent uses one element, however having small batches (about 10 elements) makes gradient steps more stable. Default is `15`. [`UInt64`](/sql-reference/data-types/int-uint)
        - `method` — Method for updating weights: `Adam` (by default), `SGD`, `Momentum`, `Nesterov`. `Momentum` and `Nesterov` require slightly more computations and memory, however they happen to be useful in terms of speed of convergence and stability of stochastic gradient methods. [`const String`](/sql-reference/data-types/string)
        - `target` — Target value (dependent variable) to learn to predict. Must be numeric. [`Float*`](/sql-reference/data-types/float)
        - `x1, x2, ...` — Feature values (independent variables). All must be numeric. [`Float*`](/sql-reference/data-types/float)

        Returns the trained linear regression model weights. First values correspond to the parameters of the model, the last one is bias. Use `evalMLMethod` for predictions. [`Array(Float64)`](/sql-reference/data-types/array)
        """
        return Function("stochasticLinearRegression", *to_args(locals()))
    
    @staticmethod
    def stochasticLogisticRegression(learning_rate: Any | None = None, l2_regularization_coef: Any | None = None, mini_batch_size: Any | None = None, method: Any | None = None) -> Function:
        """
        stochasticLogisticRegression([learning_rate, l2_regularization_coef, mini_batch_size, method])(target, x1, x2, ...)

        Args:
        - `learning_rate` — The coefficient on step length when gradient descent step is performed. A learning rate that is too big may cause infinite weights of the model. Default is `0.00001`. [`Float64`](/sql-reference/data-types/float)
        - `l2_regularization_coef` — L2 regularization coefficient which may help to prevent overfitting. Default is `0.1`. [`Float64`](/sql-reference/data-types/float)
        - `mini_batch_size` — Sets the number of elements which gradients will be computed and summed to perform one step of gradient descent. Pure stochastic descent uses one element, however having small batches (about 10 elements) makes gradient steps more stable. Default is `15`. [`UInt64`](/sql-reference/data-types/int-uint)
        - `method` — Method for updating weights: `Adam` (by default), `SGD`, `Momentum`, `Nesterov`. `Momentum` and `Nesterov` require a little bit more computations and memory, however they happen to be useful in terms of speed of convergence and stability of stochastic gradient methods. [`String`](/sql-reference/data-types/string)
        - `target` — Target binary classification labels. Must be in range [-1, 1]. [`Float`](/sql-reference/data-types/float)
        - `x1, x2, ...` — Feature values (independent variables). All must be numeric. [`Float`](/sql-reference/data-types/float)

        Returns the trained logistic regression model weights. Use `evalMLMethod` for predictions which returns probabilities of object having label `1`. [`Array(Float64)`](/sql-reference/data-types/array)
        """
        return Function("stochasticLogisticRegression", *to_args(locals()))
    
    @staticmethod
    def stringBytesEntropy(s: Any) -> Function:
        """
        stringBytesEntropy(s)

        Args:
        - `s` — The string to analyze. [`String`](/sql-reference/data-types/string)

        Returns Shannon's entropy of byte distribution in the string. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stringBytesEntropy", *to_args(locals()))
    
    @staticmethod
    def stringBytesUniq(s: Any) -> Function:
        """
        stringBytesUniq(s)

        Args:
        - `s` — The string to analyze. [`String`](/sql-reference/data-types/string)

        Returns the number of distinct bytes in the string. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("stringBytesUniq", *to_args(locals()))
    
    @staticmethod
    def stringJaccardIndex(s1: Any, s2: Any) -> Function:
        """
        stringJaccardIndex(s1, s2)

        Args:
        - `s1` — First input string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input string. [`String`](/sql-reference/data-types/string)

        Returns the Jaccard similarity index between the two strings. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stringJaccardIndex", *to_args(locals()))
    
    @staticmethod
    def stringJaccardIndexUTF8(s1: Any, s2: Any) -> Function:
        """
        stringJaccardIndexUTF8(s1, s2)

        Args:
        - `s1` — First input UTF8 string. [`String`](/sql-reference/data-types/string)
        - `s2` — Second input UTF8 string. [`String`](/sql-reference/data-types/string)

        Returns the Jaccard similarity index between the two UTF8 strings. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("stringJaccardIndexUTF8", *to_args(locals()))
    
    @staticmethod
    def stringToH3(index_str: Any) -> Function:
        """
        stringToH3(index_str)

        Args:
        - `index_str` — String representation of the H3 index. [`String`](/sql-reference/data-types/string)

        Returns the H3 index number, or `0` if the input is not a valid H3 index. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("stringToH3", *to_args(locals()))
    
    @staticmethod
    def structureToCapnProtoSchema(table_structure: Any, message: Any) -> Function:
        """
        structureToCapnProtoSchema(table_structure, message)

        
        
        """
        return Function("structureToCapnProtoSchema", *to_args(locals()))
    
    @staticmethod
    def structureToProtobufSchema(structure: Any, message_name: Any) -> Function:
        """
        structureToProtobufSchema(structure, message_name)

        Args:
        - `structure` — ClickHouse table structure definition as a string (e.g., 'column1 Type1, column2 Type2'). [`String`](/sql-reference/data-types/string)
        - `message_name` — Name for the Protobuf message type in the generated schema. [`String`](/sql-reference/data-types/string)

        Returns a Protobuf schema definition in proto3 syntax that corresponds to the input ClickHouse structure. [`String`](/sql-reference/data-types/string)
        """
        return Function("structureToProtobufSchema", *to_args(locals()))
    
    @staticmethod
    def studentTTest(confidence_level: Any | None = None) -> Function:
        """
        studentTTest([confidence_level])(sample_data, sample_index)

        Args:
        - `sample_data` — Sample data. [`Integer`](/sql-reference/data-types/int-uint) or [`Float`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `sample_index` — Sample index. [`Integer`](/sql-reference/data-types/int-uint)

        Returns a tuple with two or four elements (if the optional `confidence_level` is specified): calculated t-statistic, calculated p-value, [calculated confidence-interval-low], [calculated confidence-interval-high]. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple) or [`Tuple(Float64, Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("studentTTest", *to_args(locals()))
    
    @staticmethod
    def studentTTestOneSample(confidence_level: Any | None = None) -> Function:
        """
        studentTTestOneSample([confidence_level])(sample_data, population_mean)

        Args:
        - `sample_data` — Sample data. [`Integer`](/sql-reference/data-types/int-uint) or [`Float`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `population_mean` — Known population mean to test against (usually a constant). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple with two or four elements (if `confidence_level` is specified): calculated t-statistic, calculated p-value (two-tailed), [calculated confidence-interval-low], [calculated confidence-interval-high]. Confidence intervals are for the sample mean at the given confidence level. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple) or [`Tuple(Float64, Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("studentTTestOneSample", *to_args(locals()))
    
    @staticmethod
    def subBitmap(bitmap: Any, offset: Any, cardinality_limit: Any) -> Function:
        """
        subBitmap(bitmap, offset, cardinality_limit)

        Args:
        - `bitmap` — Bitmap object. [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction). - `offset` — Number of set bits to skip from the beginning (zero-based). [`UInt32`](/sql-reference/data-types/int-uint) - `cardinality_limit` — Maximum number of set bits to include in the subset. [`UInt32`](/sql-reference/data-types/int-uint) 
        Returns a bitmap containing at most `limit` set bits, starting after skipping `offset` set bits in ascending order [`AggregateFunction(groupBitmap, T)`](/sql-reference/data-types/aggregatefunction)
        """
        return Function("subBitmap", *to_args(locals()))
    
    @staticmethod
    def subDate(datetime: Any, interval: Any) -> Function:
        """
        subDate(datetime, interval)

        Args:
        - `datetime` — The date or date with time from which `interval` is subtracted. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `interval` — Interval to subtract. [`Interval`](/sql-reference/data-types/int-uint)

        Returns date or date with time obtained by subtracting `interval` from `datetime`. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subDate", *to_args(locals()))
    
    @staticmethod
    def substring(s: Any, offset: Any, length: Any | None = None) -> Function:
        """
        substring(s, offset[, length])

        Args:
        - `s` — The string to calculate a substring from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Enum`](/sql-reference/data-types/enum)
        - `offset` — The starting position of the substring in `s`. [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `length` — Optional. The maximum length of the substring. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a substring of `s` with `length` many bytes, starting at index `offset`. [`String`](/sql-reference/data-types/string)
        """
        return Function("substring", *to_args(locals()))
    
    @staticmethod
    def substringIndex(s: Any, delim: Any, count: Any) -> Function:
        """
        substringIndex(s, delim, count)

        Args:
        - `s` — The string to extract substring from. [`String`](/sql-reference/data-types/string)
        - `delim` — The character to split. [`String`](/sql-reference/data-types/string)
        - `count` — The number of occurrences of the delimiter to count before extracting the substring. If count is positive, everything to the left of the final delimiter (counting from the left) is returned. If count is negative, everything to the right of the final delimiter (counting from the right) is returned. [`UInt`](/sql-reference/data-types/int-uint) or [`Int`](/sql-reference/data-types/int-uint)

        Returns a substring of `s` before `count` occurrences of `delim`. [`String`](/sql-reference/data-types/string)
        """
        return Function("substringIndex", *to_args(locals()))
    
    @staticmethod
    def substringIndexUTF8(s: Any, delim: Any, count: Any) -> Function:
        """
        substringIndexUTF8(s, delim, count)

        Args:
        - `s` — The string to extract substring from. [`String`](/sql-reference/data-types/string)
        - `delim` — The character to split. [`String`](/sql-reference/data-types/string)
        - `count` — The number of occurrences of the delimiter to count before extracting the substring. If count is positive, everything to the left of the final delimiter (counting from the left) is returned. If count is negative, everything to the right of the final delimiter (counting from the right) is returned. [`UInt`](/sql-reference/data-types/int-uint) or [`Int`](/sql-reference/data-types/int-uint)

        Returns a substring of `s` before `count` occurrences of `delim`. [`String`](/sql-reference/data-types/string)
        """
        return Function("substringIndexUTF8", *to_args(locals()))
    
    @staticmethod
    def substringUTF8(s: Any, offset: Any, length: Any | None = None) -> Function:
        """
        substringUTF8(s, offset[, length])

        Args:
        - `s` — The string to calculate a substring from. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Enum`](/sql-reference/data-types/enum)
        - `offset` — The starting position of the substring in `s`. [`Int`](/sql-reference/data-types/int-uint) or [`UInt`](/sql-reference/data-types/int-uint)
        - `length` — The maximum length of the substring. Optional. [`Int`](/sql-reference/data-types/int-uint) or [`UInt`](/sql-reference/data-types/int-uint)

        Returns a substring of `s` with `length` many code points, starting at code point index `offset`. [`String`](/sql-reference/data-types/string)
        """
        return Function("substringUTF8", *to_args(locals()))
    
    @staticmethod
    def subtractDays(datetime: Any, num: Any) -> Function:
        """
        subtractDays(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of days from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of days to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` days [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractDays", *to_args(locals()))
    
    @staticmethod
    def subtractHours(datetime: Any, num: Any) -> Function:
        """
        subtractHours(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of hours from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of hours to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` hours [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractHours", *to_args(locals()))
    
    @staticmethod
    def subtractInterval(interval_1: Any, interval_2: Any) -> Function:
        """
        subtractInterval(interval_1, interval_2)

        Args:
        - `interval_1` — First interval or interval of tuples. [`Interval`](/sql-reference/data-types/int-uint) or [`Tuple(Interval)`](/sql-reference/data-types/tuple)
        - `interval_2` — Second interval to be negated. [`Interval`](/sql-reference/data-types/int-uint)

        Returns a tuple of intervals [`Tuple(T)`](/sql-reference/data-types/tuple)
        """
        return Function("subtractInterval", *to_args(locals()))
    
    @staticmethod
    def subtractMicroseconds(datetime: Any, num: Any) -> Function:
        """
        subtractMicroseconds(datetime, num)

        Args:
        - `datetime` — Date with time to subtract specified number of microseconds from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of microseconds to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` microseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractMicroseconds", *to_args(locals()))
    
    @staticmethod
    def subtractMilliseconds(datetime: Any, num: Any) -> Function:
        """
        subtractMilliseconds(datetime, num)

        Args:
        - `datetime` — Date with time to subtract specified number of milliseconds from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of milliseconds to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` milliseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractMilliseconds", *to_args(locals()))
    
    @staticmethod
    def subtractMinutes(datetime: Any, num: Any) -> Function:
        """
        subtractMinutes(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of minutes from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of minutes to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` minutes [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractMinutes", *to_args(locals()))
    
    @staticmethod
    def subtractMonths(datetime: Any, num: Any) -> Function:
        """
        subtractMonths(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of months from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of months to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` months [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractMonths", *to_args(locals()))
    
    @staticmethod
    def subtractNanoseconds(datetime: Any, num: Any) -> Function:
        """
        subtractNanoseconds(datetime, num)

        Args:
        - `datetime` — Date with time to subtract specified number of nanoseconds from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of nanoseconds to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` nanoseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractNanoseconds", *to_args(locals()))
    
    @staticmethod
    def subtractQuarters(datetime: Any, num: Any) -> Function:
        """
        subtractQuarters(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of quarters from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of quarters to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` quarters [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractQuarters", *to_args(locals()))
    
    @staticmethod
    def subtractSeconds(datetime: Any, num: Any) -> Function:
        """
        subtractSeconds(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of seconds from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of seconds to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` seconds [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64(3)`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractSeconds", *to_args(locals()))
    
    @staticmethod
    def subtractTupleOfIntervals(datetime: Any, intervals: Any) -> Function:
        """
        subtractTupleOfIntervals(datetime, intervals)

        Args:
        - `datetime` — Date or date with time to subtract intervals from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `intervals` — Tuple of intervals to subtract from `datetime`. [`Tuple(Interval)`](/sql-reference/data-types/tuple)

        Returns `date` with subtracted `intervals` [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractTupleOfIntervals", *to_args(locals()))
    
    @staticmethod
    def subtractWeeks(datetime: Any, num: Any) -> Function:
        """
        subtractWeeks(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of weeks from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of weeks to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` weeks [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractWeeks", *to_args(locals()))
    
    @staticmethod
    def subtractYears(datetime: Any, num: Any) -> Function:
        """
        subtractYears(datetime, num)

        Args:
        - `datetime` — Date or date with time to subtract specified number of years from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `num` — Number of years to subtract. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns `datetime` minus `num` years [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("subtractYears", *to_args(locals()))
    
    @staticmethod
    def sum(num: Any) -> Function:
        """
        sum(num)

        Args:
        - `num` — Column of numeric values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the sum of the values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        """
        return Function("sum", *to_args(locals()))
    
    @staticmethod
    def sumCount(x: Any) -> Function:
        """
        sumCount(x)

        Args:
        - `x` — Input value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple `(sum, count)`, where `sum` is the sum of numbers and `count` is the number of rows with not-NULL values. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("sumCount", *to_args(locals()))
    
    @staticmethod
    def sumKahan(x: Any) -> Function:
        """
        sumKahan(x)

        Args:
        - `x` — Input value. [`Integer`](/sql-reference/data-types/int-uint) or [`Float`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the sum of numbers. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        """
        return Function("sumKahan", *to_args(locals()))
    
    @staticmethod
    def sumMapFiltered(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("sumMapFiltered", *to_args(locals()))
    
    @staticmethod
    def sumMapFilteredWithOverflow(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("sumMapFilteredWithOverflow", *to_args(locals()))
    
    @staticmethod
    def sumMapWithOverflow(key: Any, value: Any) -> Function:
        """
        sumMapWithOverflow(key, value)
        sumMapWithOverflow(Tuple(key, value))

        Args:
        - `key` — Array of keys. [`Array`](/sql-reference/data-types/array)
        - `value` — Array of values. [`Array`](/sql-reference/data-types/array)

        Returns a tuple of two arrays: keys in sorted order, and values summed for the corresponding keys. [`Tuple(Array, Array)`](/sql-reference/data-types/tuple)
        """
        return Function("sumMapWithOverflow", *to_args(locals()))
    
    @staticmethod
    def sumMappedArrays(key: Any, value1: Any, value2: Any | None = None) -> Function:
        """
        sumMappedArrays(key, value1 [, value2, ...])
        sumMappedArrays(Tuple(key, value1 [, value2, ...]))

        Args:
        - `key` — Array of keys. [`Array`](/sql-reference/data-types/array)
        - `value1, value2, ...` — Arrays of values to sum for each key. [`Array`](/sql-reference/data-types/array)

        Returns a tuple of arrays: the first array contains keys in sorted order, followed by arrays containing values summed for the corresponding keys. [`Tuple`](/sql-reference/data-types/tuple)
        """
        return Function("sumMappedArrays", *to_args(locals()))
    
    @staticmethod
    def sumWithOverflow(num: Any) -> Function:
        """
        sumWithOverflow(num)

        Args:
        - `num` — Column of numeric values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        The sum of the values. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        """
        return Function("sumWithOverflow", *to_args(locals()))
    
    @staticmethod
    def svg(geometry: Any, style: Any | None = None) -> Function:
        """
        svg(geometry[, style])

        Args:
        - `geometry` — Geometry object (Point, Ring, Polygon, MultiPolygon). [`Point`](/sql-reference/data-types/geo#point) or [`Ring`](/sql-reference/data-types/geo#ring) or [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)
        - `style` — Optional CSS style string to apply to the SVG element. [`String`](/sql-reference/data-types/string)

        Returns the SVG representation of the geometry. [`String`](/sql-reference/data-types/string)
        """
        return Function("svg", *to_args(locals()))
    
    @staticmethod
    def synonyms(ext_name: Any, word: Any) -> Function:
        """
        synonyms(ext_name, word)

        Args:
        - `ext_name` — Name of the extension in which search will be performed. [`String`](/sql-reference/data-types/string)
        - `word` — Word that will be searched in extension. [`String`](/sql-reference/data-types/string)

        Returns array of synonyms for the given word. [`Array(String)`](/sql-reference/data-types/array)
        """
        return Function("synonyms", *to_args(locals()))
    
    @staticmethod
    def tan(x: Any) -> Function:
        """
        tan(x)

        Args:
        - `x` — The angle in radians. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the tangent of `x`. [`Float*`](/sql-reference/data-types/float)
        """
        return Function("tan", *to_args(locals()))
    
    @staticmethod
    def tanh(x: Any) -> Function:
        """
        tanh(x)

        Args:
        - `x` — The angle in radians. Values from the interval: -∞ < x < +∞. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns values from the interval: -1 < tanh(x) < 1 [`Float*`](/sql-reference/data-types/float)
        """
        return Function("tanh", *to_args(locals()))
    
    @staticmethod
    def tcpPort() -> Function:
        """
        tcpPort()

        
        Returns the TCP port number. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("tcpPort", *to_args(locals()))
    
    @staticmethod
    def tgamma(x: Any) -> Function:
        """
        tgamma(x)

        Args:
        - `x` — The number for which to compute the gamma function of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the gamma function value [`Float*`](/sql-reference/data-types/float)
        """
        return Function("tgamma", *to_args(locals()))
    
    @staticmethod
    def theilsU(column1: Any, column2: Any) -> Function:
        """
        theilsU(column1, column2)

        Args:
        - `column1` — First column to be compared. [`Any`](/sql-reference/data-types)
        - `column2` — Second column to be compared. [`Any`](/sql-reference/data-types)

        Returns a value between -1 and 1. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("theilsU", *to_args(locals()))
    
    @staticmethod
    def throwIf(x: Any, message: Any | None = None, error_code: Any | None = None) -> Function:
        """
        throwIf(x[, message[, error_code]])

        Args:
        - `x` — The condition to check. [`Any`](/sql-reference/data-types)
        - `message` — Optional. Custom error message. [`const String`](/sql-reference/data-types/string)
        - `error_code` — Optional. Custom error code. [`const Int8/16/32`](/sql-reference/data-types/int-uint)

        Returns `0` if the condition is false, throws an exception if the condition is true. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("throwIf", *to_args(locals()))
    
    @staticmethod
    def tid() -> Function:
        """
        tid()

        
        Returns the current thread id. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("tid", *to_args(locals()))
    
    @staticmethod
    def timeDiff(startdate: Any, enddate: Any) -> Function:
        """
        timeDiff(startdate, enddate)

        Args:
        - `startdate` — The first time value to subtract (the subtrahend). [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `enddate` — The second time value to subtract from (the minuend). [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the difference between `enddate` and `startdate` expressed in seconds. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeDiff", *to_args(locals()))
    
    @staticmethod
    def timeSeriesChangesToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesChangesToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. 
        `changes` values on the specified grid as an `Array(Nullable(Float64))`. The returned array contains one value for each time grid point. The value is NULL if there are no samples within the window to calculate the changes value for a particular grid point.
        """
        return Function("timeSeriesChangesToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesCopyTag(dest_group: Any, src_group: Any, tag_to_copy: Any) -> Function:
        """
        timeSeriesCopyTag(dest_group, src_group, tag_to_copy)

        Args:
        - `dest_group` — The destination group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `src_group` — The source group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `tag_to_copy` — The name of a tag to copy. [`String`](/sql-reference/data-types/string)

        Returns a group of tags containing the tags from `dest_group` along with the copied tags from `src_group`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesCopyTag", *to_args(locals()))
    
    @staticmethod
    def timeSeriesCopyTags(dest_group: Any, src_group: Any, tags_to_copy: Any) -> Function:
        """
        timeSeriesCopyTags(dest_group, src_group, tags_to_copy)

        Args:
        - `dest_group` — The destination group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `src_group` — The source group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `tags_to_copy` — The names of tags to copy. [`Array(String)`](/sql-reference/data-types/array)

        Returns a group of tags containing the tags from `dest_group` along with the copied tags from `src_group`. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesCopyTags", *to_args(locals()))
    
    @staticmethod
    def timeSeriesDeltaToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesDeltaToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime`](/sql-reference/data-types/datetime) or [`Array(UInt32)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. [`Float*`](/sql-reference/data-types/float) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns delta values on the specified grid. The returned array contains one value for each time grid point. The value is NULL if there are not enough samples within the window to calculate the delta value for a particular grid point. [`Array(Nullable(Float64))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesDeltaToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesDerivToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesDerivToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. 
        `deriv` values on the specified grid as an `Array(Nullable(Float64))`. The returned array contains one value for each time grid point. The value is NULL if there are not enough samples within the window to calculate the derivative value for a particular grid point.
        """
        return Function("timeSeriesDerivToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesExtractTag(group: Any) -> Function:
        """
        timeSeriesExtractTag(group)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `tag_to_extract` — The name of a tag to extract from the group [`String`](/sql-reference/data-types/string)

        Returns the value of a specified tag. [`Nullable(String)`](/sql-reference/data-types/nullable)
        """
        return Function("timeSeriesExtractTag", *to_args(locals()))
    
    @staticmethod
    def timeSeriesFromGrid(start_timestamp: Any, end_timestamp: Any, step: Any, values: Any) -> Function:
        """
        timeSeriesFromGrid(start_timestamp, end_timestamp, step, values)

        Args:
        - `start_timestamp` — Start of the grid. [`DateTime64`](/sql-reference/data-types/datetime64) or [`DateTime`](/sql-reference/data-types/datetime) or [`UInt32`](/sql-reference/data-types/int-uint)
        - `end_timestamp` — End of the grid. [`DateTime64`](/sql-reference/data-types/datetime64) or [`DateTime`](/sql-reference/data-types/datetime) or [`UInt32`](/sql-reference/data-types/int-uint)
        - `step` — Step of the grid in seconds [`Decimal64`](/sql-reference/data-types/decimal) or [`Decimal32`](/sql-reference/data-types/decimal) or [`UInt32/64`](/sql-reference/data-types/int-uint)
        - `values` — Array of values [`Array(Float*)`](/sql-reference/data-types/array) or [`Array(Nullable(Float*))`](/sql-reference/data-types/array)

        Returns values from the source array of values combined with timestamps on a regular time grid described by `start_timestamp` and `step`. [`Array(Tuple(DateTime64, Float64))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesFromGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesGroupArray(timestamp: Any, value: Any) -> Function:
        """
        timeSeriesGroupArray(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. [`DateTime`](/sql-reference/data-types/datetime) or [`UInt32`](/sql-reference/data-types/int-uint) or [`UInt64`](/sql-reference/data-types/int-uint)
        - `value` — Value of the time series corresponding to the timestamp. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns an array of tuples `(timestamp, value)` sorted by timestamp in ascending order. If there are multiple values for the same timestamp then the function chooses the greatest of these values. [`Array(Tuple(T1, T2))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesGroupArray", *to_args(locals()))
    
    @staticmethod
    def timeSeriesGroupToTags(group: Any) -> Function:
        """
        timeSeriesGroupToTags(group)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of pairs `(tag_name, tag_value)`.
        The returned array is always sorted by `tag_name` and never contains the same `tag_name` more than once.
                 [`Array(Tuple(String, String))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesGroupToTags", *to_args(locals()))
    
    @staticmethod
    def timeSeriesIdToGroup(id: Any) -> Function:
        """
        timeSeriesIdToGroup(id)

        Args:
        - `id` — Identifier of a time series. [`UInt64`](/sql-reference/data-types/int-uint) or [`UInt128`](/sql-reference/data-types/int-uint) or [`UUID`](/sql-reference/data-types/uuid) or [`FixedString(16)`](/sql-reference/data-types/fixedstring)

        Returns a group of tags associated with the identifier `id` of a time series. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesIdToGroup", *to_args(locals()))
    
    @staticmethod
    def timeSeriesIdToTags(id: Any) -> Function:
        """
        timeSeriesIdToTags(id)

        Args:
        - `id` — Identifier of a time series. [`UInt64`](/sql-reference/data-types/int-uint) or [`UInt128`](/sql-reference/data-types/int-uint) or [`UUID`](/sql-reference/data-types/uuid) or [`FixedString(16)`](/sql-reference/data-types/fixedstring)

        Returns an array of pairs `(tag_name, tag_value)`.
        The returned array is always sorted by `tag_name` and never contains the same `tag_name` more than once.
                 [`Array(Tuple(String, String))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesIdToTags", *to_args(locals()))
    
    @staticmethod
    def timeSeriesInstantDeltaToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesInstantDeltaToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime`](/sql-reference/data-types/datetime) or [`Array(UInt32)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. [`Float*`](/sql-reference/data-types/float) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns idelta values on the specified grid. The returned array contains one value for each time grid point. The value is NULL if there are not enough samples within the window to calculate the instant delta value for a particular grid point. [`Array(Nullable(Float64))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesInstantDeltaToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesInstantRateToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesInstantRateToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime`](/sql-reference/data-types/datetime) or [`Array(UInt32)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. [`Float*`](/sql-reference/data-types/float) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns irate values on the specified grid. The returned array contains one value for each time grid point. The value is NULL if there are not enough samples within the window to calculate the instant rate value for a particular grid point. [`Array(Nullable(Float64))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesInstantRateToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesJoinTags(group: Any, dest_tag: Any, separator: Any, src_tags: Any) -> Function:
        """
        timeSeriesJoinTags(group, dest_tag, separator, src_tags)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `dest_tag` — The name of a tag with the joined result which will be added to the `group`. [`String`](/sql-reference/data-types/string)
        - `separator` — A separator to insert between joined values. [`String`](/sql-reference/data-types/string)
        - `src_tags` — The names of source tags with values which will be joined. [`Array(String)`](/sql-reference/data-types/array)

        Returns a new group of tags with the `dest_tag` tag set to the joined result. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesJoinTags", *to_args(locals()))
    
    @staticmethod
    def timeSeriesLastTwoSamples(timestamp: Any, value: Any) -> Function:
        """
        timeSeriesLastTwoSamples(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Int*`](/sql-reference/data-types/int-uint)
        - `value` — Value of the time series corresponding to the timestamp. [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)

        Returns a pair of arrays of equal length from 0 to 2. The first array contains the timestamps of sampled time series, the second array contains the corresponding values of the time series. [`Tuple(Array(DateTime), Array(Float64))`](/sql-reference/data-types/tuple)
        """
        return Function("timeSeriesLastTwoSamples", *to_args(locals()))
    
    @staticmethod
    def timeSeriesPredictLinearToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any, predict_offset: Any) -> Function:
        """
        timeSeriesPredictLinearToGrid(start_timestamp, end_timestamp, grid_step, staleness, predict_offset)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. 
        `predict_linear` values on the specified grid as an `Array(Nullable(Float64))`. The returned array contains one value for each time grid point. The value is NULL if there are not enough samples within the window to calculate the rate value for a particular grid point.
        """
        return Function("timeSeriesPredictLinearToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesRange(start_timestamp: Any, end_timestamp: Any, step: Any) -> Function:
        """
        timeSeriesRange(start_timestamp, end_timestamp, step)

        Args:
        - `start_timestamp` — Start of the range. [`DateTime64`](/sql-reference/data-types/datetime64) or [`DateTime`](/sql-reference/data-types/datetime) or [`UInt32`](/sql-reference/data-types/int-uint)
        - `end_timestamp` — End of the range. [`DateTime64`](/sql-reference/data-types/datetime64) or [`DateTime`](/sql-reference/data-types/datetime) or [`UInt32`](/sql-reference/data-types/int-uint)
        - `step` — Step of the range in seconds [`UInt32/64`](/sql-reference/data-types/int-uint) or [`Decimal32/64`](/sql-reference/data-types/decimal)

        Returns a range of timestamps. [`Array(DateTime64)`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesRange", *to_args(locals()))
    
    @staticmethod
    def timeSeriesRateToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesRateToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime`](/sql-reference/data-types/datetime) or [`Array(UInt32)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. [`Float*`](/sql-reference/data-types/float) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns rate values on the specified grid. The returned array contains one value for each time grid point. The value is NULL if there are not enough samples within the window to calculate the rate value for a particular grid point. [`Array(Nullable(Float64))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesRateToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesRemoveAllTagsExcept(group: Any, tags_to_keep: Any) -> Function:
        """
        timeSeriesRemoveAllTagsExcept(group, tags_to_keep)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `tags_to_keep` — The names of tags to keep in the group. [`Array(String)`](/sql-reference/data-types/array)

        A new group of tags with only the specified tags kept. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesRemoveAllTagsExcept", *to_args(locals()))
    
    @staticmethod
    def timeSeriesRemoveTag(group: Any, tag_to_remove: Any) -> Function:
        """
        timeSeriesRemoveTag(group, tag_to_remove)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `tag_to_remove` — The name of a tag to remove from the group. [`String`](/sql-reference/data-types/string)

        A new group of tags without the specified tag. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesRemoveTag", *to_args(locals()))
    
    @staticmethod
    def timeSeriesRemoveTags(group: Any, tags_to_remove: Any) -> Function:
        """
        timeSeriesRemoveTags(group, tags_to_remove)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `tags_to_remove` — The names of tags to remove from the group. [`Array(String)`](/sql-reference/data-types/array)

        A new group of tags without the specified tags. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesRemoveTags", *to_args(locals()))
    
    @staticmethod
    def timeSeriesReplaceTag(group: Any, dest_tag: Any, replacement: Any, src_tag: Any, regex: Any) -> Function:
        """
        timeSeriesReplaceTag(group, dest_tag, replacement, src_tag, regex)

        Args:
        - `group` — A group of tags. [`UInt64`](/sql-reference/data-types/int-uint)
        - `dest_tag` — The name of a destination tag to get the result group. [`String`](/sql-reference/data-types/string)
        - `replacement` — A replacement pattern, can contain $1, $2 or $name to refer capturing groups in the regular expression 'regex'. [`String`](/sql-reference/data-types/string)
        - `src_tag` — The name of a tag which value is used to match the regular expression 'regex'. [`String`](/sql-reference/data-types/string)
        - `regex` — A regular expression. [`String`](/sql-reference/data-types/string)

        A new group of tags with maybe `dest_tag` added. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesReplaceTag", *to_args(locals()))
    
    @staticmethod
    def timeSeriesResampleToGridWithStaleness(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness_window: Any) -> Function:
        """
        timeSeriesResampleToGridWithStaleness(start_timestamp, end_timestamp, grid_step, staleness_window)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime`](/sql-reference/data-types/datetime) or [`Array(UInt32)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. [`Float*`](/sql-reference/data-types/float) or [`Array(Float*)`](/sql-reference/data-types/array)

        Returns time series values re-sampled to the specified grid. The returned array contains one value for each time grid point. The value is NULL if there is no sample for a particular grid point. [`Array(Nullable(Float64))`](/sql-reference/data-types/array)
        """
        return Function("timeSeriesResampleToGridWithStaleness", *to_args(locals()))
    
    @staticmethod
    def timeSeriesResetsToGrid(start_timestamp: Any, end_timestamp: Any, grid_step: Any, staleness: Any) -> Function:
        """
        timeSeriesResetsToGrid(start_timestamp, end_timestamp, grid_step, staleness)(timestamp, value)

        Args:
        - `timestamp` — Timestamp of the sample. Can be individual values or arrays. - `value` — Value of the time series corresponding to the timestamp. Can be individual values or arrays. 
        `resets` values on the specified grid as an `Array(Nullable(Float64))`. The returned array contains one value for each time grid point. The value is NULL if there are no samples within the window to calculate the resets value for a particular grid point.
        """
        return Function("timeSeriesResetsToGrid", *to_args(locals()))
    
    @staticmethod
    def timeSeriesStoreTags(id: Any, tags_array: Any, separate_tag_name_1: Any, separate_tag_value_1: Any) -> Function:
        """
        timeSeriesStoreTags(id, tags_array, separate_tag_name_1, separate_tag_value_1, ...)

        Args:
        - `id` — Identifier of a time series. [`UInt64`](/sql-reference/data-types/int-uint) or [`UInt128`](/sql-reference/data-types/int-uint) or [`UUID`](/sql-reference/data-types/uuid) or [`FixedString(16)`](/sql-reference/data-types/fixedstring)
        - `tags_array` — Array of pairs (tag_name, tag_value). [`Array(Tuple(String, String))`](/sql-reference/data-types/array) or [`NULL`](/sql-reference/syntax#null)
        - `separate_tag_name_i` — The name of a tag. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `separate_tag_value_i` — The value of a tag. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Nullable(String)`](/sql-reference/data-types/nullable)

        Returns the identifier of a time series (i.e. just the first argument).
        """
        return Function("timeSeriesStoreTags", *to_args(locals()))
    
    @staticmethod
    def timeSeriesTagsToGroup(tags_array: Any, tag_name_1: Any, tag_value_1: Any, tag_name2: Any, tag_value2: Any) -> Function:
        """
        timeSeriesTagsToGroup(tags_array, tag_name_1, tag_value_1, tag_name2, tag_value2, ...)

        Args:
        - `tags_array` — Array of pairs (tag_name, tag_value). [`Array(Tuple(String, String))`](/sql-reference/data-types/array) or [`NULL`](/sql-reference/syntax#null)
        - `tag_name_i` — The name of a tag. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `tag_value_i` — The value of a tag. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Nullable(String)`](/sql-reference/data-types/nullable)

        Returns a group of tags associated with the specified tags. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesTagsToGroup", *to_args(locals()))
    
    @staticmethod
    def timeSeriesThrowDuplicateSeriesIf(condition: Any, group: Any) -> Function:
        """
        timeSeriesThrowDuplicateSeriesIf(condition, group)

        Args:
        - `condition` — Condition to check, usually contains function [count()](/sql-reference/aggregate-functions/reference/count#count) [`UInt8`](/sql-reference/data-types/int-uint)
        - `group` — Group of tags. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("timeSeriesThrowDuplicateSeriesIf", *to_args(locals()))
    
    @staticmethod
    def timeSlot(time: Any, time_zone: Any | None = None) -> Function:
        """
        timeSlot(time[, time_zone])

        Args:
        - `time` — Time to round to the start of a half-an-hour length interval. [`DateTime`](/sql-reference/data-types/datetime) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `time_zone` — Optional. A String type const value or an expression representing the time zone. [`String`](/sql-reference/data-types/string)

        Returns the time rounded to the start of a half-an-hour length interval. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("timeSlot", *to_args(locals()))
    
    @staticmethod
    def timeSlots(StartTime: Any, Duration: Any, Size: Any | None = None) -> Function:
        """
        timeSlots(StartTime, Duration[, Size])

        Args:
        - `StartTime` — Starting time for the interval. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `Duration` — Duration of the interval in seconds. [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `Size` — Optional. Size of time slots in seconds. Default is 1800 (30 minutes). [`UInt32`](/sql-reference/data-types/int-uint) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns an array of DateTime/DateTime64 (return type matches the type of `StartTime`). For DateTime64, the return value's scale can differ from the scale of `StartTime` - the highest scale among all given arguments is taken. [`Array(DateTime)`](/sql-reference/data-types/array) or [`Array(DateTime64)`](/sql-reference/data-types/array)
        """
        return Function("timeSlots", *to_args(locals()))
    
    @staticmethod
    def timestamp(expr: Any, expr_time: Any | None = None) -> Function:
        """
        timestamp(expr[, expr_time])

        Args:
        - `expr` — Date or date with time. [`String`](/sql-reference/data-types/string)
        - `expr_time` — Optional. Time to add to the converted value. [`String`](/sql-reference/data-types/string)

        Returns the converted value of `expr`, or `expr` with added time [`DateTime64(6)`](/sql-reference/data-types/datetime64)
        """
        return Function("timestamp", *to_args(locals()))
    
    @staticmethod
    def timezone() -> Function:
        """
        timezone()

        
        Returns the canonical time zone name as a [`String`](/sql-reference/data-types/string)
        """
        return Function("timezone", *to_args(locals()))
    
    @staticmethod
    def timezoneOf(datetime: Any) -> Function:
        """
        timezoneOf(datetime)

        Args:
        - `datetime` — A value of type. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone name to convert the `datetime` value's timezone to. [`String`](/sql-reference/data-types/string)

        Returns the timezone name for `datetime` [`String`](/sql-reference/data-types/string)
        """
        return Function("timezoneOf", *to_args(locals()))
    
    @staticmethod
    def timezoneOffset(datetime: Any) -> Function:
        """
        timezoneOffset(datetime)

        Args:
        - `datetime` — `DateTime` value to get the timezone offset for. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the offset from UTC in seconds [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("timezoneOffset", *to_args(locals()))
    
    @staticmethod
    def toBFloat16(expr: Any) -> Function:
        """
        toBFloat16(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 16-bit brain-float value. [`BFloat16`](/sql-reference/data-types/float)
        """
        return Function("toBFloat16", *to_args(locals()))
    
    @staticmethod
    def toBFloat16OrNull(x: Any) -> Function:
        """
        toBFloat16OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Reurns a 16-bit brain-float value, otherwise `NULL`. [`BFloat16`](/sql-reference/data-types/float) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toBFloat16OrNull", *to_args(locals()))
    
    @staticmethod
    def toBFloat16OrZero(x: Any) -> Function:
        """
        toBFloat16OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a 16-bit brain-float value, otherwise `0`. [`BFloat16`](/sql-reference/data-types/float)
        """
        return Function("toBFloat16OrZero", *to_args(locals()))
    
    @staticmethod
    def toBool(expr: Any) -> Function:
        """
        toBool(expr)

        Args:
        - `expr` — Expression returning a number or a string. For strings, accepts 'true' or 'false' (case-insensitive). [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string) or [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns `true` or `false` based on evaluation of the argument. [`Bool`](/sql-reference/data-types/boolean)
        """
        return Function("toBool", *to_args(locals()))
    
    @staticmethod
    def toColumnTypeName(value: Any) -> Function:
        """
        toColumnTypeName(value)

        Args:
        - `value` — Value for which to return the internal data type. [`Any`](/sql-reference/data-types)

        Returns the internal data type used to represent the value. [`String`](/sql-reference/data-types/string)
        """
        return Function("toColumnTypeName", *to_args(locals()))
    
    @staticmethod
    def toDate(x: Any) -> Function:
        """
        toDate(x)

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`DateTime`](/sql-reference/data-types/datetime) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the converted input value. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toDate", *to_args(locals()))
    
    @staticmethod
    def toDate32(expr: Any) -> Function:
        """
        toDate32(expr)

        Args:
        - `expr` — The value to convert. [`String`](/sql-reference/data-types/string) or [`UInt32`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date)

        Returns a calendar date. [`Date32`](/sql-reference/data-types/date32)
        """
        return Function("toDate32", *to_args(locals()))
    
    @staticmethod
    def toDate32OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toDate32OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Date32`](/sql-reference/data-types/date32)

        Value of type Date32 if successful, otherwise returns the default value if passed or 1900-01-01 if not. [`Date32`](/sql-reference/data-types/date32)
        """
        return Function("toDate32OrDefault", *to_args(locals()))
    
    @staticmethod
    def toDate32OrNull(x: Any) -> Function:
        """
        toDate32OrNull(x)

        Args:
        - `x` — A string representation of a date. [`String`](/sql-reference/data-types/string)

        Returns a Date32 value if successful, otherwise `NULL`. [`Date32`](/sql-reference/data-types/date32) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDate32OrNull", *to_args(locals()))
    
    @staticmethod
    def toDate32OrZero(x: Any) -> Function:
        """
        toDate32OrZero(x)

        Args:
        - `x` — A string representation of a date. [`String`](/sql-reference/data-types/string)

        Returns a Date32 value if successful, otherwise the lower boundary of Date32 (`1900-01-01`). [`Date32`](/sql-reference/data-types/date32)
        """
        return Function("toDate32OrZero", *to_args(locals()))
    
    @staticmethod
    def toDateOrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toDateOrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Date`](/sql-reference/data-types/date)

        Value of type Date if successful, otherwise returns the default value if passed or 1970-01-01 if not. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toDateOrDefault", *to_args(locals()))
    
    @staticmethod
    def toDateOrNull(x: Any) -> Function:
        """
        toDateOrNull(x)

        Args:
        - `x` — A string representation of a date. [`String`](/sql-reference/data-types/string)

        Returns a Date value if successful, otherwise `NULL`. [`Date`](/sql-reference/data-types/date) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDateOrNull", *to_args(locals()))
    
    @staticmethod
    def toDateOrZero(x: Any) -> Function:
        """
        toDateOrZero(x)

        Args:
        - `x` — A string representation of a date. [`String`](/sql-reference/data-types/string)

        Returns a Date value if successful, otherwise the lower boundary of Date (`1970-01-01`). [`Date`](/sql-reference/data-types/date)
        """
        return Function("toDateOrZero", *to_args(locals()))
    
    @staticmethod
    def toDateTime(expr: Any, time_zone: Any | None = None) -> Function:
        """
        toDateTime(expr[, time_zone])

        Args:
        - `expr` — The value. [`String`](/sql-reference/data-types/string) or [`Int`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `time_zone` — Time zone. [`String`](/sql-reference/data-types/string)

        Returns a date time. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("toDateTime", *to_args(locals()))
    
    @staticmethod
    def toDateTime32(x: Any, timezone: Any | None = None) -> Function:
        """
        toDateTime32(x[, timezone])

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the returned `DateTime` value. [`String`](/sql-reference/data-types/string)

        Returns the converted input value. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("toDateTime32", *to_args(locals()))
    
    @staticmethod
    def toDateTime64(expr: Any, scale: Any, timezone: Any | None = None) -> Function:
        """
        toDateTime64(expr, scale[, timezone])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `scale` — Tick size (precision): 10^(-scale) seconds. [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Time zone for the specified `DateTime64` object. [`String`](/sql-reference/data-types/string)

        Returns a calendar date and time of day, with sub-second precision. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toDateTime64", *to_args(locals()))
    
    @staticmethod
    def toDateTime64OrDefault(expr: Any, scale: Any, timezone: Any | None = None, default: Any | None = None) -> Function:
        """
        toDateTime64OrDefault(expr, scale[, timezone, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `scale` — Tick size (precision): 10^-precision seconds. [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Time zone. [`String`](/sql-reference/data-types/string)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`DateTime64`](/sql-reference/data-types/datetime64)

        Value of type DateTime64 if successful, otherwise returns the default value if passed or 1970-01-01 00:00:00.000 if not. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toDateTime64OrDefault", *to_args(locals()))
    
    @staticmethod
    def toDateTime64OrNull(x: Any) -> Function:
        """
        toDateTime64OrNull(x)

        Args:
        - `x` — A string representation of a date with time and subsecond precision. [`String`](/sql-reference/data-types/string)

        Returns a DateTime64 value if successful, otherwise `NULL`. [`DateTime64`](/sql-reference/data-types/datetime64) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDateTime64OrNull", *to_args(locals()))
    
    @staticmethod
    def toDateTime64OrZero(x: Any) -> Function:
        """
        toDateTime64OrZero(x)

        Args:
        - `x` — A string representation of a date with time and subsecond precision. [`String`](/sql-reference/data-types/string)

        Returns a DateTime64 value if successful, otherwise the lower boundary of DateTime64 (`1970-01-01 00:00:00.000`). [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toDateTime64OrZero", *to_args(locals()))
    
    @staticmethod
    def toDateTimeOrDefault(expr: Any, timezone: Any | None = None, default: Any | None = None) -> Function:
        """
        toDateTimeOrDefault(expr[, timezone, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `timezone` — Optional. Time zone. [`String`](/sql-reference/data-types/string)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`DateTime`](/sql-reference/data-types/datetime)

        Value of type DateTime if successful, otherwise returns the default value if passed or 1970-01-01 00:00:00 if not. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("toDateTimeOrDefault", *to_args(locals()))
    
    @staticmethod
    def toDateTimeOrNull(x: Any) -> Function:
        """
        toDateTimeOrNull(x)

        Args:
        - `x` — A string representation of a date with time. [`String`](/sql-reference/data-types/string)

        Returns a `DateTime` value if successful, otherwise `NULL`. [`DateTime`](/sql-reference/data-types/datetime) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDateTimeOrNull", *to_args(locals()))
    
    @staticmethod
    def toDateTimeOrZero(x: Any) -> Function:
        """
        toDateTimeOrZero(x)

        Args:
        - `x` — A string representation of a date with time. [`String`](/sql-reference/data-types/string)

        Returns a DateTime value if successful, otherwise the lower boundary of DateTime (`1970-01-01 00:00:00`). [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("toDateTimeOrZero", *to_args(locals()))
    
    @staticmethod
    def toDayOfMonth(datetime: Any) -> Function:
        """
        toDayOfMonth(datetime)

        Args:
        - `datetime` — Date or date with time to get the day of month from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the day of the month of the given date/time [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toDayOfMonth", *to_args(locals()))
    
    @staticmethod
    def toDayOfWeek(datetime: Any, mode: Any | None = None, timezone: Any | None = None) -> Function:
        """
        toDayOfWeek(datetime[, mode[, timezone]])

        Args:
        - `datetime` — Date or date with time to get the day of week from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `mode` — Optional. Integer specifying the week mode (0-3). Defaults to 0 if omitted. [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone to use for the conversion. [`String`](/sql-reference/data-types/string)

        Returns the day of the week for the given `Date` or `DateTime` [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toDayOfWeek", *to_args(locals()))
    
    @staticmethod
    def toDayOfYear(datetime: Any) -> Function:
        """
        toDayOfYear(datetime)

        Args:
        - `datetime` — Date or date with time to get the day of year from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the day of the year of the given Date or DateTime [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toDayOfYear", *to_args(locals()))
    
    @staticmethod
    def toDaysInMonth(datetime: Any) -> Function:
        """
        toDaysInMonth(datetime)

        Args:
        - `datetime` — Date or date with time to get the number of days in the month from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of days in the month of the given date/time. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toDaysInMonth", *to_args(locals()))
    
    @staticmethod
    def toDaysSinceYearZero(date: Any, time_zone: Any | None = None) -> Function:
        """
        toDaysSinceYearZero(date[, time_zone])

        Args:
        - `date` — The date or date with time for which to calculate the number of days since year zero from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `time_zone` — Time zone. [`String`](/sql-reference/data-types/string)

        Returns the number of days passed since date `0000-01-01`. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toDaysSinceYearZero", *to_args(locals()))
    
    @staticmethod
    def toDecimal128(expr: Any, S: Any) -> Function:
        """
        toDecimal128(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 38, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a value of type `Decimal(38, S)` [`Decimal128(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal128", *to_args(locals()))
    
    @staticmethod
    def toDecimal128OrDefault(expr: Any, S: Any, default: Any | None = None) -> Function:
        """
        toDecimal128OrDefault(expr, S[, default])

        Args:
        - `expr` — A String representation of a number. [`String`](/sql-reference/data-types/string)
        - `S` — Scale parameter between 0 and 38, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)
        - `default` — Optional. The default value to return if parsing to type Decimal128(S) is unsuccessful. [`Decimal128(S)`](/sql-reference/data-types/decimal)

        Value of type Decimal(38, S) if successful, otherwise returns the default value if passed or 0 if not. [`Decimal128(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal128OrDefault", *to_args(locals()))
    
    @staticmethod
    def toDecimal128OrNull(expr: Any, S: Any) -> Function:
        """
        toDecimal128OrNull(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 38, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(38, S) value if successful, otherwise `NULL`. [`Decimal128(S)`](/sql-reference/data-types/decimal) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDecimal128OrNull", *to_args(locals()))
    
    @staticmethod
    def toDecimal128OrZero(expr: Any, S: Any) -> Function:
        """
        toDecimal128OrZero(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 38, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(38, S) value if successful, otherwise `0`. [`Decimal128(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal128OrZero", *to_args(locals()))
    
    @staticmethod
    def toDecimal256(expr: Any, S: Any) -> Function:
        """
        toDecimal256(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 76, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a value of type `Decimal(76, S)`. [`Decimal256(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal256", *to_args(locals()))
    
    @staticmethod
    def toDecimal256OrDefault(expr: Any, S: Any, default: Any | None = None) -> Function:
        """
        toDecimal256OrDefault(expr, S[, default])

        Args:
        - `expr` — A String representation of a number. [`String`](/sql-reference/data-types/string)
        - `S` — Scale parameter between 0 and 76, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)
        - `default` — Optional. The default value to return if parsing to type Decimal256(S) is unsuccessful. [`Decimal256(S)`](/sql-reference/data-types/decimal)

        Value of type Decimal(76, S) if successful, otherwise returns the default value if passed or 0 if not. [`Decimal256(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal256OrDefault", *to_args(locals()))
    
    @staticmethod
    def toDecimal256OrNull(expr: Any, S: Any) -> Function:
        """
        toDecimal256OrNull(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 76, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(76, S) value if successful, otherwise `NULL`. [`Decimal256(S)`](/sql-reference/data-types/decimal) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDecimal256OrNull", *to_args(locals()))
    
    @staticmethod
    def toDecimal256OrZero(expr: Any, S: Any) -> Function:
        """
        toDecimal256OrZero(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 76, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(76, S) value if successful, otherwise `0`. [`Decimal256(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal256OrZero", *to_args(locals()))
    
    @staticmethod
    def toDecimal32(expr: Any, S: Any) -> Function:
        """
        toDecimal32(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 9, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a value of type `Decimal(9, S)` [`Decimal32(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal32", *to_args(locals()))
    
    @staticmethod
    def toDecimal32OrDefault(expr: Any, S: Any, default: Any | None = None) -> Function:
        """
        toDecimal32OrDefault(expr, S[, default])

        Args:
        - `expr` — A String representation of a number. [`String`](/sql-reference/data-types/string)
        - `S` — Scale parameter between 0 and 9, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)
        - `default` — Optional. The default value to return if parsing to type Decimal32(S) is unsuccessful. [`Decimal32(S)`](/sql-reference/data-types/decimal)

        Value of type Decimal(9, S) if successful, otherwise returns the default value if passed or 0 if not. [`Decimal32(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal32OrDefault", *to_args(locals()))
    
    @staticmethod
    def toDecimal32OrNull(expr: Any, S: Any) -> Function:
        """
        toDecimal32OrNull(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 9, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(9, S) value if successful, otherwise `NULL`. [`Decimal32(S)`](/sql-reference/data-types/decimal) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDecimal32OrNull", *to_args(locals()))
    
    @staticmethod
    def toDecimal32OrZero(expr: Any, S: Any) -> Function:
        """
        toDecimal32OrZero(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 9, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(9, S) value if successful, otherwise `0`. [`Decimal32(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal32OrZero", *to_args(locals()))
    
    @staticmethod
    def toDecimal64(expr: Any, S: Any) -> Function:
        """
        toDecimal64(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 18, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a decimal value. [`Decimal(18, S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal64", *to_args(locals()))
    
    @staticmethod
    def toDecimal64OrDefault(expr: Any, S: Any, default: Any | None = None) -> Function:
        """
        toDecimal64OrDefault(expr, S[, default])

        Args:
        - `expr` — A String representation of a number. [`String`](/sql-reference/data-types/string)
        - `S` — Scale parameter between 0 and 18, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)
        - `default` — Optional. The default value to return if parsing to type Decimal64(S) is unsuccessful. [`Decimal64(S)`](/sql-reference/data-types/decimal)

        Value of type Decimal(18, S) if successful, otherwise returns the default value if passed or 0 if not. [`Decimal64(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal64OrDefault", *to_args(locals()))
    
    @staticmethod
    def toDecimal64OrNull(expr: Any, S: Any) -> Function:
        """
        toDecimal64OrNull(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 18, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(18, S) value if successful, otherwise `NULL`. [`Decimal64(S)`](/sql-reference/data-types/decimal) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toDecimal64OrNull", *to_args(locals()))
    
    @staticmethod
    def toDecimal64OrZero(expr: Any, S: Any) -> Function:
        """
        toDecimal64OrZero(expr, S)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)
        - `S` — Scale parameter between 0 and 18, specifying how many digits the fractional part of a number can have. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a Decimal(18, S) value if successful, otherwise `0`. [`Decimal64(S)`](/sql-reference/data-types/decimal)
        """
        return Function("toDecimal64OrZero", *to_args(locals()))
    
    @staticmethod
    def toDecimalString(number: Any, scale: Any) -> Function:
        """
        toDecimalString(number, scale)

        Args:
        - `number` — The numeric value to convert to a string. Can be any numeric type (Int, UInt, Float, Decimal). [`Int8`](/sql-reference/data-types/int-uint) or [`Int16`](/sql-reference/data-types/int-uint) or [`Int32`](/sql-reference/data-types/int-uint) or [`Int64`](/sql-reference/data-types/int-uint) or [`UInt8`](/sql-reference/data-types/int-uint) or [`UInt16`](/sql-reference/data-types/int-uint) or [`UInt32`](/sql-reference/data-types/int-uint) or [`UInt64`](/sql-reference/data-types/int-uint) or [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)
        - `scale` — The number of digits to display in the fractional part. The result will be rounded if necessary. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a String representation of the number with exactly the specified number of fractional digits. [`String`](/sql-reference/data-types/string)
        """
        return Function("toDecimalString", *to_args(locals()))
    
    @staticmethod
    def toFixedString(s: Any, N: Any) -> Function:
        """
        toFixedString(s, N)

        Args:
        - `s` — String to convert. [`String`](/sql-reference/data-types/string)
        - `N` — Length of the resulting FixedString. [`const UInt*`](/sql-reference/data-types/int-uint)

        Returns a FixedString of length N. [`FixedString(N)`](/sql-reference/data-types/fixedstring)
        """
        return Function("toFixedString", *to_args(locals()))
    
    @staticmethod
    def toFloat32(expr: Any) -> Function:
        """
        toFloat32(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 32-bit floating point value. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("toFloat32", *to_args(locals()))
    
    @staticmethod
    def toFloat32OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toFloat32OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Float32`](/sql-reference/data-types/float)

        Returns a value of type Float32 if successful, otherwise returns the default value if passed or 0 if not. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("toFloat32OrDefault", *to_args(locals()))
    
    @staticmethod
    def toFloat32OrNull(x: Any) -> Function:
        """
        toFloat32OrNull(x)

        Args:
        - `x` — A string representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a 32-bit Float value if successful, otherwise `NULL`. [`Float32`](/sql-reference/data-types/float) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toFloat32OrNull", *to_args(locals()))
    
    @staticmethod
    def toFloat32OrZero(x: Any) -> Function:
        """
        toFloat32OrZero(x)

        Args:
        - `x` — A string representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a 32-bit Float value if successful, otherwise `0`. [`Float32`](/sql-reference/data-types/float)
        """
        return Function("toFloat32OrZero", *to_args(locals()))
    
    @staticmethod
    def toFloat64(expr: Any) -> Function:
        """
        toFloat64(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 64-bit floating point value. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("toFloat64", *to_args(locals()))
    
    @staticmethod
    def toFloat64OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toFloat64OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Float64`](/sql-reference/data-types/float)

        Returns a value of type Float64 if successful, otherwise returns the default value if passed or 0 if not. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("toFloat64OrDefault", *to_args(locals()))
    
    @staticmethod
    def toFloat64OrNull(x: Any) -> Function:
        """
        toFloat64OrNull(x)

        Args:
        - `x` — A string representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a 64-bit Float value if successful, otherwise `NULL`. [`Float64`](/sql-reference/data-types/float) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toFloat64OrNull", *to_args(locals()))
    
    @staticmethod
    def toFloat64OrZero(x: Any) -> Function:
        """
        toFloat64OrZero(x)

        Args:
        - `x` — A string representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a 64-bit Float value if successful, otherwise `0`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("toFloat64OrZero", *to_args(locals()))
    
    @staticmethod
    def toHour(datetime: Any) -> Function:
        """
        toHour(datetime)

        Args:
        - `datetime` — Date with time to get the hour from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the hour (0-23) of `datetime`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toHour", *to_args(locals()))
    
    @staticmethod
    def toIPv4(x: Any) -> Function:
        """
        toIPv4(x)

        Args:
        - `x` — An IPv4 address [`String`](/sql-reference/data-types/string) or [`UInt8/16/32`](/sql-reference/data-types/int-uint)

        Returns an IPv4 address. [`IPv4`](/sql-reference/data-types/ipv4)
        """
        return Function("toIPv4", *to_args(locals()))
    
    @staticmethod
    def toIPv4OrDefault(string: Any, default: Any | None = None) -> Function:
        """
        toIPv4OrDefault(string[, default])

        Args:
        - `string` — IP address string to convert. [`String`](/sql-reference/data-types/string)
        - `default` — Optional. The value to return if string is an invalid IPv4 address. [`IPv4`](/sql-reference/data-types/ipv4)

        Returns a string converted to the current IPv4 address, or the default value if conversion fails. [`IPv4`](/sql-reference/data-types/ipv4)
        """
        return Function("toIPv4OrDefault", *to_args(locals()))
    
    @staticmethod
    def toIPv4OrNull(x: Any) -> Function:
        """
        toIPv4OrNull(x)

        Args:
        - `x` — A string or integer representation of an IPv4 address. [`String`](/sql-reference/data-types/string) or [`Integer`](/sql-reference/data-types/int-uint)

        Returns an IPv4 address if successful, otherwise `NULL`. [`IPv4`](/sql-reference/data-types/ipv4) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toIPv4OrNull", *to_args(locals()))
    
    @staticmethod
    def toIPv4OrZero(x: Any) -> Function:
        """
        toIPv4OrZero(x)

        Args:
        - `x` — A string or integer representation of an IPv4 address. [`String`](/sql-reference/data-types/string) or [`Integer`](/sql-reference/data-types/int-uint)

        Returns an IPv4 address if successful, otherwise zero IPv4 address (`0.0.0.0`). [`IPv4`](/sql-reference/data-types/ipv4)
        """
        return Function("toIPv4OrZero", *to_args(locals()))
    
    @staticmethod
    def toIPv6(x: Any) -> Function:
        """
        toIPv6(x)

        Args:
        - `x` — An IP address. [`String`](/sql-reference/data-types/string) or [`UInt128`](/sql-reference/data-types/int-uint)

        Returns an IPv6 address. [`IPv6`](/sql-reference/data-types/ipv6)
        """
        return Function("toIPv6", *to_args(locals()))
    
    @staticmethod
    def toIPv6OrDefault(string: Any, default: Any | None = None) -> Function:
        """
        toIPv6OrDefault(string[, default])

        Args:
        - `string` — IP address string to convert. - `default` — Optional. The value to return if string has an invalid format. 
        Returns the IPv6 address, otherwise `::` or the provided optional default if argument `string` has an invalid format. [`IPv6`](/sql-reference/data-types/ipv6)
        """
        return Function("toIPv6OrDefault", *to_args(locals()))
    
    @staticmethod
    def toIPv6OrNull(x: Any) -> Function:
        """
        toIPv6OrNull(x)

        Args:
        - `x` — A string representation of an IPv6 or IPv4 address. [`String`](/sql-reference/data-types/string)

        Returns an IPv6 address if successful, otherwise `NULL`. [`IPv6`](/sql-reference/data-types/ipv6) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toIPv6OrNull", *to_args(locals()))
    
    @staticmethod
    def toIPv6OrZero(x: Any) -> Function:
        """
        toIPv6OrZero(x)

        Args:
        - `x` — A string representation of an IPv6 or IPv4 address. [`String`](/sql-reference/data-types/string)

        Returns an IPv6 address if successful, otherwise zero IPv6 address (`::`).  [`IPv6`](/sql-reference/data-types/ipv6)
        """
        return Function("toIPv6OrZero", *to_args(locals()))
    
    @staticmethod
    def toISOWeek(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toISOWeek(datetime[, timezone])

        Args:
        - `datetime` — Date or date with time to get the ISO week number from. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Time zone. [`String`](/sql-reference/data-types/string)

        Returns the ISO week number according to ISO 8601 standard. Returns a number between 1 and 53. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toISOWeek", *to_args(locals()))
    
    @staticmethod
    def toISOYear(datetime: Any) -> Function:
        """
        toISOYear(datetime)

        Args:
        - `datetime` — The value with date or date with time. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the input value converted to an ISO year number. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toISOYear", *to_args(locals()))
    
    @staticmethod
    def toInt128(expr: Any) -> Function:
        """
        toInt128(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 128-bit integer value. [`Int128`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt128", *to_args(locals()))
    
    @staticmethod
    def toInt128OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toInt128OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Int128`](/sql-reference/data-types/int-uint)

        Returns a value of type Int128 if successful, otherwise returns the default value if passed, or 0 if not. [`Int128`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt128OrDefault", *to_args(locals()))
    
    @staticmethod
    def toInt128OrNull(x: Any) -> Function:
        """
        toInt128OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int128, otherwise `NULL` if the conversion is unsuccessful. [`Int128`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toInt128OrNull", *to_args(locals()))
    
    @staticmethod
    def toInt128OrZero(x: Any) -> Function:
        """
        toInt128OrZero(x)

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the converted input value, otherwise `0` if conversion fails. [`Int128`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt128OrZero", *to_args(locals()))
    
    @staticmethod
    def toInt16(expr: Any) -> Function:
        """
        toInt16(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 16-bit integer value. [`Int16`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt16", *to_args(locals()))
    
    @staticmethod
    def toInt16OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toInt16OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Int16`](/sql-reference/data-types/int-uint)

        Returns a value of type Int16 if successful, otherwise returns the default value if passed, or 0 if not. [`Int16`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt16OrDefault", *to_args(locals()))
    
    @staticmethod
    def toInt16OrNull(x: Any) -> Function:
        """
        toInt16OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type `Int16`, otherwise `NULL` if the conversion is unsuccessful. [`Int16`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toInt16OrNull", *to_args(locals()))
    
    @staticmethod
    def toInt16OrZero(x: Any) -> Function:
        """
        toInt16OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int16, otherwise `0` if the conversion is unsuccessful. [`Int16`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt16OrZero", *to_args(locals()))
    
    @staticmethod
    def toInt256(expr: Any) -> Function:
        """
        toInt256(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 256-bit integer value. [`Int256`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt256", *to_args(locals()))
    
    @staticmethod
    def toInt256OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toInt256OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Int256`](/sql-reference/data-types/int-uint)

        Returns a value of type Int256 if successful, otherwise returns the default value if passed, or 0 if not. [`Int256`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt256OrDefault", *to_args(locals()))
    
    @staticmethod
    def toInt256OrNull(x: Any) -> Function:
        """
        toInt256OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int256, otherwise `NULL` if the conversion is unsuccessful. [`Int256`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toInt256OrNull", *to_args(locals()))
    
    @staticmethod
    def toInt256OrZero(x: Any) -> Function:
        """
        toInt256OrZero(x)

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the converted input value, otherwise `0` if conversion fails. [`Int256`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt256OrZero", *to_args(locals()))
    
    @staticmethod
    def toInt32(expr: Any) -> Function:
        """
        toInt32(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 32-bit integer value. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt32", *to_args(locals()))
    
    @staticmethod
    def toInt32OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toInt32OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Int32`](/sql-reference/data-types/int-uint)

        Returns a value of type Int32 if successful, otherwise returns the default value if passed or 0 if not. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt32OrDefault", *to_args(locals()))
    
    @staticmethod
    def toInt32OrNull(x: Any) -> Function:
        """
        toInt32OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int32, otherwise `NULL` if the conversion is unsuccessful. [`Int32`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toInt32OrNull", *to_args(locals()))
    
    @staticmethod
    def toInt32OrZero(x: Any) -> Function:
        """
        toInt32OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int32, otherwise `0` if the conversion is unsuccessful. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt32OrZero", *to_args(locals()))
    
    @staticmethod
    def toInt64(expr: Any) -> Function:
        """
        toInt64(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. Supported: values or string representations of type (U)Int*, values of type Float*. Unsupported: string representations of Float* values including NaN and Inf, string representations of binary and hexadecimal values. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 64-bit integer value. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt64", *to_args(locals()))
    
    @staticmethod
    def toInt64OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toInt64OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Int64`](/sql-reference/data-types/int-uint)

        Returns a value of type Int64 if successful, otherwise returns the default value if passed, or 0 if not. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt64OrDefault", *to_args(locals()))
    
    @staticmethod
    def toInt64OrNull(x: Any) -> Function:
        """
        toInt64OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int64, otherwise `NULL` if the conversion is unsuccessful. [`Int64`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toInt64OrNull", *to_args(locals()))
    
    @staticmethod
    def toInt64OrZero(x: Any) -> Function:
        """
        toInt64OrZero(x)

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the converted input value, otherwise `0` if conversion fails. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt64OrZero", *to_args(locals()))
    
    @staticmethod
    def toInt8(expr: Any) -> Function:
        """
        toInt8(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns an 8-bit integer value. [`Int8`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt8", *to_args(locals()))
    
    @staticmethod
    def toInt8OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toInt8OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`Int8`](/sql-reference/data-types/int-uint)

        Returns a value of type Int8 if successful, otherwise returns the default value if passed, or 0 if not. [`Int8`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt8OrDefault", *to_args(locals()))
    
    @staticmethod
    def toInt8OrNull(x: Any) -> Function:
        """
        toInt8OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int8, otherwise `NULL` if the conversion is unsuccessful. [`Int8`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toInt8OrNull", *to_args(locals()))
    
    @staticmethod
    def toInt8OrZero(x: Any) -> Function:
        """
        toInt8OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type Int8, otherwise `0` if the conversion is unsuccessful. [`Int8`](/sql-reference/data-types/int-uint)
        """
        return Function("toInt8OrZero", *to_args(locals()))
    
    @staticmethod
    def toInterval(value: Any, unit: Any) -> Function:
        """
        toInterval(value, unit)

        Args:
        - `value` — The numeric value representing the number of units. Can be any numeric type. [`Int8`](/sql-reference/data-types/int-uint) or [`Int16`](/sql-reference/data-types/int-uint) or [`Int32`](/sql-reference/data-types/int-uint) or [`Int64`](/sql-reference/data-types/int-uint) or [`UInt8`](/sql-reference/data-types/int-uint) or [`UInt16`](/sql-reference/data-types/int-uint) or [`UInt32`](/sql-reference/data-types/int-uint) or [`UInt64`](/sql-reference/data-types/int-uint) or [`Float32`](/sql-reference/data-types/float) or [`Float64`](/sql-reference/data-types/float)
        - `unit` — The unit of time. Must be a constant string. Valid values: 'nanosecond', 'microsecond', 'millisecond', 'second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year'. [`String`](/sql-reference/data-types/string)

        Returns an Interval value of the specified type. The result type depends on the unit: IntervalNanosecond, IntervalMicrosecond, IntervalMillisecond, IntervalSecond, IntervalMinute, IntervalHour, IntervalDay, IntervalWeek, IntervalMonth, IntervalQuarter, or IntervalYear. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toInterval", *to_args(locals()))
    
    @staticmethod
    def toIntervalDay(n: Any) -> Function:
        """
        toIntervalDay(n)

        Args:
        - `n` — Number of days. Integer numbers or string representations thereof, and float numbers. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` days. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalDay", *to_args(locals()))
    
    @staticmethod
    def toIntervalHour(n: Any) -> Function:
        """
        toIntervalHour(n)

        Args:
        - `n` — Number of hours. Integer numbers or string representations thereof, and float numbers. [`Int*`](/sql-reference/data-types/int-uint) or [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` hours. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalHour", *to_args(locals()))
    
    @staticmethod
    def toIntervalMicrosecond(n: Any) -> Function:
        """
        toIntervalMicrosecond(n)

        Args:
        - `n` — Number of microseconds. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` microseconds. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalMicrosecond", *to_args(locals()))
    
    @staticmethod
    def toIntervalMillisecond(n: Any) -> Function:
        """
        toIntervalMillisecond(n)

        Args:
        - `n` — Number of milliseconds. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` milliseconds. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalMillisecond", *to_args(locals()))
    
    @staticmethod
    def toIntervalMinute(n: Any) -> Function:
        """
        toIntervalMinute(n)

        Args:
        - `n` — Number of minutes. Integer numbers or string representations thereof, and float numbers. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` minutes. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalMinute", *to_args(locals()))
    
    @staticmethod
    def toIntervalMonth(n: Any) -> Function:
        """
        toIntervalMonth(n)

        Args:
        - `n` — Number of months. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` months. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalMonth", *to_args(locals()))
    
    @staticmethod
    def toIntervalNanosecond(n: Any) -> Function:
        """
        toIntervalNanosecond(n)

        Args:
        - `n` — Number of nanoseconds. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` nanoseconds. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalNanosecond", *to_args(locals()))
    
    @staticmethod
    def toIntervalQuarter(n: Any) -> Function:
        """
        toIntervalQuarter(n)

        Args:
        - `n` — Number of quarters. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` quarters. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalQuarter", *to_args(locals()))
    
    @staticmethod
    def toIntervalSecond(n: Any) -> Function:
        """
        toIntervalSecond(n)

        Args:
        - `n` — Number of seconds. Integer numbers or string representations thereof, and float numbers. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` seconds. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalSecond", *to_args(locals()))
    
    @staticmethod
    def toIntervalWeek(n: Any) -> Function:
        """
        toIntervalWeek(n)

        Args:
        - `n` — Number of weeks. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` weeks. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalWeek", *to_args(locals()))
    
    @staticmethod
    def toIntervalYear(n: Any) -> Function:
        """
        toIntervalYear(n)

        Args:
        - `n` — Number of years. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string)

        Returns an interval of `n` years. [`Interval`](/sql-reference/data-types/int-uint)
        """
        return Function("toIntervalYear", *to_args(locals()))
    
    @staticmethod
    def toJSONString(value: Any) -> Function:
        """
        toJSONString(value)

        Args:
        - `value` — Value to serialize. Value may be of any data type. [`Any`](/sql-reference/data-types)

        Returns the JSON representation of the value. [`String`](/sql-reference/data-types/string)
        """
        return Function("toJSONString", *to_args(locals()))
    
    @staticmethod
    def toLastDayOfMonth(value: Any) -> Function:
        """
        toLastDayOfMonth(value)

        Args:
        - `value` — The date or date with time to round up to the last day of the month. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date of the last day of the month for the given date or date with time. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toLastDayOfMonth", *to_args(locals()))
    
    @staticmethod
    def toLastDayOfWeek(datetime: Any, mode: Any | None = None, timezone: Any | None = None) -> Function:
        """
        toLastDayOfWeek(datetime[, mode[, timezone]])

        Args:
        - `datetime` — A date or date with time to convert. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `mode` — Determines the first day of the week as described in the `toWeek()` function. Default `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. The timezone to use for the conversion. If not specified, the server's timezone is used. [`String`](/sql-reference/data-types/string)

        Returns the date of the nearest Saturday or Sunday, on or after the given date, depending on the mode [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toLastDayOfWeek", *to_args(locals()))
    
    @staticmethod
    def toLowCardinality(expr: Any) -> Function:
        """
        toLowCardinality(expr)

        Args:
        - `expr` — Expression resulting in one of the supported data types. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the input value converted to the `LowCardinality` data type. [`LowCardinality`](/sql-reference/data-types/lowcardinality)
        """
        return Function("toLowCardinality", *to_args(locals()))
    
    @staticmethod
    def toMillisecond(datetime: Any) -> Function:
        """
        toMillisecond(datetime)

        Args:
        - `datetime` — Date with time to get the millisecond from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the millisecond in the minute (0 - 59) of `datetime`. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toMillisecond", *to_args(locals()))
    
    @staticmethod
    def toMinute(datetime: Any) -> Function:
        """
        toMinute(datetime)

        Args:
        - `datetime` — Date with time to get the minute from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the minute of the hour (0 - 59) of `datetime`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toMinute", *to_args(locals()))
    
    @staticmethod
    def toModifiedJulianDay(date: Any) -> Function:
        """
        toModifiedJulianDay(date)

        Args:
        - `date` — The date in String form. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns Modified Julian Day number. [`Int32`](/sql-reference/data-types/int-uint)
        """
        return Function("toModifiedJulianDay", *to_args(locals()))
    
    @staticmethod
    def toModifiedJulianDayOrNull(date: Any) -> Function:
        """
        toModifiedJulianDayOrNull(date)

        Args:
        - `date` — Date in text form. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns the modified Julian day number for valid `date`, otherwise `null`. [`Nullable(Int32)`](/sql-reference/data-types/nullable)
        """
        return Function("toModifiedJulianDayOrNull", *to_args(locals()))
    
    @staticmethod
    def toMonday(value: Any) -> Function:
        """
        toMonday(value)

        Args:
        - `value` — Date or date with time to round down to the Monday of the week. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date of the Monday of the same week for the given date or date with time. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toMonday", *to_args(locals()))
    
    @staticmethod
    def toMonth(datetime: Any) -> Function:
        """
        toMonth(datetime)

        Args:
        - `datetime` — Date or date with time to get the month from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the month of the given date/time [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toMonth", *to_args(locals()))
    
    @staticmethod
    def toMonthNumSinceEpoch(date: Any) -> Function:
        """
        toMonthNumSinceEpoch(date)

        Args:
        - `date` — A date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Positive integer
        """
        return Function("toMonthNumSinceEpoch", *to_args(locals()))
    
    @staticmethod
    def toNullable(x: Any) -> Function:
        """
        toNullable(x)

        Args:
        - `x` — A value of any non-compound type. [`Any`](/sql-reference/data-types)

        Returns the input value but of `Nullable` type. [`Nullable(Any)`](/sql-reference/data-types/nullable)
        """
        return Function("toNullable", *to_args(locals()))
    
    @staticmethod
    def toQuarter(datetime: Any) -> Function:
        """
        toQuarter(datetime)

        Args:
        - `datetime` — Date or date with time to get the quarter of the year from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the quarter of the year for the given date/time [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toQuarter", *to_args(locals()))
    
    @staticmethod
    def toRelativeDayNum(date: Any) -> Function:
        """
        toRelativeDayNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of days from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeDayNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeHourNum(date: Any) -> Function:
        """
        toRelativeHourNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of hours from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeHourNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeMinuteNum(date: Any) -> Function:
        """
        toRelativeMinuteNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of minutes from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeMinuteNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeMonthNum(date: Any) -> Function:
        """
        toRelativeMonthNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of months from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeMonthNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeQuarterNum(date: Any) -> Function:
        """
        toRelativeQuarterNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of quarters from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeQuarterNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeSecondNum(date: Any) -> Function:
        """
        toRelativeSecondNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of seconds from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeSecondNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeWeekNum(date: Any) -> Function:
        """
        toRelativeWeekNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of weeks from a fixed reference point in the past. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeWeekNum", *to_args(locals()))
    
    @staticmethod
    def toRelativeYearNum(date: Any) -> Function:
        """
        toRelativeYearNum(date)

        Args:
        - `date` — Date or date with time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the number of years from a fixed reference point in the past. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toRelativeYearNum", *to_args(locals()))
    
    @staticmethod
    def toSecond(datetime: Any) -> Function:
        """
        toSecond(datetime)

        Args:
        - `datetime` — Date with time to get the second from. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the second in the minute (0 - 59) of `datetime`. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toSecond", *to_args(locals()))
    
    @staticmethod
    def toStartOfDay(datetime: Any) -> Function:
        """
        toStartOfDay(datetime)

        Args:
        - `datetime` — A date or date with time to round. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the date with time rounded down to the start of the day. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfDay", *to_args(locals()))
    
    @staticmethod
    def toStartOfFifteenMinutes(datetime: Any) -> Function:
        """
        toStartOfFifteenMinutes(datetime)

        Args:
        - `datetime` — A date or date with time to round. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date with time rounded to the start of the nearest fifteen-minute interval [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfFifteenMinutes", *to_args(locals()))
    
    @staticmethod
    def toStartOfFiveMinutes(datetime: Any) -> Function:
        """
        toStartOfFiveMinutes(datetime)

        Args:
        - `datetime` — A date with time to round. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date with time rounded to the start of the nearest five-minute interval [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfFiveMinutes", *to_args(locals()))
    
    @staticmethod
    def toStartOfHour(datetime: Any) -> Function:
        """
        toStartOfHour(datetime)

        Args:
        - `datetime` — A date with time to round. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date with time rounded down to the start of the hour. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfHour", *to_args(locals()))
    
    @staticmethod
    def toStartOfISOYear(value: Any) -> Function:
        """
        toStartOfISOYear(value)

        Args:
        - `value` — The date or date with time to round down to the first day of the ISO year. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the first day of the ISO year for the given date or date with time. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toStartOfISOYear", *to_args(locals()))
    
    @staticmethod
    def toStartOfInterval(value: Any, INTERVAL: Any, x: Any, unit: Any, time_zone: Any | None = None) -> Function:
        """
        toStartOfInterval(value, INTERVAL x unit[, time_zone])
        toStartOfInterval(value, INTERVAL x unit[, origin[, time_zone]])

        Args:
        - `value` — Date or date with time value to round down. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `x` — Interval length number. - `unit` — Interval unit: YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, MINUTE, SECOND, MILLISECOND, MICROSECOND, NANOSECOND. - `time_zone` — Optional. Time zone name as a string. - `origin` — Optional. Origin point for calculation (second overload only). 
        Returns the start of the interval containing the input value. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("toStartOfInterval", *to_args(locals()))
    
    @staticmethod
    def toStartOfMicrosecond(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toStartOfMicrosecond(datetime[, timezone])

        Args:
        - `datetime` — Date and time. [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the returned value. If not specified, the function uses the timezone of the `value` parameter. [`String`](/sql-reference/data-types/string)

        Input value with sub-microseconds [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfMicrosecond", *to_args(locals()))
    
    @staticmethod
    def toStartOfMillisecond(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toStartOfMillisecond(datetime[, timezone])

        Args:
        - `datetime` — Date and time. [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the returned value. If not specified, the function uses the timezone of the `value` parameter. [`String`](/sql-reference/data-types/string)

        Input value with sub-milliseconds. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfMillisecond", *to_args(locals()))
    
    @staticmethod
    def toStartOfMinute(datetime: Any) -> Function:
        """
        toStartOfMinute(datetime)

        Args:
        - `datetime` — A date with time to round. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date with time rounded down to the start of the minute. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfMinute", *to_args(locals()))
    
    @staticmethod
    def toStartOfMonth(value: Any) -> Function:
        """
        toStartOfMonth(value)

        Args:
        - `value` — The date or date with time to round down to the first day of the month. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the first day of the month for the given date or date with time. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toStartOfMonth", *to_args(locals()))
    
    @staticmethod
    def toStartOfNanosecond(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toStartOfNanosecond(datetime[, timezone])

        Args:
        - `datetime` — Date and time. [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the returned value. If not specified, the function uses the timezone of the `value` parameter. [`String`](/sql-reference/data-types/string)

        Input value with nanoseconds. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfNanosecond", *to_args(locals()))
    
    @staticmethod
    def toStartOfQuarter(value: Any) -> Function:
        """
        toStartOfQuarter(value)

        Args:
        - `value` — The date or date with time to round down to the first day of the quarter. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the first day of the quarter for the given date or date with time. [`Date`](/sql-reference/data-types/date)
        """
        return Function("toStartOfQuarter", *to_args(locals()))
    
    @staticmethod
    def toStartOfSecond(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toStartOfSecond(datetime[, timezone])

        Args:
        - `datetime` — Date and time to truncate sub-seconds from. [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the returned value. If not specified, the function uses the timezone of the `value` parameter. [`String`](/sql-reference/data-types/string)

        Returns the input value without sub-seconds. [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfSecond", *to_args(locals()))
    
    @staticmethod
    def toStartOfTenMinutes(datetime: Any) -> Function:
        """
        toStartOfTenMinutes(datetime)

        Args:
        - `datetime` — A date with time. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the date with time rounded to the start of the nearest ten-minute interval [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfTenMinutes", *to_args(locals()))
    
    @staticmethod
    def toStartOfWeek(datetime: Any, mode: Any | None = None, timezone: Any | None = None) -> Function:
        """
        toStartOfWeek(datetime[, mode[, timezone]])

        Args:
        - `datetime` — A date or date with time to convert. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `mode` — Determines the first day of the week as described in the `toWeek()` function. Default `0`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `timezone` — The timezone to use for the conversion. If not specified, the server's timezone is used. [`String`](/sql-reference/data-types/string)

        Returns the date of the nearest Sunday or Monday on, or prior to, the given date, depending on the mode [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toStartOfWeek", *to_args(locals()))
    
    @staticmethod
    def toStartOfYear(value: Any) -> Function:
        """
        toStartOfYear(value)

        Args:
        - `value` — The date or date with time to round down. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the first day of the year for the given date/time [`Date`](/sql-reference/data-types/date)
        """
        return Function("toStartOfYear", *to_args(locals()))
    
    @staticmethod
    def toString(value: Any, timezone: Any | None = None) -> Function:
        """
        toString(value[, timezone])

        Args:
        - `value` — Value to convert to string. [`Any`](/sql-reference/data-types)
        - `timezone` — Optional. Timezone name for DateTime conversion. [`String`](/sql-reference/data-types/string)

        Returns a string representation of the input value. [`String`](/sql-reference/data-types/string)
        """
        return Function("toString", *to_args(locals()))
    
    @staticmethod
    def toStringCutToZero(s: Any) -> Function:
        """
        toStringCutToZero(s)

        Args:
        - `s` — String or FixedString to process. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns a String containing the characters before the first null byte. [`String`](/sql-reference/data-types/string)
        """
        return Function("toStringCutToZero", *to_args(locals()))
    
    @staticmethod
    def toTime(x: Any) -> Function:
        """
        toTime(x)

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`DateTime`](/sql-reference/data-types/datetime) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the converted value. [`Time`](/sql-reference/data-types/time)
        """
        return Function("toTime", *to_args(locals()))
    
    @staticmethod
    def toTime64(x: Any) -> Function:
        """
        toTime64(x)

        Args:
        - `x` — Input value to convert. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)

        Returns the converted input value with microsecond precision. [`Time64(6)`](/sql-reference/data-types/time64)
        """
        return Function("toTime64", *to_args(locals()))
    
    @staticmethod
    def toTime64OrNull(x: Any) -> Function:
        """
        toTime64OrNull(x)

        Args:
        - `x` — A string representation of a time with subsecond precision. [`String`](/sql-reference/data-types/string)

        Returns a Time64 value if successful, otherwise `NULL`. [`Time64`](/sql-reference/data-types/time64) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toTime64OrNull", *to_args(locals()))
    
    @staticmethod
    def toTime64OrZero(x: Any) -> Function:
        """
        toTime64OrZero(x)

        Args:
        - `x` — A string representation of a time with subsecond precision. [`String`](/sql-reference/data-types/string)

        Returns a Time64 value if successful, otherwise `00:00:00.000`. [`Time64`](/sql-reference/data-types/time64)
        """
        return Function("toTime64OrZero", *to_args(locals()))
    
    @staticmethod
    def toTimeOrNull(x: Any) -> Function:
        """
        toTimeOrNull(x)

        Args:
        - `x` — A string representation of a time. [`String`](/sql-reference/data-types/string)

        Returns a Time value if successful, otherwise `NULL`. [`Time`](/sql-reference/data-types/time) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toTimeOrNull", *to_args(locals()))
    
    @staticmethod
    def toTimeOrZero(x: Any) -> Function:
        """
        toTimeOrZero(x)

        Args:
        - `x` — A string representation of a time. [`String`](/sql-reference/data-types/string)

        Returns a Time value if successful, otherwise `00:00:00`. [`Time`](/sql-reference/data-types/time)
        """
        return Function("toTimeOrZero", *to_args(locals()))
    
    @staticmethod
    def toTimeWithFixedDate(date: Any, timezone: Any | None = None) -> Function:
        """
        toTimeWithFixedDate(date[, timezone])

        Args:
        - `date` — Date to convert to a time. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the returned value. [`String`](/sql-reference/data-types/string)

        Returns the time component of a date or date with time in the form of an offset to a fixed point in time (selected as 1970-01-02, currently). [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("toTimeWithFixedDate", *to_args(locals()))
    
    @staticmethod
    def toTimezone(datetime: Any, timezone: Any) -> Function:
        """
        toTimezone(datetime, timezone)

        Args:
        - `date` — The value to convert. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — The target time zone name. [`String`](/sql-reference/data-types/string)

        Returns the same timestamp as the input, but with the specified time zone [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toTimezone", *to_args(locals()))
    
    @staticmethod
    def toTypeName(x: Any) -> Function:
        """
        toTypeName(x)

        Args:
        - `x` — A value of arbitrary type. [`Any`](/sql-reference/data-types)

        Returns the data type name of the input value. [`String`](/sql-reference/data-types/string)
        """
        return Function("toTypeName", *to_args(locals()))
    
    @staticmethod
    def toUInt128(expr: Any) -> Function:
        """
        toUInt128(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 128-bit unsigned integer value. [`UInt128`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt128", *to_args(locals()))
    
    @staticmethod
    def toUInt128OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toUInt128OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`UInt128`](/sql-reference/data-types/int-uint)

        Returns a value of type UInt128 if successful, otherwise returns the default value if passed, or 0 if not. [`UInt128`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt128OrDefault", *to_args(locals()))
    
    @staticmethod
    def toUInt128OrNull(x: Any) -> Function:
        """
        toUInt128OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt128, otherwise `NULL` if the conversion is unsuccessful. [`UInt128`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUInt128OrNull", *to_args(locals()))
    
    @staticmethod
    def toUInt128OrZero(x: Any) -> Function:
        """
        toUInt128OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt128, otherwise `0` if the conversion is unsuccessful. [`UInt128`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt128OrZero", *to_args(locals()))
    
    @staticmethod
    def toUInt16(expr: Any) -> Function:
        """
        toUInt16(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 16-bit unsigned integer value. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt16", *to_args(locals()))
    
    @staticmethod
    def toUInt16OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toUInt16OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`UInt16`](/sql-reference/data-types/int-uint)

        Returns a value of type UInt16 if successful, otherwise returns the default value if passed, or 0 if not. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt16OrDefault", *to_args(locals()))
    
    @staticmethod
    def toUInt16OrNull(x: Any) -> Function:
        """
        toUInt16OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type `UInt16`, otherwise `NULL` if the conversion is unsuccessful. [`UInt16`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUInt16OrNull", *to_args(locals()))
    
    @staticmethod
    def toUInt16OrZero(x: Any) -> Function:
        """
        toUInt16OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt16, otherwise `0` if the conversion is unsuccessful. [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt16OrZero", *to_args(locals()))
    
    @staticmethod
    def toUInt256(expr: Any) -> Function:
        """
        toUInt256(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 256-bit unsigned integer value. [`UInt256`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt256", *to_args(locals()))
    
    @staticmethod
    def toUInt256OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toUInt256OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`UInt256`](/sql-reference/data-types/int-uint)

        Returns a value of type UInt256 if successful, otherwise returns the default value if passed, or 0 if not. [`UInt256`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt256OrDefault", *to_args(locals()))
    
    @staticmethod
    def toUInt256OrNull(x: Any) -> Function:
        """
        toUInt256OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt256, otherwise `NULL` if the conversion is unsuccessful. [`UInt256`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUInt256OrNull", *to_args(locals()))
    
    @staticmethod
    def toUInt256OrZero(x: Any) -> Function:
        """
        toUInt256OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt256, otherwise `0` if the conversion is unsuccessful. [`UInt256`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt256OrZero", *to_args(locals()))
    
    @staticmethod
    def toUInt32(expr: Any) -> Function:
        """
        toUInt32(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 32-bit unsigned integer value. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt32", *to_args(locals()))
    
    @staticmethod
    def toUInt32OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toUInt32OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`UInt32`](/sql-reference/data-types/int-uint)

        Returns a value of type UInt32 if successful, otherwise returns the default value if passed, or 0 if not. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt32OrDefault", *to_args(locals()))
    
    @staticmethod
    def toUInt32OrNull(x: Any) -> Function:
        """
        toUInt32OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type `UInt32`, otherwise `NULL` if the conversion is unsuccessful. [`UInt32`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUInt32OrNull", *to_args(locals()))
    
    @staticmethod
    def toUInt32OrZero(x: Any) -> Function:
        """
        toUInt32OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt32, otherwise `0` if the conversion is unsuccessful. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt32OrZero", *to_args(locals()))
    
    @staticmethod
    def toUInt64(expr: Any) -> Function:
        """
        toUInt64(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns a 64-bit unsigned integer value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt64", *to_args(locals()))
    
    @staticmethod
    def toUInt64OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toUInt64OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns a value of type UInt64 if successful, otherwise returns the default value if passed, or 0 if not. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt64OrDefault", *to_args(locals()))
    
    @staticmethod
    def toUInt64OrNull(x: Any) -> Function:
        """
        toUInt64OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt64, otherwise `NULL` if the conversion is unsuccessful. [`UInt64`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUInt64OrNull", *to_args(locals()))
    
    @staticmethod
    def toUInt64OrZero(x: Any) -> Function:
        """
        toUInt64OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt64, otherwise `0` if the conversion is unsuccessful. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt64OrZero", *to_args(locals()))
    
    @staticmethod
    def toUInt8(expr: Any) -> Function:
        """
        toUInt8(expr)

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`Expression`](/sql-reference/data-types/special-data-types/expression)

        Returns an 8-bit unsigned integer value. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt8", *to_args(locals()))
    
    @staticmethod
    def toUInt8OrDefault(expr: Any, default: Any | None = None) -> Function:
        """
        toUInt8OrDefault(expr[, default])

        Args:
        - `expr` — Expression returning a number or a string representation of a number. [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float)
        - `default` — Optional. The default value to return if parsing is unsuccessful. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a value of type UInt8 if successful, otherwise returns the default value if passed, or 0 if not. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt8OrDefault", *to_args(locals()))
    
    @staticmethod
    def toUInt8OrNull(x: Any) -> Function:
        """
        toUInt8OrNull(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt8, otherwise `NULL` if the conversion is unsuccessful. [`UInt8`](/sql-reference/data-types/int-uint) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUInt8OrNull", *to_args(locals()))
    
    @staticmethod
    def toUInt8OrZero(x: Any) -> Function:
        """
        toUInt8OrZero(x)

        Args:
        - `x` — A String representation of a number. [`String`](/sql-reference/data-types/string)

        Returns a value of type UInt8, otherwise `0` if the conversion is unsuccessful. [`UInt8`](/sql-reference/data-types/int-uint)
        """
        return Function("toUInt8OrZero", *to_args(locals()))
    
    @staticmethod
    def toUTCTimestamp(datetime: Any, time_zone: Any) -> Function:
        """
        toUTCTimestamp(datetime, time_zone)

        Args:
        - `datetime` — A date or date with time type const value or an expression. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `time_zone` — A String type const value or an expression representing the time zone. [`String`](/sql-reference/data-types/string)

        Returns a date or date with time in UTC timezone. [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        """
        return Function("toUTCTimestamp", *to_args(locals()))
    
    @staticmethod
    def toUUID(string: Any) -> Function:
        """
        toUUID(string)

        Args:
        - `string` — UUID as a string. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns a UUID from the string representation of the UUID. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("toUUID", *to_args(locals()))
    
    @staticmethod
    def toUUIDOrDefault(string: Any, default: Any) -> Function:
        """
        toUUIDOrDefault(string, default)

        Args:
        - `string` — String of 36 characters or FixedString(36) to be converted to UUID. - `default` — UUID value to be returned if the first argument cannot be converted to UUID type. 
        Returns the converted UUID if successful, or the default UUID if conversion fails. [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("toUUIDOrDefault", *to_args(locals()))
    
    @staticmethod
    def toUUIDOrNull(x: Any) -> Function:
        """
        toUUIDOrNull(x)

        Args:
        - `x` — A string representation of a UUID. [`String`](/sql-reference/data-types/string)

        Returns a UUID value if successful, otherwise `NULL`. [`UUID`](/sql-reference/data-types/uuid) or [`NULL`](/sql-reference/syntax#null)
        """
        return Function("toUUIDOrNull", *to_args(locals()))
    
    @staticmethod
    def toUUIDOrZero(x: Any) -> Function:
        """
        toUUIDOrZero(x)

        Args:
        - `x` — A string representation of a UUID. [`String`](/sql-reference/data-types/string)

        Returns a UUID value if successful, otherwise zero UUID (`00000000-0000-0000-0000-000000000000`). [`UUID`](/sql-reference/data-types/uuid)
        """
        return Function("toUUIDOrZero", *to_args(locals()))
    
    @staticmethod
    def toUnixTimestamp(date: Any, timezone: Any | None = None) -> Function:
        """
        toUnixTimestamp(date[, timezone])

        Args:
        - `date` — Value to convert. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64) or [`String`](/sql-reference/data-types/string)
        - `timezone` — Optional. Timezone to use for conversion. If not specified, the server's timezone is used. [`String`](/sql-reference/data-types/string)

        Returns the Unix timestamp. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toUnixTimestamp", *to_args(locals()))
    
    @staticmethod
    def toUnixTimestamp64Micro(value: Any) -> Function:
        """
        toUnixTimestamp64Micro(value)

        Args:
        - `value` — DateTime64 value with any precision. [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns a Unix timestamp in microseconds. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUnixTimestamp64Micro", *to_args(locals()))
    
    @staticmethod
    def toUnixTimestamp64Milli(value: Any) -> Function:
        """
        toUnixTimestamp64Milli(value)

        Args:
        - `value` — DateTime64 value with any precision. [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns a Unix timestamp in milliseconds. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUnixTimestamp64Milli", *to_args(locals()))
    
    @staticmethod
    def toUnixTimestamp64Nano(value: Any) -> Function:
        """
        toUnixTimestamp64Nano(value)

        Args:
        - `value` — DateTime64 value with any precision. [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns a Unix timestamp in nanoseconds. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUnixTimestamp64Nano", *to_args(locals()))
    
    @staticmethod
    def toUnixTimestamp64Second(value: Any) -> Function:
        """
        toUnixTimestamp64Second(value)

        Args:
        - `value` — DateTime64 value with any precision. [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns a Unix timestamp in seconds. [`Int64`](/sql-reference/data-types/int-uint)
        """
        return Function("toUnixTimestamp64Second", *to_args(locals()))
    
    @staticmethod
    def toValidUTF8(s: Any) -> Function:
        """
        toValidUTF8(s)

        Args:
        - `s` — Any set of bytes represented as the String data type object. [`String`](/sql-reference/data-types/string)

        Returns a valid UTF-8 string. [`String`](/sql-reference/data-types/string)
        """
        return Function("toValidUTF8", *to_args(locals()))
    
    @staticmethod
    def toWeek(datetime: Any, mode: Any | None = None, time_zone: Any | None = None) -> Function:
        """
        toWeek(datetime[, mode[, time_zone]])

        Args:
        - `datetime` — Date or date with time to get the week number from. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `mode` — Optional. A mode `0` to `9` determines the first day of the week and the range of the week number. Default `0`. - `time_zone` — Optional. Time zone. [`String`](/sql-reference/data-types/string)

        Returns the week number according to the specified mode. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toWeek", *to_args(locals()))
    
    @staticmethod
    def toYYYYMM(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toYYYYMM(datetime[, timezone])

        Args:
        - `datetime` — A date or date with time to convert. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the conversion. If provided, the timezone must be a string constant. [`String`](/sql-reference/data-types/string)

        Returns a UInt32 number containing the year and month number (YYYY * 100 + MM). [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toYYYYMM", *to_args(locals()))
    
    @staticmethod
    def toYYYYMMDD(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toYYYYMMDD(datetime[, timezone])

        Args:
        - `datetime` — A date or date with time to convert. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the conversion. If provided, the timezone must be a string constant. [`String`](/sql-reference/data-types/string)

        Returns a `UInt32` number containing the year, month and day (YYYY * 10000 + MM * 100 + DD). [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toYYYYMMDD", *to_args(locals()))
    
    @staticmethod
    def toYYYYMMDDhhmmss(datetime: Any, timezone: Any | None = None) -> Function:
        """
        toYYYYMMDDhhmmss(datetime[, timezone])

        Args:
        - `datetime` — Date or date with time to convert. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)
        - `timezone` — Optional. Timezone for the conversion. If provided, the timezone must be a string constant. [`String`](/sql-reference/data-types/string)

        Returns a `UInt64` number containing the year, month, day, hour, minute and second (YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss). [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("toYYYYMMDDhhmmss", *to_args(locals()))
    
    @staticmethod
    def toYear(datetime: Any) -> Function:
        """
        toYear(datetime)

        Args:
        - `datetime` — Date or date with time to get the year from. [`Date`](/sql-reference/data-types/date) or [`Date32`](/sql-reference/data-types/date32) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Returns the year of the given Date or DateTime [`UInt16`](/sql-reference/data-types/int-uint)
        """
        return Function("toYear", *to_args(locals()))
    
    @staticmethod
    def toYearNumSinceEpoch(date: Any) -> Function:
        """
        toYearNumSinceEpoch(date)

        Args:
        - `date` — A date or date with time to convert. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`DateTime64`](/sql-reference/data-types/datetime64)

        Positive integer
        """
        return Function("toYearNumSinceEpoch", *to_args(locals()))
    
    @staticmethod
    def toYearWeek(datetime: Any, mode: Any | None = None, timezone: Any | None = None) -> Function:
        """
        toYearWeek(datetime[, mode[, timezone]])

        Args:
        - `datetime` — Date or date with time to get the year and week of. [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `mode` — Optional. A mode `0` to `9` determines the first day of the week and the range of the week number. Default `0`. - `timezone` — Optional. Time zone. [`String`](/sql-reference/data-types/string)

        Returns year and week number as a combined integer value. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("toYearWeek", *to_args(locals()))
    
    @staticmethod
    def today() -> Function:
        """
        today()

        
        Returns the current date [`Date`](/sql-reference/data-types/date)
        """
        return Function("today", *to_args(locals()))
    
    @staticmethod
    def tokens(value: Any) -> Function:
        """
        tokens(value) -- 'splitByNonAlpha' tokenizer
        tokens(value, 'splitByNonAlpha')
        tokens(value, 'splitByString'[, separators])
        tokens(value, 'ngrams'[, n])
        tokens(value, 'sparseGrams'[, min_length, max_length[, min_cutoff_length]])
        tokens(value, 'array')
        tokens(value, 'unicode_word'[, stop_words])

        Args:
        - `value` — The input string. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `tokenizer` — The tokenizer to use. Valid arguments are `splitByNonAlpha`, `ngrams`, `splitByString`, `array`, `sparseGrams`, and `unicode_word`. Optional, if not set explicitly, defaults to `splitByNonAlpha`. [`const String`](/sql-reference/data-types/string)
        - `n` — Only relevant if argument `tokenizer` is `ngrams`: An optional parameter which defines the length of the ngrams. If not set explicitly, defaults to `3`. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `separators` — Only relevant if argument `tokenizer` is `split`: An optional parameter which defines the separator strings. If not set explicitly, defaults to `[' ']`. [`const Array(String)`](/sql-reference/data-types/array)
        - `min_length` — Only relevant if argument `tokenizer` is `sparseGrams`: An optional parameter which defines the minimum gram length, defaults to 3. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `max_length` — Only relevant if argument `tokenizer` is `sparseGrams`: An optional parameter which defines the maximum gram length, defaults to 100. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `min_cutoff_length` — Only relevant if argument `tokenizer` is `sparseGrams`: An optional parameter which defines the minimum cutoff length. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `stop_words` — Only relevant if argument `tokenizer` is `unicode_word`: An optional parameter which defines the stop words. If not set explicitly, defaults to common CJK punctuation marks. [`const Array(String)`](/sql-reference/data-types/array)

        Returns the resulting array of tokens from input string. [`Array`](/sql-reference/data-types/array)
        """
        return Function("tokens", *to_args(locals()))
    
    @staticmethod
    def tokensForLikePattern(value: Any, tokenizer: Any | None = None, tokenizer_specific_arguments: Any | None = None) -> Function:
        """
        tokensForLikePattern(value[, tokenizer[, tokenizer_specific_arguments...]])

        Args:
        - `value` — The input string. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)
        - `tokenizer` — The tokenizer to use. Valid arguments are `splitByNonAlpha`, `ngrams`, `splitByString`, `array`, `sparseGrams`, and `unicode_word`. Optional, if not set explicitly, defaults to `splitByNonAlpha`. [`const String`](/sql-reference/data-types/string)
        - `n` — Only relevant if argument `tokenizer` is `ngrams`: An optional parameter which defines the length of the ngrams. If not set explicitly, defaults to `3`. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `separators` — Only relevant if argument `tokenizer` is `split`: An optional parameter which defines the separator strings. If not set explicitly, defaults to `[' ']`. [`const Array(String)`](/sql-reference/data-types/array)
        - `min_length` — Only relevant if argument `tokenizer` is `sparseGrams`: An optional parameter which defines the minimum gram length, defaults to 3. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `max_length` — Only relevant if argument `tokenizer` is `sparseGrams`: An optional parameter which defines the maximum gram length, defaults to 100. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `min_cutoff_length` — Only relevant if argument `tokenizer` is `sparseGrams`: An optional parameter which defines the minimum cutoff length. [`const UInt8`](/sql-reference/data-types/int-uint)
        - `stop_words` — Only relevant if argument `tokenizer` is `unicode_word`: An optional parameter which defines the stop words. If not set explicitly, defaults to common CJK punctuation marks. [`const Array(String)`](/sql-reference/data-types/array)

        Returns the resulting array of tokens from input string. [`Array`](/sql-reference/data-types/array)
        """
        return Function("tokensForLikePattern", *to_args(locals()))
    
    @staticmethod
    def topK(N: Any) -> Function:
        """
        topK(N)(column)
        topK(N, load_factor)(column)
        topK(N, load_factor, 'counts')(column)

        Args:
        - `column` — The name of the column for which to find the most frequent values. [`String`](/sql-reference/data-types/string)

        Returns an array of the approximately most frequent values, sorted in descending order of approximate frequency. [`Array`](/sql-reference/data-types/array)
        """
        return Function("topK", *to_args(locals()))
    
    @staticmethod
    def topKWeighted(N: Any) -> Function:
        """
        topKWeighted(N)(column, weight)
        topKWeighted(N, load_factor)(column, weight)
        topKWeighted(N, load_factor, 'counts')(column, weight)

        Args:
        - `column` — The name of the column for which to find the most frequent values. - `weight` — The weight. Every value is accounted `weight` times for frequency calculation. [`UInt64`](/sql-reference/data-types/int-uint)

        Returns an array of the values with maximum approximate sum of weights. [`Array`](/sql-reference/data-types/array)
        """
        return Function("topKWeighted", *to_args(locals()))
    
    @staticmethod
    def topLevelDomain(url: Any) -> Function:
        """
        topLevelDomain(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Returns the domain name if the input string can be parsed as a URL. Otherwise, an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("topLevelDomain", *to_args(locals()))
    
    @staticmethod
    def topLevelDomainRFC(url: Any) -> Function:
        """
        topLevelDomainRFC(url)

        Args:
        - `url` — URL. [`String`](/sql-reference/data-types/string)

        Domain name if the input string can be parsed as a URL. Otherwise, an empty string. [`String`](/sql-reference/data-types/string)
        """
        return Function("topLevelDomainRFC", *to_args(locals()))
    
    @staticmethod
    def transactionID() -> Function:
        """
        transactionID()

        
        Returns a tuple consisting of `start_csn`, `local_tid` and `host_id`.
        - `start_csn`: Global sequential number, the newest commit timestamp that was seen when this transaction began.
        - `local_tid`: Local sequential number that is unique for each transaction started by this host within a specific start_csn.
        - `host_id`: UUID of the host that has started this transaction.
             [`Tuple(UInt64, UInt64, UUID)`](/sql-reference/data-types/tuple)
        """
        return Function("transactionID", *to_args(locals()))
    
    @staticmethod
    def transactionLatestSnapshot() -> Function:
        """
        transactionLatestSnapshot()

        
        Returns the latest snapshot (CSN) of a transaction. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("transactionLatestSnapshot", *to_args(locals()))
    
    @staticmethod
    def transactionOldestSnapshot() -> Function:
        """
        transactionOldestSnapshot()

        
        Returns the oldest snapshot (CSN) of a transaction. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("transactionOldestSnapshot", *to_args(locals()))
    
    @staticmethod
    def transform(x: Any, array_from: Any, array_to: Any, default: Any | None = None) -> Function:
        """
        transform(x, array_from, array_to[, default])

        Args:
        - `x` — Value to transform. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)
        - `array_from` — Constant array of values to search for matches. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Array(Decimal)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array) or [`Array(String)`](/sql-reference/data-types/array) or [`Array(Date)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `array_to` — Constant array of values to return for corresponding matches in `array_from`. [`Array((U)Int*)`](/sql-reference/data-types/array) or [`Array(Decimal)`](/sql-reference/data-types/array) or [`Array(Float*)`](/sql-reference/data-types/array) or [`Array(String)`](/sql-reference/data-types/array) or [`Array(Date)`](/sql-reference/data-types/array) or [`Array(DateTime)`](/sql-reference/data-types/array)
        - `default` — Optional. Value to return if `x` is not found in `array_from`. If omitted, returns x unchanged. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Decimal`](/sql-reference/data-types/decimal) or [`Float*`](/sql-reference/data-types/float) or [`String`](/sql-reference/data-types/string) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime)

        Returns the corresponding value from `array_to` if x matches an element in `array_from`, otherwise returns default (if provided) or x (if default not provided). [`Any`](/sql-reference/data-types)
        """
        return Function("transform", *to_args(locals()))
    
    @staticmethod
    def translate(s: Any, from_: Any, to: Any) -> Function:
        """
        translate(s, from, to)

        Args:
        - `s` — The input string to translate. [`String`](/sql-reference/data-types/string)
        - `from` — A constant ASCII string containing characters to replace. [`const String`](/sql-reference/data-types/string)
        - `to` — A constant ASCII string containing replacement characters. [`const String`](/sql-reference/data-types/string)

        Returns a string with character translations applied. [`String`](/sql-reference/data-types/string)
        """
        return Function("translate", *to_args(locals()))
    
    @staticmethod
    def translateUTF8(s: Any, from_: Any, to: Any) -> Function:
        """
        translateUTF8(s, from, to)

        Args:
        - `s` — UTF-8 input string to translate. [`String`](/sql-reference/data-types/string)
        - `from` — A constant UTF-8 string containing characters to replace. [`const String`](/sql-reference/data-types/string)
        - `to` — A constant UTF-8 string containing replacement characters. [`const String`](/sql-reference/data-types/string)

        Returns a `String` data type value. [`String`](/sql-reference/data-types/string)
        """
        return Function("translateUTF8", *to_args(locals()))
    
    @staticmethod
    def trimBoth(s: Any, trim_characters: Any | None = None) -> Function:
        """
        trimBoth(s[, trim_characters])

        Args:
        - `s` — String to trim. [`String`](/sql-reference/data-types/string)
        - `trim_characters` — Optional. Characters to trim. If not specified, common whitespace characters are removed. [`String`](/sql-reference/data-types/string)

        Returns the string with specified characters trimmed from both ends. [`String`](/sql-reference/data-types/string)
        """
        return Function("trimBoth", *to_args(locals()))
    
    @staticmethod
    def trimLeft(input: Any, trim_characters: Any | None = None) -> Function:
        """
        trimLeft(input[, trim_characters])

        Args:
        - `input` — String to trim. [`String`](/sql-reference/data-types/string)
        - `trim_characters` — Optional. Characters to trim. If not specified, common whitespace characters are removed. [`String`](/sql-reference/data-types/string)

        Returns the string with specified characters trimmed from the left. [`String`](/sql-reference/data-types/string)
        """
        return Function("trimLeft", *to_args(locals()))
    
    @staticmethod
    def trimRight(s: Any, trim_characters: Any | None = None) -> Function:
        """
        trimRight(s[, trim_characters])

        Args:
        - `s` — String to trim. [`String`](/sql-reference/data-types/string)
        - `trim_characters` — Optional characters to trim. If not specified, common whitespace characters are removed. [`String`](/sql-reference/data-types/string)

        Returns the string with specified characters trimmed from the right. [`String`](/sql-reference/data-types/string)
        """
        return Function("trimRight", *to_args(locals()))
    
    @staticmethod
    def trunc(x: Any, N: Any | None = None) -> Function:
        """
        truncate(x[, N])

        Args:
        - `x` — The value to round. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        - `N` — Optional. The number of decimal places to round to. Defaults to zero, which means rounding to an integer. [`(U)Int*`](/sql-reference/data-types/int-uint)

        Returns a rounded number of the same type as `x`. [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal) or [`(U)Int*`](/sql-reference/data-types/int-uint)
        """
        return Function("trunc", *to_args(locals()))
    
    @staticmethod
    def tryBase32Decode(encoded: Any) -> Function:
        """
        tryBase32Decode(encoded)

        Args:
        - `encoded` — String column or constant to decode. If the string is not valid Base32-encoded, returns an empty string in case of error. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("tryBase32Decode", *to_args(locals()))
    
    @staticmethod
    def tryBase58Decode(encoded: Any) -> Function:
        """
        tryBase58Decode(encoded)

        Args:
        - `encoded` — String column or constant. If the string is not valid Base58-encoded, returns an empty string in case of error. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("tryBase58Decode", *to_args(locals()))
    
    @staticmethod
    def tryBase64Decode(encoded: Any) -> Function:
        """
        tryBase64Decode(encoded)

        Args:
        - `encoded` — String column or constant to decode. If the string is not valid Base64-encoded, returns an empty string in case of error. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("tryBase64Decode", *to_args(locals()))
    
    @staticmethod
    def tryBase64URLDecode(encoded: Any) -> Function:
        """
        tryBase64URLDecode(encoded)

        Args:
        - `encoded` — String column or constant to decode. If the string is not valid Base64-encoded, returns an empty string in case of error. [`String`](/sql-reference/data-types/string)

        Returns a string containing the decoded value of the argument. [`String`](/sql-reference/data-types/string)
        """
        return Function("tryBase64URLDecode", *to_args(locals()))
    
    @staticmethod
    def tryDecrypt(mode: Any, ciphertext: Any, key: Any, iv: Any | None = None, aad: Any | None = None) -> Function:
        """
        tryDecrypt(mode, ciphertext, key[, iv, aad])

        Args:
        - `mode` — Decryption mode. [`String`](/sql-reference/data-types/string)
        - `ciphertext` — Encrypted text that should be decrypted. [`String`](/sql-reference/data-types/string)
        - `key` — Decryption key. [`String`](/sql-reference/data-types/string)
        - `iv` — Optional. Initialization vector. Required for `-gcm` modes, optional for other modes. [`String`](/sql-reference/data-types/string)
        - `aad` — Optional. Additional authenticated data. Won't decrypt if this value is incorrect. Works only in `-gcm` modes, for other modes throws an exception. [`String`](/sql-reference/data-types/string)

        Returns the decrypted String, or `NULL` if decryption fails. [`Nullable(String)`](/sql-reference/data-types/nullable)
        """
        return Function("tryDecrypt", *to_args(locals()))
    
    @staticmethod
    def tryIdnaEncode(s: Any) -> Function:
        """
        tryIdnaEncode(s)

        Args:
        - `s` — Input string. [`String`](/sql-reference/data-types/string)

        Returns an ASCII representation of the input string according to the IDNA mechanism of the input value, or empty string if input is invalid. [`String`](/sql-reference/data-types/string)
        """
        return Function("tryIdnaEncode", *to_args(locals()))
    
    @staticmethod
    def tryPunycodeDecode(s: Any) -> Function:
        """
        tryPunycodeDecode(s)

        Args:
        - `s` — Punycode-encoded string. [`String`](/sql-reference/data-types/string)

        Returns the plaintext of the input value, or empty string if input is invalid. [`String`](/sql-reference/data-types/string)
        """
        return Function("tryPunycodeDecode", *to_args(locals()))
    
    @staticmethod
    def tumble(time_attr: Any, interval: Any, timezone: Any | None = None) -> Function:
        """
        tumble(time_attr, interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `interval` — Window interval in Interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the inclusive lower and exclusive upper bound of the corresponding tumbling window. [`Tuple(DateTime, DateTime)`](/sql-reference/data-types/tuple)
        """
        return Function("tumble", *to_args(locals()))
    
    @staticmethod
    def tumbleEnd(time_attr: Any, interval: Any, timezone: Any | None = None) -> Function:
        """
        tumbleEnd(time_attr, interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `interval` — Window interval in Interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the exclusive upper bound of the corresponding tumbling window. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("tumbleEnd", *to_args(locals()))
    
    @staticmethod
    def tumbleStart(time_attr: Any, interval: Any, timezone: Any | None = None) -> Function:
        """
        tumbleStart(time_attr, interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `interval` — Window interval in Interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the inclusive lower bound of the corresponding tumbling window. [`DateTime`](/sql-reference/data-types/datetime)
        """
        return Function("tumbleStart", *to_args(locals()))
    
    @staticmethod
    def tuple(t1: Any | None = None, t2: Any | None = None) -> Function:
        """
        tuple([t1[, t2[ ...]])

        
        
        """
        return Function("tuple", *to_args(locals()))
    
    @staticmethod
    def tupleConcat(tuple1: Any, tuple2: Any | None = None) -> Function:
        """
        tupleConcat(tuple1[, tuple2, [...]])

        Args:
        - `tupleN` — Arbitrary number of arguments of Tuple type. [`Tuple(T)`](/sql-reference/data-types/tuple)

        Returns a tuple containing all elements from the input tuples. [`Tuple(T)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleConcat", *to_args(locals()))
    
    @staticmethod
    def tupleDivide(t1: Any, t2: Any) -> Function:
        """
        tupleDivide(t1, t2)

        Args:
        - `t1` — First tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `t2` — Second tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns tuple with the result of division. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleDivide", *to_args(locals()))
    
    @staticmethod
    def tupleDivideByNumber(tuple: Any, number: Any) -> Function:
        """
        tupleDivideByNumber(tuple, number)

        Args:
        - `tuple` — Tuple to divide. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `number` — Divider. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple with divided elements. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleDivideByNumber", *to_args(locals()))
    
    @staticmethod
    def tupleElement(tuple: Any, index: Any, name: Any, default_value: Any | None = None) -> Function:
        """
        tupleElement(tuple, index|name[, default_value])

        Args:
        - `tuple` — A tuple or array of tuples. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(Tuple(T))`](/sql-reference/data-types/array)
        - `index` — Column index, starting from 1. [`const UInt8/16/32/64`](/sql-reference/data-types/int-uint)
        - `name` — Name of the element. [`const String`](/sql-reference/data-types/string)
        - `default_value` — Default value returned when index is out of bounds or element doesn't exist. [`Any`](/sql-reference/data-types)

        Returns the element at the specified index or name. [`Any`](/sql-reference/data-types)
        """
        return Function("tupleElement", *to_args(locals()))
    
    @staticmethod
    def tupleHammingDistance(t1: Any, t2: Any) -> Function:
        """
        tupleHammingDistance(t1, t2)

        Args:
        - `t1` — First tuple. [`Tuple(*)`](/sql-reference/data-types/tuple)
        - `t2` — Second tuple. [`Tuple(*)`](/sql-reference/data-types/tuple)

        Returns the Hamming distance. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)
        """
        return Function("tupleHammingDistance", *to_args(locals()))
    
    @staticmethod
    def tupleIntDiv(tuple_num: Any, tuple_div: Any) -> Function:
        """
        tupleIntDiv(tuple_num, tuple_div)

        Args:
        - `tuple_num` — Tuple of numerator values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `tuple_div` — Tuple of divisor values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns a tuple of the quotients. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleIntDiv", *to_args(locals()))
    
    @staticmethod
    def tupleIntDivByNumber(tuple_num: Any, div: Any) -> Function:
        """
        tupleIntDivByNumber(tuple_num, div)

        Args:
        - `tuple_num` — Tuple of numerator values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `div` — The divisor value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple of the quotients. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleIntDivByNumber", *to_args(locals()))
    
    @staticmethod
    def tupleIntDivOrZero(tuple_num: Any, tuple_div: Any) -> Function:
        """
        tupleIntDivOrZero(tuple_num, tuple_div)

        Args:
        - `tuple_num` — Tuple of numerator values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `tuple_div` — Tuple of divisor values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns tuple of the quotients. Returns 0 for quotients where the divisor is 0. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleIntDivOrZero", *to_args(locals()))
    
    @staticmethod
    def tupleIntDivOrZeroByNumber(tuple_num: Any, div: Any) -> Function:
        """
        tupleIntDivOrZeroByNumber(tuple_num, div)

        Args:
        - `tuple_num` — Tuple of numerator values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `div` — The divisor value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple of the quotients with `0` for quotients where the divisor is `0`. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleIntDivOrZeroByNumber", *to_args(locals()))
    
    @staticmethod
    def tupleMinus(t1: Any, t2: Any) -> Function:
        """
        tupleMinus(t1, t2)

        Args:
        - `t1` — First tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `t2` — Second tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns a tuple containing the results  of the subtractions. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleMinus", *to_args(locals()))
    
    @staticmethod
    def tupleModulo(tuple_num: Any, tuple_mod: Any) -> Function:
        """
        tupleModulo(tuple_num, tuple_mod)

        Args:
        - `tuple_num` — Tuple of numerator values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `tuple_mod` — Tuple of modulus values. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns tuple of the remainders of division. An error is thrown for division by zero. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleModulo", *to_args(locals()))
    
    @staticmethod
    def tupleModuloByNumber(tuple_num: Any, div: Any) -> Function:
        """
        tupleModuloByNumber(tuple_num, div)

        Args:
        - `tuple_num` — Tuple of numerator elements. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `div` — The divisor value. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns tuple of the remainders of division. An error is thrown for division by zero. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleModuloByNumber", *to_args(locals()))
    
    @staticmethod
    def tupleMultiply(t1: Any, t2: Any) -> Function:
        """
        tupleMultiply(t1, t2)

        Args:
        - `t1` — First tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `t2` — Second tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns a tuple with the results of the multiplications. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleMultiply", *to_args(locals()))
    
    @staticmethod
    def tupleMultiplyByNumber(tuple: Any, number: Any) -> Function:
        """
        tupleMultiplyByNumber(tuple, number)

        Args:
        - `tuple` — Tuple to multiply. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `number` — Multiplier. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a tuple with multiplied elements. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleMultiplyByNumber", *to_args(locals()))
    
    @staticmethod
    def tupleNames(tuple: Any) -> Function:
        """
        tupleNames(tuple)

        
        
        """
        return Function("tupleNames", *to_args(locals()))
    
    @staticmethod
    def tupleNegate(t: Any) -> Function:
        """
        tupleNegate(t)

        Args:
        - `t` — Tuple to negate. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns a tuple with the result of negation. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tupleNegate", *to_args(locals()))
    
    @staticmethod
    def tuplePlus(t1: Any, t2: Any) -> Function:
        """
        tuplePlus(t1, t2)

        Args:
        - `t1` — First tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        - `t2` — Second tuple. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)

        Returns a tuple containing the sums of corresponding input tuple arguments. [`Tuple((U)Int*)`](/sql-reference/data-types/tuple) or [`Tuple(Float*)`](/sql-reference/data-types/tuple) or [`Tuple(Decimal)`](/sql-reference/data-types/tuple)
        """
        return Function("tuplePlus", *to_args(locals()))
    
    @staticmethod
    def tupleToNameValuePairs(tuple: Any) -> Function:
        """
        tupleToNameValuePairs(tuple)

        Args:
        - `tuple` — Named tuple with any types of values. [`Tuple(n1 T1[, n2 T2, ...])`](/sql-reference/data-types/tuple)

        Returns an array with `(name, value)` pairs. [`Array(Tuple(String, T))`](/sql-reference/data-types/array)
        """
        return Function("tupleToNameValuePairs", *to_args(locals()))
    
    @staticmethod
    def unbin(arg: Any) -> Function:
        """
        unbin(arg)

        Args:
        - `arg` — A string containing any number of binary digits. [`String`](/sql-reference/data-types/string)

        Returns a binary string (BLOB). [`String`](/sql-reference/data-types/string)
        """
        return Function("unbin", *to_args(locals()))
    
    @staticmethod
    def unhex(arg: Any) -> Function:
        """
        unhex(arg)

        Args:
        - `arg` — A string containing any number of hexadecimal digits. [`String`](/sql-reference/data-types/string) or [`FixedString`](/sql-reference/data-types/fixedstring)

        Returns a binary string (BLOB). [`String`](/sql-reference/data-types/string)
        """
        return Function("unhex", *to_args(locals()))
    
    @staticmethod
    def uniq(x: Any) -> Function:
        """
        uniq(x[, ...])

        Args:
        - `x` — The function takes a variable number of parameters. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a UInt64-type number representing the approximate number of different values. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("uniq", *to_args(locals()))
    
    @staticmethod
    def uniqCombined(HLL_precision: Any) -> Function:
        """
        uniqCombined(HLL_precision)(x[, ...])
        uniqCombined(x[, ...])

        Args:
        - `x` — A variable number of parameters. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a UInt64-type number representing the approximate number of different argument values. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("uniqCombined", *to_args(locals()))
    
    @staticmethod
    def uniqCombined64(HLL_precision: Any) -> Function:
        """
        uniqCombined64(HLL_precision)(x[, ...])
        uniqCombined64(x[, ...])

        Args:
        - `x` — A variable number of parameters. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a UInt64-type number representing the approximate number of different argument values. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("uniqCombined64", *to_args(locals()))
    
    @staticmethod
    def uniqExact(x: Any) -> Function:
        """
        uniqExact(x[, ...])

        Args:
        - `x` — The function takes a variable number of parameters. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns the exact number of different argument values as a UInt64. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("uniqExact", *to_args(locals()))
    
    @staticmethod
    def uniqHLL12(x: Any) -> Function:
        """
        uniqHLL12(x[, ...])

        Args:
        - `x` — The function takes a variable number of parameters. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a UInt64-type number representing the approximate number of different argument values. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("uniqHLL12", *to_args(locals()))
    
    @staticmethod
    def uniqTheta(x: Any) -> Function:
        """
        uniqTheta(x[, ...])

        Args:
        - `x` — The function takes a variable number of parameters. [`Tuple(T)`](/sql-reference/data-types/tuple) or [`Array(T)`](/sql-reference/data-types/array) or [`Date`](/sql-reference/data-types/date) or [`DateTime`](/sql-reference/data-types/datetime) or [`String`](/sql-reference/data-types/string) or [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal`](/sql-reference/data-types/decimal)

        Returns a UInt64-type number representing the approximate number of different argument values. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("uniqTheta", *to_args(locals()))
    
    @staticmethod
    def uniqUpTo(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("uniqUpTo", *to_args(locals()))
    
    @staticmethod
    def upper(s: Any) -> Function:
        """
        upper(s)

        Args:
        - `s` — The string to convert to uppercase. [`String`](/sql-reference/data-types/string)

        Returns an uppercase string from `s`. [`String`](/sql-reference/data-types/string)
        """
        return Function("upper", *to_args(locals()))
    
    @staticmethod
    def upperUTF8(s: Any) -> Function:
        """
        upperUTF8(s)

        Args:
        - `s` — A string type. [`String`](/sql-reference/data-types/string)

        A String data type value. [`String`](/sql-reference/data-types/string)
        """
        return Function("upperUTF8", *to_args(locals()))
    
    @staticmethod
    def uptime() -> Function:
        """
        uptime()

        
        Returns the server uptime in seconds. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("uptime", *to_args(locals()))
    
    @staticmethod
    def validateNestedArraySizes(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("validateNestedArraySizes", *to_args(locals()))
    
    @staticmethod
    def varPop(x: Any) -> Function:
        """
        varPop(x)

        Args:
        - `x` — Population of values to find the population variance of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the population variance of `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("varPop", *to_args(locals()))
    
    @staticmethod
    def varPopStable(x: Any) -> Function:
        """
        varPopStable(x)

        Args:
        - `x` — Population of values to find the population variance of. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the population variance of `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("varPopStable", *to_args(locals()))
    
    @staticmethod
    def varSamp(x: Any) -> Function:
        """
        varSamp(x)

        Args:
        - `x` — The population for which you want to calculate the sample variance. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the sample variance of the input data set `x`. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("varSamp", *to_args(locals()))
    
    @staticmethod
    def varSampStable(x: Any) -> Function:
        """
        varSampStable(x)

        Args:
        - `x` — The population for which you want to calculate the sample variance. [`(U)Int*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)

        Returns the sample variance of the input data set. [`Float64`](/sql-reference/data-types/float)
        """
        return Function("varSampStable", *to_args(locals()))
    
    @staticmethod
    def variantElement(variant: Any, type_name: Any, default_value: Any | None = None) -> Function:
        """
        variantElement(variant, type_name[, default_value])

        Args:
        - `variant` — Variant column. [`Variant`](/sql-reference/data-types/variant)
        - `type_name` — The name of the variant type to extract. [`String`](/sql-reference/data-types/string)
        - `default_value` — The default value that will be used if variant doesn't have variant with specified type. Can be any type. Optional. [`Any`](/sql-reference/data-types)

        Returns a column with the specified variant type extracted from the Variant column. [`Any`](/sql-reference/data-types)
        """
        return Function("variantElement", *to_args(locals()))
    
    @staticmethod
    def variantType(variant: Any) -> Function:
        """
        variantType(variant)

        Args:
        - `variant` — Variant column. [`Variant`](/sql-reference/data-types/variant)

        Returns an Enum column with variant type name for each row. [`Enum`](/sql-reference/data-types/enum)
        """
        return Function("variantType", *to_args(locals()))
    
    @staticmethod
    def version() -> Function:
        """
        version()

        
        Returns the current version of ClickHouse. [`String`](/sql-reference/data-types/string)
        """
        return Function("version", *to_args(locals()))
    
    @staticmethod
    def visibleWidth(x: Any) -> Function:
        """
        visibleWidth(x)

        Args:
        - `x` — A value of any data type. [`Any`](/sql-reference/data-types)

        Returns the approximate width of the value when displayed in text format. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("visibleWidth", *to_args(locals()))
    
    @staticmethod
    def welchTTest(confidence_level: Any | None = None) -> Function:
        """
        welchTTest([confidence_level])(sample_data, sample_index)

        Args:
        - `sample_data` — Sample data. [`Int*`](/sql-reference/data-types/int-uint) or [`UInt*`](/sql-reference/data-types/int-uint) or [`Float*`](/sql-reference/data-types/float) or [`Decimal*`](/sql-reference/data-types/decimal)
        - `sample_index` — Sample index. [`Int*`](/sql-reference/data-types/int-uint) or [`UInt*`](/sql-reference/data-types/int-uint)

        Returns a Tuple with two or four elements (if the optional `confidence_level` is specified): calculated t-statistic, calculated p-value, and optionally calculated confidence-interval-low and confidence-interval-high. [`Tuple(Float64, Float64)`](/sql-reference/data-types/tuple) or [`Tuple(Float64, Float64, Float64, Float64)`](/sql-reference/data-types/tuple)
        """
        return Function("welchTTest", *to_args(locals()))
    
    @staticmethod
    def widthBucket(operand: Any, low: Any, high: Any, count: Any) -> Function:
        """
        widthBucket(operand, low, high, count)

        Args:
        - `operand` — The value for which to determine the bucket. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `low` — The lower bound of the histogram range. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `high` — The upper bound of the histogram range. [`(U)Int8/16/32/64`](/sql-reference/data-types/int-uint)
        - `count` — The number of equal-width buckets. Cannot be zero. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)

        Returns the bucket number as an integer. Returns 0 if operand < low, returns count+1 if operand >= high. [`UInt8/16/32/64`](/sql-reference/data-types/int-uint)
        """
        return Function("widthBucket", *to_args(locals()))
    
    @staticmethod
    def windowFunnel(*args: Any) -> Function:
        """
        

        
        
        """
        return Function("windowFunnel", *to_args(locals()))
    
    @staticmethod
    def windowID(time_attr: Any, interval: Any, timezone: Any | None = None) -> Function:
        """
        windowID(time_attr, interval[, timezone])

        Args:
        - `time_attr` — Date and time. [`DateTime`](/sql-reference/data-types/datetime)
        - `interval` — Window interval in Interval. [`Interval`](/sql-reference/data-types/int-uint)
        - `timezone` — Optional. Timezone name. [`String`](/sql-reference/data-types/string)

        Returns the window identifier of the corresponding window. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("windowID", *to_args(locals()))
    
    @staticmethod
    def wkb(geometry: Any) -> Function:
        """
        wkb(geometry)

        Args:
        - `geometry` — The input geometry type to convert into WKB. 
        
        """
        return Function("wkb", *to_args(locals()))
    
    @staticmethod
    def wkt(geometry: Any) -> Function:
        """
        wkt(geometry)

        Args:
        - `geometry` — Geometry object (Point, Ring, Polygon, MultiPolygon). [`Point`](/sql-reference/data-types/geo#point) or [`Ring`](/sql-reference/data-types/geo#ring) or [`Polygon`](/sql-reference/data-types/geo#polygon) or [`MultiPolygon`](/sql-reference/data-types/geo#multipolygon)

        Returns the WKT string representation of the geometry. [`String`](/sql-reference/data-types/string)
        """
        return Function("wkt", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHash(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHash(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHash", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashArg(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashArg(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` word shingles each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashArg", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashArgCaseInsensitive(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashArgCaseInsensitive(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` word shingles each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashArgCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashArgCaseInsensitiveUTF8(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashArgCaseInsensitiveUTF8(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` word shingles each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashArgCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashArgUTF8(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashArgUTF8(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two tuples with `hashnum` word shingles each. [`Tuple(Tuple(String))`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashArgUTF8", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashCaseInsensitive(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashCaseInsensitive(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashCaseInsensitiveUTF8(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashCaseInsensitiveUTF8(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def wordShingleMinHashUTF8(string: Any, shinglesize: Any | None = None, hashnum: Any | None = None) -> Function:
        """
        wordShingleMinHashUTF8(string[, shinglesize, hashnum])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)
        - `hashnum` — Optional. The number of minimum and maximum hashes used to calculate the result, any number from `1` to `25`. The default value is `6`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns a tuple with two hashes — the minimum and the maximum. [`Tuple(UInt64, UInt64)`](/sql-reference/data-types/tuple)
        """
        return Function("wordShingleMinHashUTF8", *to_args(locals()))
    
    @staticmethod
    def wordShingleSimHash(string: Any, shinglesize: Any | None = None) -> Function:
        """
        wordShingleSimHash(string[, shinglesize])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("wordShingleSimHash", *to_args(locals()))
    
    @staticmethod
    def wordShingleSimHashCaseInsensitive(string: Any, shinglesize: Any | None = None) -> Function:
        """
        wordShingleSimHashCaseInsensitive(string[, shinglesize])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("wordShingleSimHashCaseInsensitive", *to_args(locals()))
    
    @staticmethod
    def wordShingleSimHashCaseInsensitiveUTF8(string: Any, shinglesize: Any | None = None) -> Function:
        """
        wordShingleSimHashCaseInsensitiveUTF8(string[, shinglesize])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("wordShingleSimHashCaseInsensitiveUTF8", *to_args(locals()))
    
    @staticmethod
    def wordShingleSimHashUTF8(string: Any, shinglesize: Any | None = None) -> Function:
        """
        wordShingleSimHashUTF8(string[, shinglesize])

        Args:
        - `string` — String for which to compute the hash. [`String`](/sql-reference/data-types/string)
        - `shinglesize` — Optional. The size of a word shingle, any number from `1` to `25`. The default value is `3`. [`UInt8`](/sql-reference/data-types/int-uint)

        Returns the computed hash value. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("wordShingleSimHashUTF8", *to_args(locals()))
    
    @staticmethod
    def wyHash64(arg: Any) -> Function:
        """
        wyHash64(arg)

        Args:
        - `arg` — String argument for which to compute the hash. [`String`](/sql-reference/data-types/string)

        Returns the computed 64-bit hash value [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("wyHash64", *to_args(locals()))
    
    @staticmethod
    def xor(val1: Any, val2: Any) -> Function:
        """
        xor(val1, val2[, ...])

        Args:
        - `val1, val2[, ...]` — List of at least two values. [`Nullable((U)Int*)`](/sql-reference/data-types/nullable) or [`Nullable(Float*)`](/sql-reference/data-types/nullable)

        Returns:
        - `1`, for two values: if one of the values evaluates to `false` and other does not
        - `0`, for two values: if both values evaluate to `false` or to both `true`
        - `NULL`, if at least one of the inputs is `NULL`.
                 [`Nullable(UInt8)`](/sql-reference/data-types/nullable)
        """
        return Function("xor", *to_args(locals()))
    
    @staticmethod
    def xxHash32(arg: Any) -> Function:
        """
        xxHash32(arg)

        Args:
        - `arg` — Input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the computed 32-bit hash of the input string. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("xxHash32", *to_args(locals()))
    
    @staticmethod
    def xxHash64(arg: Any) -> Function:
        """
        xxHash64(arg)

        Args:
        - `arg` — Input string to hash. [`String`](/sql-reference/data-types/string)

        Returns the computed 64-bit hash of the input string. [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("xxHash64", *to_args(locals()))
    
    @staticmethod
    def xxh3(expr: Any) -> Function:
        """
        xxh3(expr)

        Args:
        - `expr` — A list of expressions of any data type. [`Any`](/sql-reference/data-types)

        Returns the computed 64-bit `xxh3` hash value [`UInt64`](/sql-reference/data-types/int-uint)
        """
        return Function("xxh3", *to_args(locals()))
    
    @staticmethod
    def xxh3_128(expr: Any) -> Function:
        """
        xxh3_128(expr)

        Args:
        - `expr` — A list of expressions of any data type. [`Any`](/sql-reference/data-types)

        Returns the computed 128-bit `xxh3` hash value [`UInt128`](/sql-reference/data-types/int-uint)
        """
        return Function("xxh3_128", *to_args(locals()))
    
    @staticmethod
    def yesterday() -> Function:
        """
        yesterday()

        
        Returns yesterday's date. [`Date`](/sql-reference/data-types/date)
        """
        return Function("yesterday", *to_args(locals()))
    
    @staticmethod
    def zookeeperSessionUptime() -> Function:
        """
        zookeeperSessionUptime()

        
        Returns the uptime of the current ZooKeeper session in seconds. [`UInt32`](/sql-reference/data-types/int-uint)
        """
        return Function("zookeeperSessionUptime", *to_args(locals()))
    

F = FunctionWrapper()