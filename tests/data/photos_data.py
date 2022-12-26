"""Photos fixtures."""
DATA = {
    "query?remapEnums=True&getCurrentSyncToken=True": [
        {
            "data": {
                "query": {"recordType": "CheckIndexingState"},
                "zoneID": {"zoneName": "PrimarySync"},
            },
            "response": {
                "records": [
                    {
                        "recordName": "_5c82ba39-fa99-4f36-ad2a-1a87028f8fa4",
                        "recordType": "CheckIndexingState",
                        "fields": {
                            "progress": {"value": 100, "type": "INT64"},
                            "state": {"value": "FINISHED", "type": "STRING"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "0",
                        "created": {
                            "timestamp": 1629754179814,
                            "userRecordName": "_10",
                            "deviceID": "1",
                        },
                        "modified": {
                            "timestamp": 1629754179814,
                            "userRecordName": "_10",
                            "deviceID": "1",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    }
                ],
                "syncToken": "AQAAAAAAArKjf//////////fSxWSKv5JfZ34edrt875d",
            },
        },
        {
            "data": {
                "query": {"recordType": "CPLAlbumByPositionLive"},
                "zoneID": {"zoneName": "PrimarySync"},
            },
            "response": {
                "records": [
                    # Project-Root-Folder
                    {
                        "recordName": "----Project-Root-Folder----",
                        "recordType": "CPLAlbum",
                        "fields": {
                            "recordModificationDate": {
                                "value": 1611165435221,
                                "type": "TIMESTAMP",
                            },
                            "sortAscending": {"value": 1, "type": "INT64"},
                            "sortType": {"value": 0, "type": "INT64"},
                            "albumType": {"value": 3, "type": "INT64"},
                            "position": {"value": 0, "type": "INT64"},
                            "sortTypeExt": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3mp3",
                        "created": {
                            "timestamp": 1600316906967,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1611168194962,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # Root-Folder
                    {
                        "recordName": "----Root-Folder----",
                        "recordType": "CPLAlbum",
                        "fields": {
                            "recordModificationDate": {
                                "value": 1611165435221,
                                "type": "TIMESTAMP",
                            },
                            "sortAscending": {"value": 1, "type": "INT64"},
                            "sortType": {"value": 0, "type": "INT64"},
                            "albumType": {"value": 3, "type": "INT64"},
                            "position": {"value": 0, "type": "INT64"},
                            "sortTypeExt": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3mp2",
                        "created": {
                            "timestamp": 1442497886351,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "361FF63C0FF75A92666117B37B680CB75643625D4D9DDAA5A6E5876E606350AA",
                        },
                        "modified": {
                            "timestamp": 1611168194962,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # All Photos (Album)
                    {
                        "recordName": "E803E065-D8A4-4398-DE23-23F8FD0886EC",
                        "recordType": "CPLAlbum",
                        "fields": {
                            "recordModificationDate": {
                                "value": 1608493440571,
                                "type": "TIMESTAMP",
                            },
                            "sortAscending": {"value": 1, "type": "INT64"},
                            "sortType": {"value": 0, "type": "INT64"},
                            "albumType": {"value": 0, "type": "INT64"},
                            "albumNameEnc": {
                                "value": "QWxsIFBob3Rvcw==",  # All Photos
                                "type": "ENCRYPTED_BYTES",
                            },
                            "position": {"value": 1063936, "type": "INT64"},
                            "sortTypeExt": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3km2",
                        "created": {
                            "timestamp": 1608493450571,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1608493460571,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "D41A228F-D89E-494A-8EEF-853D461B68CF",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # album-1 (Album)
                    {
                        "recordName": "E803E065-D8A4-4398-DE23-23F8FD0886EB",
                        "recordType": "CPLAlbum",
                        "fields": {
                            "recordModificationDate": {
                                "value": 1608493740571,
                                "type": "TIMESTAMP",
                            },
                            "sortAscending": {"value": 1, "type": "INT64"},
                            "sortType": {"value": 0, "type": "INT64"},
                            "albumType": {"value": 0, "type": "INT64"},
                            "albumNameEnc": {
                                "value": "YWxidW0tMQ==",  # album-1
                                "type": "ENCRYPTED_BYTES",
                            },
                            "position": {"value": 1063936, "type": "INT64"},
                            "sortTypeExt": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3km2",
                        "created": {
                            "timestamp": 1496340770777,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1608493742434,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "D41A228F-D89E-494A-8EEF-853D461B68CF",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # album 2 (Album)
                    {
                        "recordName": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                        "recordType": "CPLAlbum",
                        "fields": {
                            "recordModificationDate": {
                                "value": 1608493740571,
                                "type": "TIMESTAMP",
                            },
                            "sortAscending": {"value": 1, "type": "INT64"},
                            "sortType": {"value": 0, "type": "INT64"},
                            "albumType": {"value": 0, "type": "INT64"},
                            "albumNameEnc": {
                                "value": "YWxidW0gMg==",  # album 2
                                "type": "ENCRYPTED_BYTES",
                            },
                            "position": {"value": 1065984, "type": "INT64"},
                            "sortTypeExt": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3km7",
                        "created": {
                            "timestamp": 1546997094145,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1608493743317,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "D41A228F-D89E-494A-8EEF-853D461B68CF",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                ],
                "syncToken": "AQAAAAAAArKjf//////////fSxWSKv5JfZ34edrt875d",
            },
        },
        {
            "data": {
                # Query to get contents of album 2
                "query": {
                    "filterBy": [
                        {
                            "fieldName": "startRank",
                            "fieldValue": {"type": "INT64", "value": 0},
                            "comparator": "EQUALS",
                        },
                        {
                            "fieldName": "direction",
                            "fieldValue": {"type": "STRING", "value": "ASCENDING"},
                            "comparator": "EQUALS",
                        },
                        {
                            "fieldName": "parentId",
                            "comparator": "EQUALS",
                            "fieldValue": {
                                "type": "STRING",
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                            },
                        },
                    ],
                    "recordType": "CPLContainerRelationLiveByAssetDate",
                },
                "resultsLimit": 200,
                "desiredKeys": [
                    "resJPEGFullWidth",
                    "resJPEGFullHeight",
                    "resJPEGFullFileType",
                    "resJPEGFullFingerprint",
                    "resJPEGFullRes",
                    "resJPEGLargeWidth",
                    "resJPEGLargeHeight",
                    "resJPEGLargeFileType",
                    "resJPEGLargeFingerprint",
                    "resJPEGLargeRes",
                    "resJPEGMedWidth",
                    "resJPEGMedHeight",
                    "resJPEGMedFileType",
                    "resJPEGMedFingerprint",
                    "resJPEGMedRes",
                    "resJPEGThumbWidth",
                    "resJPEGThumbHeight",
                    "resJPEGThumbFileType",
                    "resJPEGThumbFingerprint",
                    "resJPEGThumbRes",
                    "resVidFullWidth",
                    "resVidFullHeight",
                    "resVidFullFileType",
                    "resVidFullFingerprint",
                    "resVidFullRes",
                    "resVidMedWidth",
                    "resVidMedHeight",
                    "resVidMedFileType",
                    "resVidMedFingerprint",
                    "resVidMedRes",
                    "resVidSmallWidth",
                    "resVidSmallHeight",
                    "resVidSmallFileType",
                    "resVidSmallFingerprint",
                    "resVidSmallRes",
                    "resSidecarWidth",
                    "resSidecarHeight",
                    "resSidecarFileType",
                    "resSidecarFingerprint",
                    "resSidecarRes",
                    "itemType",
                    "dataClassType",
                    "filenameEnc",
                    "originalOrientation",
                    "resOriginalWidth",
                    "resOriginalHeight",
                    "resOriginalFileType",
                    "resOriginalFingerprint",
                    "resOriginalRes",
                    "resOriginalAltWidth",
                    "resOriginalAltHeight",
                    "resOriginalAltFileType",
                    "resOriginalAltFingerprint",
                    "resOriginalAltRes",
                    "resOriginalVidComplWidth",
                    "resOriginalVidComplHeight",
                    "resOriginalVidComplFileType",
                    "resOriginalVidComplFingerprint",
                    "resOriginalVidComplRes",
                    "isDeleted",
                    "isExpunged",
                    "dateExpunged",
                    "remappedRef",
                    "recordName",
                    "recordType",
                    "recordChangeTag",
                    "masterRef",
                    "adjustmentRenderType",
                    "assetDate",
                    "addedDate",
                    "isFavorite",
                    "isHidden",
                    "orientation",
                    "duration",
                    "assetSubtype",
                    "assetSubtypeV2",
                    "assetHDRType",
                    "burstFlags",
                    "burstFlagsExt",
                    "burstId",
                    "captionEnc",
                    "locationEnc",
                    "locationV2Enc",
                    "locationLatitude",
                    "locationLongitude",
                    "adjustmentType",
                    "timeZoneOffset",
                    "vidComplDurValue",
                    "vidComplDurScale",
                    "vidComplDispValue",
                    "vidComplDispScale",
                    "vidComplVisibilityState",
                    "customRenderedValue",
                    "containerId",
                    "itemId",
                    "position",
                    "isKeyAsset",
                ],
                "zoneID": {"zoneName": "PrimarySync"},
            },
            "response": {
                "records": [
                    # IMG_3328.JPG
                    {
                        "recordName": "YN1v8eGiHYYZ/aKUkMuGtSf0P1BN",
                        "recordType": "CPLMaster",
                        "fields": {
                            "itemType": {"value": "public.jpeg", "type": "STRING"},
                            "resJPEGThumbFingerprint": {
                                "value": "DmK0xzSiAUSFrAsYYAvby7QHrMDe",
                                "type": "STRING",
                            },
                            "filenameEnc": {
                                "value": "SU1HXzMzMjguSlBH",
                                "type": "ENCRYPTED_BYTES",
                            },
                            "resJPEGMedRes": {
                                "value": {
                                    "fileChecksum": "EeGlt2PppPTgd0Q7mp8GenIugSh7",
                                    "size": 1074354,
                                    "wrappingKey": "amaCdL9Z+QxfzgD4+aYATg==",
                                    "referenceChecksum": "AQYmx+DRYXnMs0tkDZ3rorp4IB99",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/EeGlt2PppPTgd0Q7mp8GenIugSh7AQYmx-DRYXnMs0tkDZ3rorp4IB99/${f}?o=Ai6vEWSVp5w5zaBTm7XvC55prdq006u5yUW5EfZs4KLT&v=1&x=3&a=CAogvhLnXY3DD7gxkuzbuKlak-NMlKvq37s7a-beQRlkZCsSbRCbkq2nty8Ym--IqbcvIgEAUgQugSh6WgR4IB99aiYQWP8altHEtfDsXqRVOJ19O49YwikLbHn5Ha6IeAIHhXVRK7Fpa3ImBoK0z2Usv0QeZBog1G6uVLc1ZapiFVtXuoc52Ijt3dpb4J3VMIA&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=amaCdL9Z-QxfzgD4-aYATg&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=J9LA0hC_xBV3TqYvwg_zAPWPwH8",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "originalOrientation": {"value": 1, "type": "INT64"},
                            "resJPEGMedHeight": {"value": 1559, "type": "INT64"},
                            "resOriginalRes": {
                                "value": {
                                    "fileChecksum": "YN1v8eGiHYYZ/aKUkMuGtSf0P1BN",
                                    "size": 2194253,
                                    "wrappingKey": "Y40xDPUr6DmxfeoSqxaQ7A==",
                                    "referenceChecksum": "AXKVYPcDa+9Mjvnap0ZS+p2Z24V3",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/YN1v8eGiHYYZ_aKUkMuGtSf0P1BNAXKVYPcDa-9Mjvnap0ZS-p2Z24V3/${f}?o=Ame-Q1e_1nWqIn7YG7VfVZk-XAs8bVdcHo-owaNRmfPn&v=1&x=3&a=CAogwS503Q9EkCdnzvD-kLG0VNwrlEmARONCS-hADMtqg1QSbRCckq2nty8YnO-IqbcvIgEAUgT0P1BNWgSZ24V3aiYLdjzdjGLXPtKfjwtH_PG0ralgbDDBOIftNXxyRxdhzz8OuZztNnImb65YPlo1qUOy4i7tW1pcyAZcjqS8kYfxPQD6SKIAKNk3dUid7mE&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=Y40xDPUr6DmxfeoSqxaQ7A&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=X91oiOo0Avp6TR4d27MGupd_cqY",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resJPEGMedFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resJPEGThumbHeight": {"value": 365, "type": "INT64"},
                            "resJPEGThumbWidth": {"value": 472, "type": "INT64"},
                            "resOriginalWidth": {"value": 3100, "type": "INT64"},
                            "resJPEGThumbFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "dataClassType": {"value": 1, "type": "INT64"},
                            "resOriginalFingerprint": {
                                "value": "YN1v8eGiHYYZ/aKUkMuGtSf0P1BN",
                                "type": "STRING",
                            },
                            "resJPEGMedWidth": {"value": 2016, "type": "INT64"},
                            "resJPEGThumbRes": {
                                "value": {
                                    "fileChecksum": "DmK0xzSiAUSFrAsYYAvby7QHrMDe",
                                    "size": 340532,
                                    "wrappingKey": "r7EeA3tyPsWdcECp6X9dHA==",
                                    "referenceChecksum": "AR5TiM9Qko4rHwmoDH1BgNRVZpF4",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/DmK0xzSiAUSFrAsYYAvby7QHrMDeAR5TiM9Qko4rHwmoDH1BgNRVZpF4/${f}?o=AjM3SMy6F9O-5AWTv2HnEp_GiL7ycAx1ls3yOqypKX-3&v=1&x=3&a=CAogiUnx0vJRhNr8Xt_dbOGrxiu8gKNAz_l_8Z5TVGmok64SbRCckq2nty8YnO-IqbcvIgEAUgQHrMObWgRVZpF4aiYwQUojYj2kyD-EyrtVjkw5sVJ60NK0x8nKjsjNXzTYH__dA6VcCHImQduy0Vis9tCiB3ox2KXKiyf3NOaih9TbQ8KfJ8H_8sFzdtXHw8I&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=r7EeA3tyPsWdcECp6X9dHA&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=m2Z7uOxYG9iNHiAZbLm6OE2O6hE",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resOriginalFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resOriginalHeight": {"value": 2398, "type": "INT64"},
                            "resJPEGMedFingerprint": {
                                "value": "EeGlt2PppPTgd0Q7mp8GenIugSh7",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3pjq",
                        "created": {
                            "timestamp": 1596388681827,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1619641691167,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3327.JPG
                    {
                        "recordName": "ENKzBUr+DdmTaP/GEAglTurWtsen",
                        "recordType": "CPLMaster",
                        "fields": {
                            "itemType": {"value": "public.jpeg", "type": "STRING"},
                            "resJPEGThumbFingerprint": {
                                "value": "ASy6f/leU1+xkR1aPmQyvYmwHUpE",
                                "type": "STRING",
                            },
                            "filenameEnc": {
                                "value": "SU1HXzMzMjcuSlBH",
                                "type": "ENCRYPTED_BYTES",
                            },
                            "resJPEGMedRes": {
                                "value": {
                                    "fileChecksum": "NOHzBUr+DdmTaP/SAVglTurWtsen",
                                    "size": 1074354,
                                    "wrappingKey": "eqUQfTajfGXgQHbBJh8Qwg==",
                                    "referenceChecksum": "Ab5Vyk36t2jwuON7WSxvon/DvGtK",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ARKzBUr-DdmTaP_SAVglTurWtsmrAb5Vyk36t2jwuON7WSxvon_DvGtK/${f}?o=AnHR_fOkcKyPuLPOCXcp9C52pM-oZefmc9efp0e0ahAO&v=1&x=3&a=CAogf7lfgZsLeoZdnUfnSzBMLzy9WrbD7vMgHjmY9CI7_uESbRCmkq2nty8Ypu-IqbcvIgEAUgTWtsmrWgTDvGtKaiYANfDoXLBqjbu3_O1AGa62AuKbnBEsqXqysujWIiFYxe-i-AiEb3ImWrZCs4OP45m3SoQL7fh49dD-aHcXkEMAfevtQ6xh5-RH-5bq3sQ&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=eqUQfTajfGXgQHbBJh8Qwg&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=ci4ad9AWukocHK1gYXbJrx-Ok9M",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "originalOrientation": {"value": 1, "type": "INT64"},
                            "resJPEGMedHeight": {"value": 1788, "type": "INT64"},
                            "resOriginalRes": {
                                "value": {
                                    "fileChecksum": "ENKzBUr+DdmTaP/GEAglTurWtsen",
                                    "size": 2194253,
                                    "wrappingKey": "tPtP2Y7mGQ4yOsOCMFG/sg==",
                                    "referenceChecksum": "Ad0I2qxdsqlGuSLlqtTBgoKndHE/",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/AUvKU8j-Z5pfqGI_fe-9tibuqfVRAd0I2qxdsqlGuSLlqtTBgoKndHE_/${f}?o=AuoILQZ6O-MHJ-g-prxkKJNvAz0wU24Va6re5l5JIhrW&v=1&x=3&a=CAogiV6FTwlLeQt348ipvPuax8JBYrtL7o0q7WMX775pR4YSbRCmkq2nty8Ypu-IqbcvIgEAUgTuqfVRWgSndHE_aiZN21K0DzyVdoR0roYdRIUTUdT16tIhKWq2fJfrIDzHjd0YU3MhW3ImUfLx8SZ3FmkyDDQA-J5nJkGVtdKMsxmegM4H68EIUA9-idz8C-g&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=tPtP2Y7mGQ4yOsOCMFG_sg&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=4MygIoxG8NYN-VK3zWB-a-wqy7c",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resJPEGMedFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resJPEGThumbHeight": {"value": 419, "type": "INT64"},
                            "resJPEGThumbWidth": {"value": 412, "type": "INT64"},
                            "resOriginalWidth": {"value": 2268, "type": "INT64"},
                            "resJPEGThumbFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "dataClassType": {"value": 1, "type": "INT64"},
                            "resOriginalFingerprint": {
                                "value": "ENKzBUr+DdmTaP/GEAglTurWtsen",
                                "type": "STRING",
                            },
                            "resJPEGMedWidth": {"value": 1759, "type": "INT64"},
                            "resJPEGThumbRes": {
                                "value": {
                                    "fileChecksum": "ASy6f/leU1+xkR1aPmQyvYmwHUpE",
                                    "size": 340532,
                                    "wrappingKey": "E1zCp4gxgoHQNQHWjS3Wag==",
                                    "referenceChecksum": "ARHOzkI3sbX3SZDmNQgttNJ9DqQa",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ASy6f_leU1-xkR1aPmQyvYmwHUpEARHOzkI3sbX3SZDmNQgttNJ9DqQa/${f}?o=AiE0LlRJclp9DPkfhwdmJUfxo_vgP7JLWn3qtvPUeTuS&v=1&x=3&a=CAogroLnmMZUEfwNczwEl6zmt6YvBGhwJnPwcJogyD0-dYESbRCmkq2nty8Ypu-IqbcvIgEAUgSwHUpEWgR9DqQaaiZ5SoSlUQbaa-uaRlv6ga8Vyh14lIf466mlURl-3DYa6jr_6SsjQnImlqDZof_hQbcHONiYRrB9MXnKpJ9akb7rPc8_GAwPduNtPHAhBBk&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=E1zCp4gxgoHQNQHWjS3Wag&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=5uuV1dFCaVoK0EhvreVHqYZiBNM",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resOriginalFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resOriginalHeight": {"value": 2306, "type": "INT64"},
                            "resJPEGMedFingerprint": {
                                "value": "NOHzBUr+DdmTaP/SAVglTurWtsen",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3pjr",
                        "created": {
                            "timestamp": 1596388681829,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1619641691167,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3322.JPG
                    {
                        "recordName": "AUxVFT2yVsQ5739tmU5c1497duFD",
                        "recordType": "CPLMaster",
                        "fields": {
                            "itemType": {"value": "public.jpeg", "type": "STRING"},
                            "resJPEGThumbFingerprint": {
                                "value": "ASPVZ/Pft6gIN2VEA/oUbqQzh6Wy",
                                "type": "STRING",
                            },
                            "filenameEnc": {
                                "value": "SU1HXzMzMjIuSlBH",
                                "type": "ENCRYPTED_BYTES",
                            },
                            "resJPEGMedRes": {
                                "value": {
                                    "fileChecksum": "ASTSuc7S58IPmVCJIUslbeCRjsno",
                                    "size": 1074354,
                                    "wrappingKey": "ysHoAuqERA8H3MadxO6+PA==",
                                    "referenceChecksum": "ASIoOBi88potAS0gE8tfnojuSlrb",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ASTSuc7S58IPmVCJIUslbeCRjsnoASIoOBi88potAS0gE8tfnojuSlrb/${f}?o=AotG4ZrSZDU3u6kP4yWDFXfZ3_6tKEyLXvh4gcpo4ELn&v=1&x=3&a=CAogJr6QVcZkN2p9iAoOF0Tr4qnsmeCHSHrFoTzxEHq7NQUSbRCwkq2nty8YsO-IqbcvIgEAUgSRjsnoWgTuSlrbaibzwCZQjqQ5JaCOYReCcRWatftcle04VKPDs1BnZT75v_W_X7tuyXImMWPY8r1ICHzS3Us89foRJ0jtqcXwvVd3nT7EM6EPexOdJAI4_qQ&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=ysHoAuqERA8H3MadxO6-PA&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=TiejMZ9ftbHECNhJzeowymOGu3I",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "originalOrientation": {"value": 1, "type": "INT64"},
                            "resJPEGMedHeight": {"value": 2101, "type": "INT64"},
                            "resOriginalRes": {
                                "value": {
                                    "fileChecksum": "AUxVFT2yVsQ5739tmU5c1497duFD",
                                    "size": 2194253,
                                    "wrappingKey": "8ydPkuUeW1rXYBf+8EUhWQ==",
                                    "referenceChecksum": "AdkoZP1534bwlULpwCdn2fd44LAt",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/AUxVFT2yVsQ5739tmU5c1497duFDAdkoZP1534bwlULpwCdn2fd44LAt/${f}?o=AtyLCU3HpSWYfXnAPtzDXkhqPhQVX_2KI1m03qQMcrX8&v=1&x=3&a=CAoguSOx9xIzgn8O-3JZPJEFmuCqSpNEdkQUdkK-kdTjfyQSbRCwkq2nty8YsO-IqbcvIgEAUgR7duFDWgR44LAtaiYyf1-bnKqpPXGMfJ_iZeMO0Ar6T3qqD2Nwc5hia_fAPn-qOLNguXImMEz0ks6Sun_tBea1p7Gs39vk_ERXdi-KrSpKwpkhrUNPNhAl3t4&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=8ydPkuUeW1rXYBf-8EUhWQ&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=hYKaX0XrV6ghQqijbnjdyNejnec",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resJPEGMedFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resJPEGThumbHeight": {"value": 492, "type": "INT64"},
                            "resJPEGThumbWidth": {"value": 351, "type": "INT64"},
                            "resOriginalWidth": {"value": 2899, "type": "INT64"},
                            "resJPEGThumbFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "dataClassType": {"value": 1, "type": "INT64"},
                            "resOriginalFingerprint": {
                                "value": "AUxVFT2yVsQ5739tmU5c1497duFD",
                                "type": "STRING",
                            },
                            "resJPEGMedWidth": {"value": 1498, "type": "INT64"},
                            "resJPEGThumbRes": {
                                "value": {
                                    "fileChecksum": "ASPVZ/Pft6gIN2VEA/oUbqQzh6Wy",
                                    "size": 340532,
                                    "wrappingKey": "3EAjgkS2+Mr38eqQFk7C0A==",
                                    "referenceChecksum": "AXd258pYF6LLhmADLoZAumNqI+8M",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ASPVZ_Pft6gIN2VEA_oUbqQzh6WyAXd258pYF6LLhmADLoZAumNqI-8M/${f}?o=AtA8VtFypX8-ayXsVGPnssT56G8EM8ZdWr3nFmug2dPM&v=1&x=3&a=CAogZYCSkK2TW_pwByMq7sMg791XyNwx5u0lgyxvV0cKs3YSbRCxkq2nty8Yse-IqbcvIgEAUgQzh6WyWgRqI-8MaibbeMKtZNDpNkTWx6jOoPY4npOZt2t0xHw4QfV3u2b-KI47DIvSOXImJp7IX_oKObj3XLk-Gvvg-9z_e9JYfqbOJyUNAxz_e5wdxr6wQxs&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=3EAjgkS2-Mr38eqQFk7C0A&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=PbVsX_tz5q6QJFzf_TxHZ1SH79I",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resOriginalFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resOriginalHeight": {"value": 4067, "type": "INT64"},
                            "resJPEGMedFingerprint": {
                                "value": "ASTSuc7S58IPmVCJIUslbeCRjsno",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3pjs",
                        "created": {
                            "timestamp": 1595274371241,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1619641691167,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3206.JPG
                    {
                        "recordName": "Ab/8kUAhnGzSxnl9yWvh8JKBpOvV",
                        "recordType": "CPLMaster",
                        "fields": {
                            "itemType": {"value": "public.jpeg", "type": "STRING"},
                            "resJPEGThumbFingerprint": {
                                "value": "AQNND5zpteAXnnBP2BmDd0ropjY9",
                                "type": "STRING",
                            },
                            "filenameEnc": {
                                "value": "SU1HXzMyMDYuSlBH",
                                "type": "ENCRYPTED_BYTES",
                            },
                            "resJPEGMedRes": {
                                "value": {
                                    "fileChecksum": "ATTRy6p+Q3U1HqcF6BUKrrOMnjvn",
                                    "size": 1074354,
                                    "wrappingKey": "pYDpdhqdaL9SAxHilZEj3Q==",
                                    "referenceChecksum": "ATqG89bMsXhtmMRMw009uhyJc/Kh",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ATTRy6p-Q3U1HqcF6BUKrrOMnjvnATqG89bMsXhtmMRMw009uhyJc_Kh/${f}?o=AovA4TUyNl2kYkqOdInhEXGZ_6Lgkx1fTEsqpkkMh3hm&v=1&x=3&a=CAogVnr-sKWlefxaxarlxJ-k7EPRB-Q851T9df9zyhCvis0SbRC7kq2nty8Yu--IqbcvIgEAUgSMnjvnWgSJc_KhaiZCiMEZuykdl4ex2Ra8y53DbEEtJi6ItoX1e6b8TOoWXYiLA-mkr3Im7aDvMFg_m7tYuslgLZFXL8hxJftHL4oTy1ZpuVaP__2nTQTPLp4&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=pYDpdhqdaL9SAxHilZEj3Q&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=IKz0oqClwHpM9shdTb3e5liYV5E",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "originalOrientation": {"value": 1, "type": "INT64"},
                            "resJPEGMedHeight": {"value": 1781, "type": "INT64"},
                            "resOriginalRes": {
                                "value": {
                                    "fileChecksum": "Ab/8kUAhnGzSxnl9yWvh8JKBpOvV",
                                    "size": 2194253,
                                    "wrappingKey": "YIFaf0awZsX16khQaJ5pHw==",
                                    "referenceChecksum": "AVLSGMHt+PAQ9/krqqfXATNX57d5",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/Ab_8kUAhnGzSxnl9yWvh8JKBpOvVAVLSGMHt-PAQ9_krqqfXATNX57d5/${f}?o=AvHBwurT0LTKni3mzYNLu4FnSeLeXfxYgSThZ4ImxjO8&v=1&x=3&a=CAogTIPbEVbPukTNLTRMbKPr3KEw-OwlmwJ6E2P4TWSVmS0SbRC7kq2nty8Yu--IqbcvIgEAUgSBpOvVWgRX57d5aibAoDs2oxjwpsMmZzKDj2ndE0sAhXdcwzBu-U_oZGpb059mW6D0dnImIjbNA_Bqcyw_VKQmNxeLtnGtGwyFB16OPwFKYcs1KsSFvHFAD7Y&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=YIFaf0awZsX16khQaJ5pHw&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=1bdqdYxBN6JqLAkjMyHSEGNkqDA",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resJPEGMedFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resJPEGThumbHeight": {"value": 417, "type": "INT64"},
                            "resJPEGThumbWidth": {"value": 413, "type": "INT64"},
                            "resOriginalWidth": {"value": 1995, "type": "INT64"},
                            "resJPEGThumbFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "dataClassType": {"value": 1, "type": "INT64"},
                            "resOriginalFingerprint": {
                                "value": "Ab/8kUAhnGzSxnl9yWvh8JKBpOvV",
                                "type": "STRING",
                            },
                            "resJPEGMedWidth": {"value": 1765, "type": "INT64"},
                            "resJPEGThumbRes": {
                                "value": {
                                    "fileChecksum": "AQNND5zpteAXnnBP2BmDd0ropjY9",
                                    "size": 340532,
                                    "wrappingKey": "lxLQBw46n1nvea4s30UY+A==",
                                    "referenceChecksum": "AV2Zh7WygJu74eNWVuuMT4lM8qme",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/AQNND5zpteAXnnBP2BmDd0ropjY9AV2Zh7WygJu74eNWVuuMT4lM8qme/${f}?o=ArcD2SL9b5Gy5zcnrnT2luycDRZzFLjOiX-8u9IWdQM2&v=1&x=3&a=CAogfF6-sW-XhnsFDy-vqHQjR8LXVO4OmxBUqG4CZf1zmOwSbRC8kq2nty8YvO-IqbcvIgEAUgTopjY9WgRM8qmeaibiG79B2YhfcchV4W9EgxQXAN4Bpi57NX82WXqo_YW-xi1qLAH9-HImRd8oYhd7r27sXPkUL3GT-rKGSKG-leLeNevi3ay090liNNZH-2U&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=lxLQBw46n1nvea4s30UY-A&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=34vgVK6vLEdlpYceHAmIfqIp1Fk",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resOriginalFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resOriginalHeight": {"value": 2013, "type": "INT64"},
                            "resJPEGMedFingerprint": {
                                "value": "ATTRy6p+Q3U1HqcF6BUKrrOMnjvn",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "2wtv",
                        "created": {
                            "timestamp": 1574869225887,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595187513229,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3148.JPG
                    {
                        "recordName": "AVx3/VKkbWPdNbWw68mrWzSuemXg",
                        "recordType": "CPLMaster",
                        "fields": {
                            "itemType": {"value": "public.jpeg", "type": "STRING"},
                            "resJPEGThumbFingerprint": {
                                "value": "ARpHiouI3Ib/ziuZYTCiSikohvMY",
                                "type": "STRING",
                            },
                            "filenameEnc": {
                                "value": "SU1HXzMxNDguSlBH",
                                "type": "ENCRYPTED_BYTES",
                            },
                            "resJPEGMedRes": {
                                "value": {
                                    "fileChecksum": "ARZd/GzpY62XRtXt+jP6UsV4fBZH",
                                    "size": 1074354,
                                    "wrappingKey": "dmZqsyvxEA4s3CvifNMApA==",
                                    "referenceChecksum": "ATi6BbOzDuHl6RONNFCub9eqZqSm",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ARZd_GzpY62XRtXt-jP6UsV4fBZHATi6BbOzDuHl6RONNFCub9eqZqSm/${f}?o=AkMi62tflbXgUrgSyQZ94SinXG9TYXZ6tydGOmDQx9HG&v=1&x=3&a=CAogc8yqpMgxKnf363cp0n1CujaxnsWY_KrZ3VEN9QchlhcSbRDGkq2nty8Yxu-IqbcvIgEAUgR4fBZHWgSqZqSmaiaxcg1zIsiESwGaEOecYR84r83ltACA6SY5ypGyvYxKD0M3LmqI8HIm7n2S2UL6EBM2Z3a9YFIGX8MrKABFDMA5TXFPUVUP6AfsnKigVMc&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=dmZqsyvxEA4s3CvifNMApA&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=rYmwpGBg6DPYHSGj6UAOnCfuMPk",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "originalOrientation": {"value": 1, "type": "INT64"},
                            "resJPEGMedHeight": {"value": 1747, "type": "INT64"},
                            "resOriginalRes": {
                                "value": {
                                    "fileChecksum": "AVx3/VKkbWPdNbWw68mrWzSuemXg",
                                    "size": 2194253,
                                    "wrappingKey": "Nz2a7ohpe3KPptCk0J0lWA==",
                                    "referenceChecksum": "AdUIDFzHC2rVOvwTz0jPi/tKihnb",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/AVx3_VKkbWPdNbWw68mrWzSuemXgAdUIDFzHC2rVOvwTz0jPi_tKihnb/${f}?o=AksMTyqi4NosuW50ei90oXcv82fP1r-6QocLorp20RpO&v=1&x=3&a=CAogfvU0-_8L-3qRcy6jZsj3Vuqt4aL2rk5xVXF7lwVV6A8SbRDGkq2nty8Yxu-IqbcvIgEAUgSuemXgWgRKihnbaiZoWboa3qYl3KVDo1VGIHrRDoySixw8lzXtf1Y-AnoVN1Pd4hLkPnImXYuLGS8iK7BRJcQg25R5hk54OD04duy2TscnYu1mACOSERXpXEI&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=Nz2a7ohpe3KPptCk0J0lWA&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=t3NT5mCLmsRjPqAGvROVsMrAjfg",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resJPEGMedFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resJPEGThumbHeight": {"value": 409, "type": "INT64"},
                            "resJPEGThumbWidth": {"value": 421, "type": "INT64"},
                            "resOriginalWidth": {"value": 2132, "type": "INT64"},
                            "resJPEGThumbFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "dataClassType": {"value": 1, "type": "INT64"},
                            "resOriginalFingerprint": {
                                "value": "AVx3/VKkbWPdNbWw68mrWzSuemXg",
                                "type": "STRING",
                            },
                            "resJPEGMedWidth": {"value": 1799, "type": "INT64"},
                            "resJPEGThumbRes": {
                                "value": {
                                    "fileChecksum": "ARpHiouI3Ib/ziuZYTCiSikohvMY",
                                    "size": 340532,
                                    "wrappingKey": "UiIQr3rRvyIcoAz/sxDugQ==",
                                    "referenceChecksum": "ARtMrcvA8cbMefPDnmwSWQwe+mBd",
                                    # pylint: disable=C0321
                                    "downloadURL": "https://cvws.icloud-content.com/B/ARpHiouI3Ib_ziuZYTCiSikohvMYARtMrcvA8cbMefPDnmwSWQwe-mBd/${f}?o=Auh2MA-6wuqdRGUDQ4kZL3fuuuMVWVVnTnTcThej9ad5&v=1&x=3&a=CAogaHp1wKKc8QF3MI-2OrLYdQx8V4PIVZvFQyuN1m6pXFMSbRDHkq2nty8Yx--IqbcvIgEAUgQohvMYWgQe-mBdaibQsOQuSEfHUK0xs9nLWG6nHKAvRCwkkmsvXL1Ku9aCARYpDg4mWHImDCoL_RiyOC-KXU_0Jpntuid9MdC08bvpHUp5hkzlctbjsBvT654&e=1629757781&fl=&r=4d5c62f6-c81b-4e60-a785-4139aad087a7-1&k=UiIQr3rRvyIcoAz_sxDugQ&ckc=com.apple.photos.cloud&ckz=PrimarySync&y=1&p=104&s=Rx2sZoVhs_Phm_Ps3RvVwJ2mgvA",  # noqa: E501
                                },
                                "type": "ASSETID",
                            },
                            "resOriginalFileType": {
                                "value": "public.jpeg",
                                "type": "STRING",
                            },
                            "resOriginalHeight": {"value": 2070, "type": "INT64"},
                            "resJPEGMedFingerprint": {
                                "value": "ARZd/GzpY62XRtXt+jP6UsV4fBZH",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "2wwt",
                        "created": {
                            "timestamp": 1572285894332,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595187518048,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # Reference to IMG_3328.JPG
                    {
                        "recordName": "248AFAAE-062C-40BB-92C6-B47084527A9E",
                        "recordType": "CPLAsset",
                        "fields": {
                            "assetDate": {"value": 1596386628825, "type": "TIMESTAMP"},
                            "orientation": {"value": 1, "type": "INT64"},
                            "addedDate": {"value": 1596386628833, "type": "TIMESTAMP"},
                            "assetSubtypeV2": {"value": 0, "type": "INT64"},
                            "assetHDRType": {"value": 0, "type": "INT64"},
                            "timeZoneOffset": {"value": -25200, "type": "INT64"},
                            "masterRef": {
                                "value": {
                                    "recordName": "YN1v8eGiHYYZ/aKUkMuGtSf0P1BN",
                                    "action": "DELETE_SELF",
                                    "zoneID": {
                                        "zoneName": "PrimarySync",
                                        "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                                        "zoneType": "REGULAR_CUSTOM_ZONE",
                                    },
                                },
                                "type": "REFERENCE",
                            },
                            "adjustmentRenderType": {"value": 0, "type": "INT64"},
                            "vidComplDispScale": {"value": 0, "type": "INT64"},
                            "isHidden": {"value": 0, "type": "INT64"},
                            "duration": {"value": 0, "type": "INT64"},
                            "burstFlags": {"value": 0, "type": "INT64"},
                            "assetSubtype": {"value": 0, "type": "INT64"},
                            "vidComplDurScale": {"value": 0, "type": "INT64"},
                            "vidComplDurValue": {"value": 0, "type": "INT64"},
                            "vidComplVisibilityState": {"value": 0, "type": "INT64"},
                            "customRenderedValue": {"value": 0, "type": "INT64"},
                            "isFavorite": {"value": 0, "type": "INT64"},
                            "vidComplDispValue": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3qdm",
                        "created": {
                            "timestamp": 1596388681828,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1622829385777,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # Reference to IMG_3327.JPG
                    {
                        "recordName": "32187DDB-371D-4616-A311-8A3ACA0FA5FE",
                        "recordType": "CPLAsset",
                        "fields": {
                            "assetDate": {"value": 1596386602837, "type": "TIMESTAMP"},
                            "orientation": {"value": 1, "type": "INT64"},
                            "addedDate": {"value": 1596386602843, "type": "TIMESTAMP"},
                            "assetSubtypeV2": {"value": 0, "type": "INT64"},
                            "assetHDRType": {"value": 0, "type": "INT64"},
                            "timeZoneOffset": {"value": -25200, "type": "INT64"},
                            "masterRef": {
                                "value": {
                                    "recordName": "ENKzBUr+DdmTaP/GEAglTurWtsen",
                                    "action": "DELETE_SELF",
                                    "zoneID": {
                                        "zoneName": "PrimarySync",
                                        "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                                        "zoneType": "REGULAR_CUSTOM_ZONE",
                                    },
                                },
                                "type": "REFERENCE",
                            },
                            "adjustmentRenderType": {"value": 0, "type": "INT64"},
                            "vidComplDispScale": {"value": 0, "type": "INT64"},
                            "isHidden": {"value": 0, "type": "INT64"},
                            "duration": {"value": 0, "type": "INT64"},
                            "burstFlags": {"value": 0, "type": "INT64"},
                            "assetSubtype": {"value": 0, "type": "INT64"},
                            "vidComplDurScale": {"value": 0, "type": "INT64"},
                            "vidComplDurValue": {"value": 0, "type": "INT64"},
                            "vidComplVisibilityState": {"value": 0, "type": "INT64"},
                            "customRenderedValue": {"value": 0, "type": "INT64"},
                            "isFavorite": {"value": 0, "type": "INT64"},
                            "vidComplDispValue": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3h64",
                        "created": {
                            "timestamp": 1596388681830,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1596466239177,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "D41A228F-D89E-494A-8EEF-853D461B68CF",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # Reference to IMG_3322.JPG
                    {
                        "recordName": "BEF79215-3125-45B2-A54C-39E47DBFB23A",
                        "recordType": "CPLAsset",
                        "fields": {
                            "assetDate": {"value": 1595267003960, "type": "TIMESTAMP"},
                            "orientation": {"value": 1, "type": "INT64"},
                            "addedDate": {"value": 1595267004003, "type": "TIMESTAMP"},
                            "assetSubtypeV2": {"value": 0, "type": "INT64"},
                            "assetHDRType": {"value": 0, "type": "INT64"},
                            "timeZoneOffset": {"value": -25200, "type": "INT64"},
                            "masterRef": {
                                "value": {
                                    "recordName": "AUxVFT2yVsQ5739tmU5c1497duFD",
                                    "action": "DELETE_SELF",
                                    "zoneID": {
                                        "zoneName": "PrimarySync",
                                        "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                                        "zoneType": "REGULAR_CUSTOM_ZONE",
                                    },
                                },
                                "type": "REFERENCE",
                            },
                            "adjustmentRenderType": {"value": 0, "type": "INT64"},
                            "vidComplDispScale": {"value": 0, "type": "INT64"},
                            "isHidden": {"value": 0, "type": "INT64"},
                            "duration": {"value": 0, "type": "INT64"},
                            "burstFlags": {"value": 0, "type": "INT64"},
                            "assetSubtype": {"value": 0, "type": "INT64"},
                            "vidComplDurScale": {"value": 0, "type": "INT64"},
                            "vidComplDurValue": {"value": 0, "type": "INT64"},
                            "vidComplVisibilityState": {"value": 0, "type": "INT64"},
                            "customRenderedValue": {"value": 0, "type": "INT64"},
                            "isFavorite": {"value": 0, "type": "INT64"},
                            "vidComplDispValue": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3gwf",
                        "created": {
                            "timestamp": 1595274371245,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595274371245,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # Reference to IMG_3206.JPG
                    {
                        "recordName": "97362090-90E4-4F54-A564-14F7ECC02706",
                        "recordType": "CPLAsset",
                        "fields": {
                            "assetDate": {"value": 1574840964935, "type": "TIMESTAMP"},
                            "orientation": {"value": 1, "type": "INT64"},
                            "addedDate": {"value": 1574840964970, "type": "TIMESTAMP"},
                            "assetSubtypeV2": {"value": 0, "type": "INT64"},
                            "assetHDRType": {"value": 0, "type": "INT64"},
                            "timeZoneOffset": {"value": 19800, "type": "INT64"},
                            "masterRef": {
                                "value": {
                                    "recordName": "Ab/8kUAhnGzSxnl9yWvh8JKBpOvV",
                                    "action": "DELETE_SELF",
                                    "zoneID": {
                                        "zoneName": "PrimarySync",
                                        "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                                        "zoneType": "REGULAR_CUSTOM_ZONE",
                                    },
                                },
                                "type": "REFERENCE",
                            },
                            "adjustmentRenderType": {"value": 0, "type": "INT64"},
                            "vidComplDispScale": {"value": 0, "type": "INT64"},
                            "isHidden": {"value": 0, "type": "INT64"},
                            "duration": {"value": 0, "type": "INT64"},
                            "burstFlags": {"value": 0, "type": "INT64"},
                            "assetSubtype": {"value": 0, "type": "INT64"},
                            "vidComplDurScale": {"value": 0, "type": "INT64"},
                            "vidComplDurValue": {"value": 0, "type": "INT64"},
                            "vidComplVisibilityState": {"value": 0, "type": "INT64"},
                            "customRenderedValue": {"value": 0, "type": "INT64"},
                            "isFavorite": {"value": 0, "type": "INT64"},
                            "vidComplDispValue": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "2wtw",
                        "created": {
                            "timestamp": 1574869225891,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595187513229,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # Reference to IMG_3148.JPG
                    {
                        "recordName": "986F607D-E8E0-45C4-B230-EF37B7E40B77",
                        "recordType": "CPLAsset",
                        "fields": {
                            "assetDate": {"value": 1572285626625, "type": "TIMESTAMP"},
                            "orientation": {"value": 1, "type": "INT64"},
                            "addedDate": {"value": 1572285626635, "type": "TIMESTAMP"},
                            "assetSubtypeV2": {"value": 0, "type": "INT64"},
                            "assetHDRType": {"value": 0, "type": "INT64"},
                            "timeZoneOffset": {"value": -25200, "type": "INT64"},
                            "masterRef": {
                                "value": {
                                    "recordName": "AVx3/VKkbWPdNbWw68mrWzSuemXg",
                                    "action": "DELETE_SELF",
                                    "zoneID": {
                                        "zoneName": "PrimarySync",
                                        "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                                        "zoneType": "REGULAR_CUSTOM_ZONE",
                                    },
                                },
                                "type": "REFERENCE",
                            },
                            "adjustmentRenderType": {"value": 0, "type": "INT64"},
                            "vidComplDispScale": {"value": 0, "type": "INT64"},
                            "isHidden": {"value": 0, "type": "INT64"},
                            "duration": {"value": 0, "type": "INT64"},
                            "burstFlags": {"value": 0, "type": "INT64"},
                            "assetSubtype": {"value": 0, "type": "INT64"},
                            "vidComplDurScale": {"value": 0, "type": "INT64"},
                            "vidComplDurValue": {"value": 0, "type": "INT64"},
                            "vidComplVisibilityState": {"value": 0, "type": "INT64"},
                            "customRenderedValue": {"value": 0, "type": "INT64"},
                            "isFavorite": {"value": 0, "type": "INT64"},
                            "vidComplDispValue": {"value": 0, "type": "INT64"},
                        },
                        "pluginFields": {},
                        "recordChangeTag": "2wwu",
                        "created": {
                            "timestamp": 1572285894335,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595187518048,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3328.JPG IN album 2
                    {
                        "recordName": "248AFAAE-062C-40BB-92C6-B47084527A9E-IN-E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                        "recordType": "CPLContainerRelation",
                        "fields": {
                            "itemId": {
                                "value": "248AFAAE-062C-40BB-92C6-B47084527A9E",
                                "type": "STRING",
                            },
                            "isKeyAsset": {"value": 0, "type": "INT64"},
                            "position": {"value": 6144, "type": "INT64"},
                            "containerId": {
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3h4p",
                        "created": {
                            "timestamp": 1596388681830,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1596388681830,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3327.JPG in album 2
                    {
                        "recordName": "32187DDB-371D-4616-A311-8A3ACA0FA5FE-IN-E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                        "recordType": "CPLContainerRelation",
                        "fields": {
                            "itemId": {
                                "value": "32187DDB-371D-4616-A311-8A3ACA0FA5FE",
                                "type": "STRING",
                            },
                            "isKeyAsset": {"value": 0, "type": "INT64"},
                            "position": {"value": 5120, "type": "INT64"},
                            "containerId": {
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3h4q",
                        "created": {
                            "timestamp": 1596388681830,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1596388681830,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3322.JPG in album 2
                    {
                        "recordName": "BEF79215-3125-45B2-A54C-39E47DBFB23A-IN-E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                        "recordType": "CPLContainerRelation",
                        "fields": {
                            "itemId": {
                                "value": "BEF79215-3125-45B2-A54C-39E47DBFB23A",
                                "type": "STRING",
                            },
                            "isKeyAsset": {"value": 0, "type": "INT64"},
                            "position": {"value": 4096, "type": "INT64"},
                            "containerId": {
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3gwj",
                        "created": {
                            "timestamp": 1595274371883,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595274371883,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3206.JPG in album 2
                    {
                        "recordName": "97362090-90E4-4F54-A564-14F7ECC02706-IN-E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                        "recordType": "CPLContainerRelation",
                        "fields": {
                            "itemId": {
                                "value": "97362090-90E4-4F54-A564-14F7ECC02706",
                                "type": "STRING",
                            },
                            "isKeyAsset": {"value": 0, "type": "INT64"},
                            "position": {"value": 3072, "type": "INT64"},
                            "containerId": {
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3f4w",
                        "created": {
                            "timestamp": 1574869421700,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595190034254,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                    # IMG_3148.JPG in album 2
                    {
                        "recordName": "986F607D-E8E0-45C4-B230-EF37B7E40B77-IN-E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                        "recordType": "CPLContainerRelation",
                        "fields": {
                            "itemId": {
                                "value": "986F607D-E8E0-45C4-B230-EF37B7E40B77",
                                "type": "STRING",
                            },
                            "isKeyAsset": {"value": 0, "type": "INT64"},
                            "position": {"value": 2048, "type": "INT64"},
                            "containerId": {
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                                "type": "STRING",
                            },
                        },
                        "pluginFields": {},
                        "recordChangeTag": "3f7a",
                        "created": {
                            "timestamp": 1572285894336,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "modified": {
                            "timestamp": 1595190039047,
                            "userRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "deviceID": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                        },
                        "deleted": False,
                        "zoneID": {
                            "zoneName": "PrimarySync",
                            "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                            "zoneType": "REGULAR_CUSTOM_ZONE",
                        },
                    },
                ],
                "syncToken": "AQAAAAAAArKjf//////////fSxWSKv5JfZ34edrt875d",
            },
        },
        {
            "data": {
                "query": {
                    "filterBy": [
                        {
                            "fieldName": "startRank",
                            "fieldValue": {"type": "INT64", "value": 5},
                            "comparator": "EQUALS",
                        },
                        {
                            "fieldName": "direction",
                            "fieldValue": {"type": "STRING", "value": "ASCENDING"},
                            "comparator": "EQUALS",
                        },
                        {
                            "fieldName": "parentId",
                            "comparator": "EQUALS",
                            "fieldValue": {
                                "type": "STRING",
                                "value": "E4RT4FB7-4A35-4958-1D42-5769E66BE407",
                            },
                        },
                    ],
                    "recordType": "CPLContainerRelationLiveByAssetDate",
                },
                "resultsLimit": 200,
                "desiredKeys": [
                    "resJPEGFullWidth",
                    "resJPEGFullHeight",
                    "resJPEGFullFileType",
                    "resJPEGFullFingerprint",
                    "resJPEGFullRes",
                    "resJPEGLargeWidth",
                    "resJPEGLargeHeight",
                    "resJPEGLargeFileType",
                    "resJPEGLargeFingerprint",
                    "resJPEGLargeRes",
                    "resJPEGMedWidth",
                    "resJPEGMedHeight",
                    "resJPEGMedFileType",
                    "resJPEGMedFingerprint",
                    "resJPEGMedRes",
                    "resJPEGThumbWidth",
                    "resJPEGThumbHeight",
                    "resJPEGThumbFileType",
                    "resJPEGThumbFingerprint",
                    "resJPEGThumbRes",
                    "resVidFullWidth",
                    "resVidFullHeight",
                    "resVidFullFileType",
                    "resVidFullFingerprint",
                    "resVidFullRes",
                    "resVidMedWidth",
                    "resVidMedHeight",
                    "resVidMedFileType",
                    "resVidMedFingerprint",
                    "resVidMedRes",
                    "resVidSmallWidth",
                    "resVidSmallHeight",
                    "resVidSmallFileType",
                    "resVidSmallFingerprint",
                    "resVidSmallRes",
                    "resSidecarWidth",
                    "resSidecarHeight",
                    "resSidecarFileType",
                    "resSidecarFingerprint",
                    "resSidecarRes",
                    "itemType",
                    "dataClassType",
                    "filenameEnc",
                    "originalOrientation",
                    "resOriginalWidth",
                    "resOriginalHeight",
                    "resOriginalFileType",
                    "resOriginalFingerprint",
                    "resOriginalRes",
                    "resOriginalAltWidth",
                    "resOriginalAltHeight",
                    "resOriginalAltFileType",
                    "resOriginalAltFingerprint",
                    "resOriginalAltRes",
                    "resOriginalVidComplWidth",
                    "resOriginalVidComplHeight",
                    "resOriginalVidComplFileType",
                    "resOriginalVidComplFingerprint",
                    "resOriginalVidComplRes",
                    "isDeleted",
                    "isExpunged",
                    "dateExpunged",
                    "remappedRef",
                    "recordName",
                    "recordType",
                    "recordChangeTag",
                    "masterRef",
                    "adjustmentRenderType",
                    "assetDate",
                    "addedDate",
                    "isFavorite",
                    "isHidden",
                    "orientation",
                    "duration",
                    "assetSubtype",
                    "assetSubtypeV2",
                    "assetHDRType",
                    "burstFlags",
                    "burstFlagsExt",
                    "burstId",
                    "captionEnc",
                    "locationEnc",
                    "locationV2Enc",
                    "locationLatitude",
                    "locationLongitude",
                    "adjustmentType",
                    "timeZoneOffset",
                    "vidComplDurValue",
                    "vidComplDurScale",
                    "vidComplDispValue",
                    "vidComplDispScale",
                    "vidComplVisibilityState",
                    "customRenderedValue",
                    "containerId",
                    "itemId",
                    "position",
                    "isKeyAsset",
                ],
                "zoneID": {"zoneName": "PrimarySync"},
            },
            "response": {
                "records": [],
                "syncToken": "AQAAAAAAArKjf//////////fSxWSKv5JfZ34edrt875d",
            },
        },
    ],
    "query/batch?remapEnums=True&getCurrentSyncToken=True": [
        {
            "data": {
                "batch": [
                    {
                        "resultsLimit": 1,
                        "query": {
                            "filterBy": {
                                "fieldName": "indexCountID",
                                "fieldValue": {
                                    "type": "STRING_LIST",
                                    "value": [
                                        "CPLContainerRelationNotDeletedByAssetDate:E4RT4FB7-4A35-4958-1D42-5769E66BE407"
                                    ],
                                },
                                "comparator": "IN",
                            },
                            "recordType": "HyperionIndexCountLookup",
                        },
                        "zoneWide": True,
                        "zoneID": {"zoneName": "PrimarySync"},
                    }
                ]
            },
            "response": {
                "batch": [
                    {
                        "records": [
                            {
                                # pylint: disable=C0321
                                "recordName": "CPLContainerRelationNotDeletedByAssetDate:E4RT4FB7-4A35-4958-1D42-5769E66BE407",  # noqa: E501
                                "recordType": "IndexCountResult",
                                "fields": {"itemCount": {"value": 5, "type": "INT64"}},
                                "pluginFields": {},
                                "recordChangeTag": "0",
                                "created": {
                                    "timestamp": 1629754181247,
                                    "userRecordName": "_10",
                                    "deviceID": "1",
                                },
                                "modified": {
                                    "timestamp": 1629754181247,
                                    "userRecordName": "_10",
                                    "deviceID": "1",
                                },
                                "deleted": False,
                                "zoneID": {
                                    "zoneName": "PrimarySync",
                                    "ownerRecordName": "_1d5r3c201b3a4r5daac8ff7e7fbc0c23",
                                    "zoneType": "REGULAR_CUSTOM_ZONE",
                                },
                            }
                        ],
                        "syncToken": "AQAAAAAAArKjf//////////fSxWSKv5JfZ34edrt875d",
                    }
                ]
            },
        }
    ],
    "https://cvws.icloud-content.com/B/": [],
}
