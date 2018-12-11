# coding: utf-8\n\r--------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# <copyright company="Aspose Pty Ltd" file="post_digital_from_url_request.py">
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
# --------------------------------------------------------------------------------


class PostDigitalFromUrlRequest(object):
    """
    Request model for post_digital_from_url operation.
    Initializes a new instance.
    :param url The URL to retrieve document.
    :param sign_options_data Digital Signature Options for corresponding Document Type
    :param password Document password if required.
    :param certificate_file Digital certificate file name.
    :param image_file Image file.
    :param storage The file storage which have to be used.
    """

    def __init__(self, url, sign_options_data=None, password=None, certificate_file=None, image_file=None, storage=None):
        self.url = url
        self.sign_options_data = sign_options_data
        self.password = password
        self.certificate_file = certificate_file
        self.image_file = image_file
        self.storage = storage
