# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="SignDigitalOptionsData.py">
#   Copyright (c) 2018 Aspose Pty Ltd
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six

from groupdocs_signature_cloud.models import SignImageOptionsData
class SignDigitalOptionsData(SignImageOptionsData):
    """Represents the Digital Sign Options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'password': 'str',
        'certificate_guid': 'str'
    }

    attribute_map = {
        'password': 'Password',
        'certificate_guid': 'CertificateGuid'
    }

    def __init__(self, password=None, certificate_guid=None):  # noqa: E501
        """SignDigitalOptionsData - a model defined in Swagger"""  # noqa: E501
        SignImageOptionsData.__init__(self)
        self.swagger_types.update(SignImageOptionsData.swagger_types)
        self.attribute_map.update(SignImageOptionsData.attribute_map)

        self._password = None
        self._certificate_guid = None
        self.discriminator = None
        self.options_type = "SignDigitalOptionsData"

        if password is not None:
            self.password = password
        if certificate_guid is not None:
            self.certificate_guid = certificate_guid

    @property
    def password(self):
        """Gets the password of this SignDigitalOptionsData.  # noqa: E501

        Gets or sets the password of digital certificate.  # noqa: E501

        :return: The password of this SignDigitalOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SignDigitalOptionsData.

        Gets or sets the password of digital certificate.  # noqa: E501

        :param password: The password of this SignDigitalOptionsData.  # noqa: E501
        :type: str
        """
        self._password = password
    @property
    def certificate_guid(self):
        """Gets the certificate_guid of this SignDigitalOptionsData.  # noqa: E501

        Gets or sets the digital certificate file GUID.  # noqa: E501

        :return: The certificate_guid of this SignDigitalOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._certificate_guid

    @certificate_guid.setter
    def certificate_guid(self, certificate_guid):
        """Sets the certificate_guid of this SignDigitalOptionsData.

        Gets or sets the digital certificate file GUID.  # noqa: E501

        :param certificate_guid: The certificate_guid of this SignDigitalOptionsData.  # noqa: E501
        :type: str
        """
        self._certificate_guid = certificate_guid
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignDigitalOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
