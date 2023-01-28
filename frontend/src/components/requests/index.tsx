import axios from 'axios';

const apiOCTranspo = axios.create({
    baseURL: `${process.env.REACT_APP_API}`,
});

export interface ParamsOCT {
    stopNo: string,
}

const Request = {
    oct: {
        get: (params: ParamsOCT) => apiOCTranspo.get(
            'oct',
            { params },
        ),
    },
};

export default Request;
